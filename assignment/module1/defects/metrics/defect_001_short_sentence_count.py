r"""Regression verification for TEXTSTAT-BUG-001.

Related source patches (local fix):
- textstat/backend/counts/_count_sentences.py
- textstat/backend/metrics/_automated_readability_index.py

Run from the repository root:
    .venv/Scripts/python.exe assignment/module1/defects/metrics/defect_001_short_sentence_count.py
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
    text = "Hi. How are you?"

    sentence_count = textstat.sentence_count(text)
    ari = textstat.automated_readability_index(text)

    assert sentence_count == 2, f"expected 2 sentences, got {sentence_count}"
    assert abs(ari - (-1.59)) < 1e-3, f"expected ARI -1.59, got {ari}"

    print(f"PASS TEXTSTAT-BUG-001: sentence_count={sentence_count}, ARI={ari:.4f}")


if __name__ == "__main__":
    verify()
