"""One-command environment setup and execution for the 37 AI-designed cases."""

from __future__ import annotations

import os
import subprocess
import sys
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def python_in(venv_dir: Path) -> Path:
    if os.name == "nt":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"


def prepare(name: str, requirements: str) -> Path:
    env_dir = ROOT / name
    python = python_in(env_dir)
    if not python.exists():
        print(f"Creating {name}...", flush=True)
        venv.EnvBuilder(with_pip=True).create(env_dir)
    stamp = env_dir / ".requirements-ready"
    wanted = (ROOT / requirements).read_text(encoding="utf-8")
    if not stamp.exists() or stamp.read_text(encoding="utf-8") != wanted:
        print(f"Installing {requirements} into {name}...", flush=True)
        subprocess.run(
            [str(python), "-m", "pip", "install", "-r", str(ROOT / requirements)],
            check=True,
        )
        stamp.write_text(wanted, encoding="utf-8")
    return python


def main() -> int:
    if sys.version_info < (3, 10):
        print("Python 3.10 or newer is required for this test project.", file=sys.stderr)
        return 2
    try:
        main_python = prepare(".venv-main", "requirements-main.txt")
        compat_python = prepare(".venv-compat", "requirements-compat.txt")
    except subprocess.CalledProcessError as exc:
        print(f"Dependency installation failed: {exc}", file=sys.stderr)
        return 2

    env = os.environ.copy()
    env["TEXTSTAT077_COMPAT_PYTHON"] = str(compat_python)
    env["PYTHONNOUSERSITE"] = "1"
    command = [
        str(main_python), "-m", "pytest", "-ra", "-q", "tests",
        "--junitxml=results/junit.xml",
    ]
    print("Running all 37 cases...", flush=True)
    result = subprocess.run(command, cwd=ROOT, env=env, check=False)
    print("JUnit report: results/junit.xml", flush=True)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
