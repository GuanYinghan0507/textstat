"""模块二用例 TC-M2-015 ~ TC-M2-017：标点组合与数字单位（AI 生成，人工核对）。

与模块一用例的区别：模块一只用半角标点，这里引入全角句末标点与省略号组合，
并验证数字、单位、版本号不会被误当作分隔符。
"""

from __future__ import annotations

import textstat


def test_m2_015_full_width_sentence_endings() -> None:
    """TC-M2-015：全角句末标点（！？。）应被识别为句子边界，预期 2 句。

    缺陷 M2-D2：当前实现只识别半角 .!?，返回 1。
    """
    assert textstat.sentence_count("Hello！How are you？") == 2


def test_m2_016_ellipsis_convention() -> None:
    """TC-M2-016：省略号 + 问叹号混排的断句行为（记录约定，预期 2 句）。

    当前实现把以省略号结尾的片段视为停顿不计句，"What?!" 与 "Really." 各计一句。
    """
    assert textstat.sentence_count("Wait... What?! Really.") == 2


def test_m2_017_numbers_units_version() -> None:
    """TC-M2-017：数字、单位与版本号混排时的词数，预期 5。"""
    assert textstat.lexicon_count("1,000 USD, 3.5 kg, v1.2.3") == 5
