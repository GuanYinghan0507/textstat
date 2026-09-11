"""模块一用例 TC-A-012 ~ TC-A-014：syllable_count 音节计数。"""

from __future__ import annotations

import textstat

TA = "The quick brown fox jumps over the lazy dog."
TL = "In 2024 we win."
TM = "The interoperability of systems matters."


def test_syllable_count_normal_text() -> None:
    """TC-A-012：常规文本与空字符串的音节数。

    预期依据：逐词查 cmudict 音素，TA 为 11 个音节；空字符串为 0。
    """
    assert textstat.syllable_count(TA) == 11
    assert textstat.syllable_count("") == 0


def test_syllable_count_with_number_word() -> None:
    """TC-A-013：含数字词文本的音节数。

    缺陷 A1：数字词 2024 不在 cmudict 中，count_syllables 未捕获 KeyError，
    未回退到 pyphen，直接抛出异常（见附录2 缺陷报告）。
    """
    assert textstat.syllable_count(TL) == 4


def test_syllable_count_with_out_of_vocabulary_word() -> None:
    """TC-A-014：常规文本与含未收录词文本的音节数。

    同一用例内一部分断言通过（常规文本）、一部分失败（未收录词抛 KeyError），
    修复前为部分通过（POK），用于定位缺陷 A1 的影响范围。
    """
    assert textstat.syllable_count(TA) == 11
    assert textstat.syllable_count(TM) == 13
