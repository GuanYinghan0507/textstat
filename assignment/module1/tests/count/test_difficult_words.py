"""模块一用例 TC-A-015 ~ TC-A-017、TC-A-024：difficult_words 困难词统计。"""

from __future__ import annotations

import textstat

TN = "Cool dogs wear da sunglasses."
TO = "The dog is in the park."
TM = "The interoperability of systems matters."
TZ = "intricate intricate intricate"


def test_difficult_words_easy_text() -> None:
    """TC-A-015：全为易词的文本困难词数为 0。"""
    assert textstat.difficult_words(TO) == 0


def test_difficult_words_unique_switch() -> None:
    """TC-A-016：同一个困难词出现 3 次时的 unique 开关。

    预期依据：unique=True 时重复词只计一次（1），unique=False 时按出现次数统计（3）。
    """
    assert textstat.difficult_words(TZ, syllable_threshold=2, unique=True) == 1
    assert textstat.difficult_words(TZ, syllable_threshold=2, unique=False) == 3


def test_difficult_words_with_out_of_vocabulary_word() -> None:
    """TC-A-017：常规文本与含未收录词文本的困难词数。

    难词判定依赖音节统计，未收录词触发 KeyError（缺陷 A1），修复前该用例部分通过。
    """
    assert textstat.difficult_words(TO) == 0
    assert textstat.difficult_words(TM) == 3


def test_difficult_words_syllable_threshold_boundary() -> None:
    """TC-A-024：音节阈值边界（边界值）。

    预期依据：同一文本在 syllable_threshold 为 1、2、3 时困难词数分别为 3、1、1，
    用于验证阈值判定使用的是不小于阈值的语义。
    """
    assert textstat.difficult_words(TN, syllable_threshold=1, unique=True) == 3
    assert textstat.difficult_words(TN, syllable_threshold=2, unique=True) == 1
    assert textstat.difficult_words(TN, syllable_threshold=3, unique=True) == 1
