"""Offline public entry-point acceptance, without fixture implementation oracles."""
import json
import os
import subprocess
import sys

import pytest


@pytest.mark.parametrize("args", [["demo", "repository", "--json"], ["demo", "repository"]])
def test_demo_expected_denials_are_success(args):
    result = subprocess.run([sys.executable, "-m", "tbc", *args], capture_output=True, text=True)
    assert result.returncode == 0
    data = json.loads(result.stdout)
    assert data["simulation"] is True
    results = {item["name"]: item["receipt"] for item in data["cases"]}
    assert results["contributor_proposal"]["decision"] == "ALLOW"
    assert results["independent_inspection"]["decision"] == "ALLOW"
    for name in ["canonical_main", "canonical_tag", "canonical_delete", "canonical_non_ff",
                 "agent_merge", "agent_release", "changed_proposal", "ambiguous_repository", "unknown_operation"]:
        assert results[name]["decision"] == "DENY"
    assert all(receipt["executed"] is False for receipt in results.values())
    assert result.stdout == subprocess.check_output([sys.executable, "-m", "tbc", *args], text=True)


@pytest.mark.parametrize("args,code", [(["--help"], 0), (["--version"], 0),
                                      ([], 2), (["run"], 2), (["demo", "live"], 2)])
def test_cli_boundary(args, code):
    result = subprocess.run([sys.executable, "-m", "tbc", *args], capture_output=True, text=True)
    assert result.returncode == code


def test_demo_has_no_network_clock_or_process_actions(monkeypatch, capsys):
    import socket
    import time
    import tbc.__main__ as cli
    def forbidden(*args, **kwargs):
        raise AssertionError("demo crossed execution boundary")
    monkeypatch.setattr(socket, "socket", forbidden)
    monkeypatch.setattr(subprocess, "Popen", forbidden)
    monkeypatch.setattr(os, "system", forbidden)
    monkeypatch.setattr(time, "time", forbidden)
    assert cli.main(["demo", "repository", "--json"]) == 0
    assert json.loads(capsys.readouterr().out)["simulation"] is True


def test_unexpected_demo_result_exits_one(monkeypatch, capsys):
    import tbc.__main__ as cli
    monkeypatch.setattr(cli, "repository_demo", lambda: {
        "simulation": True, "cases": [{"name": "broken", "expected": "ALLOW",
                                         "receipt": {"decision": "DENY"}}]})
    assert cli.main(["demo", "repository", "--json"]) == 1
    assert json.loads(capsys.readouterr().out)["simulation"] is True
