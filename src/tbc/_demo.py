"""Synthetic host profile; intentionally no live collection or execution."""
from copy import deepcopy
import re

from . import action_digest, evaluate

_NOW = 100
_OBSERVATION = {
    "canonical": "demo/canonical", "contributor": "demo/contributor",
    "principal": "demo-agent", "canonical_permission": "read", "contributor_permission": "write",
}


def _context(action, observation):
    # In an actual integration these are independently verified host facts.
    digest = action_digest(action)
    canonical, contributor = observation["canonical"], observation["contributor"]
    known = canonical != contributor and action["resource"] in (canonical, contributor)
    identity = observation["principal"] == action["actor"]
    roles = observation["canonical_permission"] == "read" and observation["contributor_permission"] == "write"
    inspect = action["transition"] == "inspect"
    payload = action["payload"]
    proposal = (action["transition"] == "propose" and action["resource"] == contributor
                and payload.get("ref", "").startswith("refs/heads/")
                and payload.get("ref") != "refs/heads/main"
                and payload.get("fast_forward") is True
                and re.fullmatch(r"[0-9a-f]{40}", payload.get("head", "")) is not None)
    permitted = known and identity and roles and (inspect or proposal)
    return {
        "schema": "tbc.context.v1", "evaluation_time": _NOW,
        "authenticated_actor": observation["principal"], "action_digest": digest,
        "grant": {"id": "demo-grant", "issuer": "demo-host", "action_digest": digest,
                  "not_before": 90, "expires_at": 110},
        "policy": {"id": "demo-repository-profile", "version": "1", "digest": "sha256:" + "1" * 64,
                   "action_digest": digest, "decision": "ALLOW" if permitted else "DENY",
                   "not_before": 90, "expires_at": 110, "required_evidence_ids": ["repository-observation"]},
        "evidence": [{"id": "repository-observation", "subject_digest": digest,
                      "verifier": "demo-host", "observed_at": 90, "expires_at": 110, "passed": True}],
    }


def repository_demo():
    action = {"actor": "demo-agent", "transition": "propose", "resource": "demo/contributor",
              "payload": {"ref": "refs/heads/task-demo", "head": "a" * 40, "fast_forward": True}}
    cases = []

    def add(name, action, expected, context=None, observation=None):
        if context is None:
            context = _context(action, observation or _OBSERVATION)
        receipt = evaluate({"schema": "tbc.request.v1", "action": action}, context=context)
        cases.append({"name": name, "expected": expected, "receipt": receipt})

    add("contributor_proposal", action, "ALLOW")
    for name, transition in [("canonical_main", "push"), ("canonical_tag", "tag"),
                             ("canonical_delete", "delete"), ("canonical_non_ff", "force_push"),
                             ("agent_merge", "merge"), ("agent_release", "release")]:
        changed = deepcopy(action)
        changed.update(resource="demo/canonical", transition=transition)
        changed["payload"]["ref"] = "refs/tags/demo" if transition == "tag" else "refs/heads/main"
        add(name, changed, "DENY")
    changed = deepcopy(action)
    changed["payload"]["head"] = "b" * 40
    add("changed_proposal", changed, "DENY", context=_context(action, _OBSERVATION))
    add("ambiguous_repository", action, "DENY",
        observation={**_OBSERVATION, "canonical": "demo/contributor"})
    add("unknown_operation", {**action, "transition": "unknown"}, "DENY")
    add("independent_inspection", {**action, "transition": "inspect", "resource": "demo/canonical"}, "ALLOW")
    return {"simulation": True, "cases": cases}
