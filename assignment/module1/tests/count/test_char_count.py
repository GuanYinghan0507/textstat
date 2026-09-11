"""模块一用例 TC-A-001 ~ TC-A-002：char_count 字符计数。"""

from __future__ import annotations

import textstat

TA = "The quick brown fox jumps over the lazy dog."


def test_char_count_normal_text() -> None:
    """TC-A-001：正常英文句子的字符数。

    预期依据：TA 含 35 个字母、1 个句点与 8 个空格，
    忽略空格为 36，统计空格为 44（同一用例覆盖两个参数分支）。
    """
    assert textstat.char_count(TA) == 36
    assert textstat.char_count(TA, ignore_spaces=False) == 44


def test_char_count_empty_and_blank_text() -> None:
    """TC-A-002：空字符串与纯空白文本的字符数（边界值）。

    预期依据：空字符串为 0；纯空白在忽略空格时为 0、统计空格时为 3。
    """
    assert textstat.char_count("") == 0
    assert textstat.char_count("   ") == 0
    assert textstat.char_count("   ", ignore_spaces=False) == 3
