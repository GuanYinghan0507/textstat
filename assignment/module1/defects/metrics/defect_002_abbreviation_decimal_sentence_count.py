r"""Regression verification for TEXTSTAT-BUG-002.

Related source patch (local fix):
- textstat/backend/counts/_count_sentences.py

Run from the repository root:
    .venv/Scripts/python.exe assignment/module1/defects/metrics/defect_002_abbreviation_decimal_sentence_count.py
"""

from __future__ import annotations

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[4]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import textstat  # noqa: E402


def verify() -> None:
    textstat.set_lang("en_US")
    samples = [
        (
            "The meeting was led by Dr. Smith at 3.14 p.m. We left after lunch.",
            2,
        ),
        (
            "The project cost 3.14 million dollars. We approved the budget.",
            2,
        ),
    ]

    for text, expected in samples:
        actual = textstat.sentence_count(text)
        assert actual == expected, (
            f"expected {expected} sentences for {text!r}, got {actual}"
        )
        print(f"PASS TEXTSTAT-BUG-002: {actual} sentences -> {text!r}")


if __name__ == "__main__":
    verify()
