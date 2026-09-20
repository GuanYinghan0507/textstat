"""模块二用例 TC-M2-018 ~ TC-M2-021：不变量与性质测试（AI 生成，人工核对）。

与模块一用例的区别：模块一是“给定输入查期望值”，这里验证跨输入的数学性质
（追加句末标点、换行、大小写、参数差值），用于发现人工很难想到的口径错误。
"""

from __future__ import annotations

import textstat

BASE = "The quick brown fox jumps over the lazy dog"


def test_m2_018_adding_period_keeps_word_count() -> None:
    """TC-M2-018：追加句号不改变词数（性质测试）。"""
    assert textstat.lexicon_count(BASE) == textstat.lexicon_count(BASE + ".") == 9


def test_m2_019_line_break_keeps_word_count() -> None:
    """TC-M2-019：文本拆成两段（换行）后词数不变（性质测试），预期 9。"""
    assert textstat.lexicon_count("The quick brown fox.\n\nJumps over the lazy dog.") == 9


def test_m2_020_case_insensitive_counts() -> None:
    """TC-M2-020：大小写不改变字母数与音节数（性质测试）。"""
    assert textstat.letter_count("Hello World") == textstat.letter_count("hello world") == 10
    assert textstat.syllable_count("Hello World") == textstat.syllable_count("hello world") == 3


def test_m2_021_char_count_parameter_semantics() -> None:
    """TC-M2-021：含空格与不含空格的差值等于空白字符数（性质测试）。"""
    assert textstat.char_count("   a   b   ") == 2
    assert textstat.char_count("   a   b   ", ignore_spaces=False) == 11
    assert (
        textstat.char_count("   a   b   ", ignore_spaces=False)
        - textstat.char_count("   a   b   ")
        == 9
    )
