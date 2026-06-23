"""Convenience launcher for LogicBot."""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from chatbot import run_chatbot  # noqa: E402


if __name__ == "__main__":
    run_chatbot()
