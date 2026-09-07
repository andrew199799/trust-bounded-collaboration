"""Runnable use-case acceptance through the frozen public API."""
import copy
import json
import os
from pathlib import Path
import runpy
import socket
import subprocess
import time

import pytest

from tbc import action_digest, dumps_receipt, evaluate


EXAMPLES = Path(__file__).resolve().parents[1] / "examples"
EXPECTED = {
    "approval_bound_action": {
        "approved_action": [],
        "approval_absent": ["AUTHORITY_MISSING"],
        "changed_action_old_grant": ["ACTION_BINDING_MISMATCH"],
    },
    "evidence_bound_transition": {
        "ready_transition": [],
        "missing_evidence": ["EVIDENCE_MISSING"],
        "stale_evidence": ["EVIDENCE_NOT_CURRENT"],
        "failed_evidence": ["EVIDENCE_FAILED"],
        "mismatched_evidence": ["EVIDENCE_BINDING_MISMATCH"],
        "changed_action_old_policy": ["POLICY_BINDING_MISMATCH"],
        "changed_action_old_evidence": ["EVIDENCE_BINDING_MISMATCH"],
    },
    "scoped_blocker": {
        "blocked_transition": ["EVIDENCE_MISSING"],
        "independent_inspection": [],
    },
}


def example(name):
    return runpy.run_path(str(EXAMPLES / (name + ".py")))


@pytest.mark.parametrize("module,name,reasons", [
    (module, name, reasons)
    for module, cases in EXPECTED.items() for name, reasons in cases.items()
])
def test_example_contract(module, name, reasons):
    request, context = example(module)["scenarios"]()[name]
    before = copy.deepcopy((request, context))
    receipt = evaluate(request, context=context)
    assert receipt["decision"] == ("DENY" if reasons else "ALLOW")
    assert receipt["reason_codes"] == reasons
    assert receipt["executed"] is False
    assert receipt["action_digest"] == action_digest(request["action"])
    assert receipt["affected_transition"] == request["action"]["transition"]
    assert json.loads(dumps_receipt(receipt)) == receipt
    assert (request, context) == before


@pytest.mark.parametrize("module", EXPECTED)
@pytest.mark.parametrize("field", ["actor", "resource", "transition", "payload"])
def test_new_action_cannot_reuse_example_authority(module, field):
    cases = example(module)["scenarios"]()
    name = next(name for name, reasons in EXPECTED[module].items() if not reasons)
    request, context = cases[name]
    request["action"][field] = {"revision": "changed"} if field == "payload" else "different"
    receipt = evaluate(request, context=context)
    assert receipt["decision"] == "DENY"
    assert "ACTION_BINDING_MISMATCH" in receipt["reason_codes"]
    assert "POLICY_BINDING_MISMATCH" in receipt["reason_codes"]
    assert receipt["executed"] is False


@pytest.mark.parametrize("module", EXPECTED)
def test_script_output_is_deterministic_and_offline(module, monkeypatch, capsys):
    def forbidden(*args, **kwargs):
        raise AssertionError("example crossed offline boundary")
    monkeypatch.setattr(socket, "socket", forbidden)
    monkeypatch.setattr(subprocess, "Popen", forbidden)
    monkeypatch.setattr(os, "system", forbidden)
    monkeypatch.setattr(time, "time", forbidden)
    monkeypatch.setattr(Path, "write_text", forbidden)
    monkeypatch.setattr(Path, "write_bytes", forbidden)
    outputs = []
    for _ in range(2):
        runpy.run_path(str(EXAMPLES / (module + ".py")), run_name="__main__")
        outputs.append(capsys.readouterr().out)
    assert outputs[0] == outputs[1]
    result = json.loads(outputs[0])
    assert result["simulation"] is True
    assert set(result["cases"]) == set(EXPECTED[module])
    for name, reasons in EXPECTED[module].items():
        receipt = result["cases"][name]
        assert receipt["reason_codes"] == reasons
        assert receipt["decision"] == ("DENY" if reasons else "ALLOW")
        assert receipt["executed"] is False


def test_blocked_and_safe_work_remain_independent_in_either_order():
    cases = example("scoped_blocker")["scenarios"]()
    before = copy.deepcopy(cases)
    results = []
    for names in (list(cases), list(reversed(cases)), list(cases)):
        results.append({name: evaluate(cases[name][0], context=cases[name][1]) for name in names})
    assert results[0] == results[1] == results[2]
    blocked, safe = (results[0][name] for name in EXPECTED["scoped_blocker"])
    assert blocked["decision"] == "DENY" and safe["decision"] == "ALLOW"
    assert blocked["affected_transition"] != safe["affected_transition"]
    assert blocked["action_digest"] != safe["action_digest"]
    assert cases == before
