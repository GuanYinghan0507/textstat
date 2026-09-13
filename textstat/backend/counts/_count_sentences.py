from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ._count_words import count_words

# 常见缩写（用于区分“被句点切开的缩写”与“真正的短句”）
_ABBREVIATIONS = {
    "dr",
    "mr",
    "mrs",
    "ms",
    "prof",
    "st",
    "jr",
    "sr",
    "vs",
    "etc",
    "no",
    "fig",
    "vol",
    "e.g",
    "i.e",
    "u.s",
    "u.k",
    "t.v",
}


def _is_fragment(sentence: str) -> bool:
    """判断短片段是否为缩写或被截断的句尾残片。

    以省略号结尾的片段表示停顿而非句末；句尾没有终止标点（. ! ?）的片段视为
    残片；以缩写（如 Dr.、V.）结尾的片段视为缩写的一部分。以上情况都不应单独
    计为一句，其余短句应正常计数。
    """
    stripped = sentence.strip()
    if not stripped:
        return True
    if stripped.endswith("...") or stripped.endswith("…"):
        return True
    if stripped[-1] not in ".!?":
        return True
    last_word = stripped.rstrip(".!?\"'’”)]}").split()[-1].strip(".").lower()
    return len(last_word) <= 1 or last_word in _ABBREVIATIONS


@typed_cache
def count_sentences(text: str) -> int:
    """Count the sentences of the text.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of sentences in the text. Will be 0 for empty string, otherwise >= 1.

    """
    if len(text) == 0:
        return 0

    ignore_count = 0
    sentences = re.findall(r"\b[^.!?]+[.!?]*", text, re.UNICODE)
    for sentence in sentences:
        if count_words(sentence) <= 2 and _is_fragment(sentence):
            ignore_count += 1
    return max(1, len(sentences) - ignore_count)
