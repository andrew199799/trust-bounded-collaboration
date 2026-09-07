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
with tarfile.open(sdist) as archive:
    names = archive.getnames()
    assert not any("/tbao/" in n or "/docs/" in n or "/social/" in n for n in names)
    assert any(n.endswith("/src/tbc/__init__.py") for n in names)
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
    subprocess.run([str(python), "-I", str(root / "examples/tbc_integration.py")], cwd=temp, check=True, capture_output=True)
elapsed = time.monotonic() - started
assert elapsed < 600
print(json.dumps({"wheel_contents": "PASS", "sdist_contents": "PASS", "clean_install": "PASS", "first_run_seconds": round(elapsed, 3)}))
