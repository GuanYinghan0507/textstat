r"""Regression verification for TEXTSTAT-BUG-003.

Related source patches (local fix):
- textstat/backend/validations/_is_difficult_word.py
- textstat/resources/en/easy_words.txt

Run from the repository root:
    .venv/Scripts/python.exe assignment/module1/defects/metrics/defect_003_difficult_word_inflections.py
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
    text = "Scotland returned. The giants strongest form was giant's."
    expected_words = ["Scotland", "returned", "giants", "strongest", "giant's"]

    difficult_words = textstat.difficult_words_list(text)
    difficult_count = textstat.difficult_words(text)

    assert difficult_words == [], f"expected no difficult words, got {difficult_words}"
    assert difficult_count == 0, f"expected difficult_words=0, got {difficult_count}"

    for word in expected_words:
        assert not textstat.is_difficult_word(word), (
            f"{word!r} should be treated as familiar"
        )

    print(
        "PASS TEXTSTAT-BUG-003: "
        f"difficult_words={difficult_count}, list={difficult_words}"
    )


if __name__ == "__main__":
    verify()
