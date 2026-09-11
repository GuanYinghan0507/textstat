"""模块一用例 TC-A-018 ~ TC-A-019：long_word_count 长词统计。"""

from __future__ import annotations

import textstat

TP = "sixsix seven77"


def test_long_word_count_threshold_boundary() -> None:
    """TC-A-018：长词阈值边界（边界值）。

    预期依据：源码使用 len(word) > threshold 的严格大于判定，
    threshold=6 时 sixsix（6 个字母）不计入、seven77（7 个字母）计入，结果为 1；
    threshold=5 时两个词都超过阈值，结果为 2。
    """
    assert textstat.long_word_count(TP, threshold=6) == 1
    assert textstat.long_word_count(TP, threshold=5) == 2


def test_long_word_count_empty_and_short_words() -> None:
    """TC-A-019：空字符串与短词文本的长词数（边界值）。"""
    assert textstat.long_word_count("") == 0
    assert textstat.long_word_count("hi") == 0
