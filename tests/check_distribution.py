"""Inspect built artifacts and measure a clean, offline wheel first run."""
from email.parser import Parser
import json
import os
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import time
import zipfile


def assert_python_range(metadata):
    values = Parser().parsestr(metadata).get_all("Requires-Python", [])
    assert len(values) == 1, "Exactly one Requires-Python header is required"
    assert {part.strip() for part in values[0].split(",")} == {">=3.11", "<3.15"}, values[0]


CURRENT_EXAMPLES = (
    "tbc_integration.py", "approval_bound_action.py",
    "evidence_bound_transition.py", "scoped_blocker.py",
)
root = Path(__file__).resolve().parents[1]
wheel, = (root / "dist").glob("*.whl")
sdist, = (root / "dist").glob("*.tar.gz")
with zipfile.ZipFile(wheel) as archive:
    names = archive.namelist()
    assert any(n == "tbc/__init__.py" for n in names)
    assert all(n.startswith("tbc/") or ".dist-info/" in n for n in names)
    license_name, = [n for n in names if n.endswith("/licenses/LICENSE")]
    assert archive.read(license_name) == (root / "LICENSE").read_bytes()
    metadata_name, = [n for n in names if n.endswith("/METADATA")]
    metadata = archive.read(metadata_name).decode()
    assert_python_range(metadata)
    assert "License-Expression: MIT" in metadata
    assert "Requires-Dist:" not in metadata
    assert Parser().parsestr(metadata)["Version"] == "1.0.0a1"
source_examples = {}
with tarfile.open(sdist) as archive:
    names = archive.getnames()
    assert not any("/tbao/" in n or "/social/" in n for n in names)
    assert any(n.endswith("/src/tbc/__init__.py") for n in names)
    relative = {n.split("/", 1)[-1]: n for n in names}
    # Admit only the current capability map, not the historical documentation tree.
    assert {n for n in relative if n.startswith("docs/")} == {"docs/capability-disposition.md"}
    for name in ("README.md", "README.zh-CN.md", "docs/capability-disposition.md"):
        assert archive.extractfile(relative[name]).read() == (root / name).read_bytes()
    for name, other in (("README.md", "README.zh-CN.md"), ("README.zh-CN.md", "README.md")):
        readme = archive.extractfile(relative[name]).read().decode("utf-8")
        assert "](" + other + ")" in readme
        assert "`1.0.0a1`" in readme
    expected_examples = {"examples/README.md", *("examples/" + n for n in CURRENT_EXAMPLES)}
    assert {n for n in relative if n.startswith("examples/")} == expected_examples
    assert "tests/test_tbc_examples.py" in relative
    for name in CURRENT_EXAMPLES:
        data = archive.extractfile(relative["examples/" + name]).read()
        assert data == (root / "examples" / name).read_bytes()
        source_examples[name] = data
    metadata_name, = [n for n in names if n.split("/", 1)[-1] == "PKG-INFO"]
    assert_python_range(archive.extractfile(metadata_name).read().decode())

started = time.monotonic()
with tempfile.TemporaryDirectory() as temp:
    env_root = Path(temp) / "clean"
    subprocess.run([sys.executable, "-m", "venv", str(env_root)], check=True, capture_output=True)
    bindir = env_root / ("Scripts" if os.name == "nt" else "bin")
    python = bindir / ("python.exe" if os.name == "nt" else "python")
    subprocess.run([str(python), "-m", "pip", "install", "--no-index", "--no-deps", str(wheel)], check=True, capture_output=True)
    result = subprocess.check_output([str(python), "-I", "-m", "tbc", "demo", "repository", "--json"], cwd=temp, text=True)
    assert json.loads(result)["simulation"] is True
    command = bindir / ("tbc.exe" if os.name == "nt" else "tbc")
    assert subprocess.check_output([str(command), "demo", "repository", "--json"], cwd=temp, text=True) == result
    probe = "import importlib.util; assert importlib.util.find_spec('tbao') is None"
    subprocess.run([str(python), "-I", "-c", probe], cwd=temp, check=True, capture_output=True)
    # Run the exact scripts shipped in the sdist against only the installed wheel,
    # from outside the checkout. -I excludes checkout/PYTHONPATH import leakage.
    for name, data in source_examples.items():
        script = Path(temp) / name
        script.write_bytes(data)
        args = [str(python), "-I", str(script)]
        output = subprocess.check_output(args, cwd=temp, text=True)
        assert subprocess.check_output(args, cwd=temp, text=True) == output
        result = json.loads(output)
        if name == "tbc_integration.py":
            assert result["decision"] == "ALLOW" and result["executed"] is False
        else:
            assert result["simulation"] is True
            assert result["cases"]
            assert all(r["executed"] is False for r in result["cases"].values())
elapsed = time.monotonic() - started
assert elapsed < 600
print(json.dumps({"wheel_contents": "PASS", "sdist_contents": "PASS", "clean_install": "PASS", "current_examples": len(CURRENT_EXAMPLES), "first_run_seconds": round(elapsed, 3)}))
