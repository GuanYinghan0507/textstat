"""模块一用例 TC-A-022 ~ TC-A-023：polysyllabcount 多音节词统计。"""

from __future__ import annotations

import textstat

TA = "The quick brown fox jumps over the lazy dog."
TM = "The interoperability of systems matters."


def test_polysyllabcount_three_syllable_word() -> None:
    """TC-A-022：三音节词与常规文本的多音节词数。

    预期依据：banana 为三音节词，达到三音节及以上计入标准（1）；
    TA 中没有三音节及以上的词（0）。
    """
    assert textstat.polysyllabcount("banana") == 1
    assert textstat.polysyllabcount(TA) == 0


def test_polysyllabcount_with_out_of_vocabulary_word() -> None:
    """TC-A-023：常规文本与含未收录词文本的多音节词数。

    未收录词 interoperability 的音节统计触发 KeyError（缺陷 A1），
    修复前该用例部分通过，修复后返回 1。
    """
    assert textstat.polysyllabcount(TA) == 0
    assert textstat.polysyllabcount(TM) == 1
