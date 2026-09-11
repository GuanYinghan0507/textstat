"""模块一用例 TC-A-003 ~ TC-A-005：letter_count 字母计数。"""

from __future__ import annotations

import textstat

TD = "They're here, and they're there."


def test_letter_count_normal_text() -> None:
    """TC-A-003：正常英文句子的字母数。

    预期依据：去标点与空格后 They're 6 + here 4 + and 3 + they're 6 + there 5 = 24。
    """
    assert textstat.letter_count(TD) == 24


def test_letter_count_empty_string() -> None:
    """TC-A-004：空字符串的字母数为 0（边界值）。"""
    assert textstat.letter_count("") == 0


def test_letter_count_non_letter_characters() -> None:
    """TC-A-005：数字与下划线混排文本的字母数。

    缺陷 A2："3 apples" 中数字 3 不是字母，应只统计 apples 的 6 个字母；
    hello_world 中的下划线也不是字母，应统计为 5 + 5 = 10。
    修复前实际返回 7 与 11（见附录2 缺陷报告）。
    """
    assert textstat.letter_count("3 apples") == 6
    assert textstat.letter_count("hello_world") == 10
