"""Fixed, credential-free demo CLI; no arbitrary authority or action runner."""
import argparse
import json

from . import __version__
from ._demo import repository_demo


def main(argv=None):
    parser = argparse.ArgumentParser(prog="tbc", description="Offline exact-action evaluation demo")
    parser.add_argument("--version", action="version", version=__version__)
    commands = parser.add_subparsers(dest="command", required=True)
    demo = commands.add_parser("demo", help="Run fixed synthetic scenarios")
    demo.add_argument("scenario", choices=["repository"])
    demo.add_argument("--json", action="store_true", help="Emit deterministic JSON (the default)")
    parser.parse_args(argv)
    result = repository_demo()
    print(json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False))
    return 0 if all(case["receipt"]["decision"] == case["expected"] for case in result["cases"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
