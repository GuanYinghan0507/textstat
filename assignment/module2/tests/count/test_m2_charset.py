"""模块二用例 TC-M2-011 ~ TC-M2-014：字符集与特殊字符（AI 生成，人工核对）。

与模块一用例的区别：模块一只覆盖数字与下划线，这里覆盖 CJK 汉字与 emoji
（含 ZWJ 组合序列），验证“字母”的定义与字符计数口径。
"""

from __future__ import annotations

import textstat


def test_m2_011_cjk_not_counted_as_letters() -> None:
    """TC-M2-011：中英混排文本只应统计英文字母，预期 3。

    缺陷 M2-D1：汉字被计入字母数，当前实现返回 7（4 个汉字 + abc）。
    """
    assert textstat.letter_count("今天天气abc") == 3


def test_m2_012_emoji_zwj_sequence() -> None:
    """TC-M2-012：emoji 组合序列中的零宽连接符不应计入字符数，预期 3。

    预期依据：该序列由 3 个 emoji 通过零宽连接符（ZWJ，U+200D）拼接，
    ZWJ 是不可见控制字符，不应算作字符；修复前按码点计数返回 5。
    """
    assert textstat.char_count("👨‍👩‍👧") == 3


def test_m2_013_cjk_char_count_is_correct() -> None:
    """TC-M2-013：中文文本按字符数统计是正确的（用于对照 TC-M2-011），预期 15。"""
    assert textstat.char_count("今天天气很好，我们去公园散步。") == 15


def test_m2_014_emoji_does_not_pollute_counts() -> None:
    """TC-M2-014：emoji 不应被计入字母数与词数（字母 9、词 2）。"""
    assert textstat.letter_count("emoji 😀 text") == 9
    assert textstat.lexicon_count("emoji 😀 text") == 2
