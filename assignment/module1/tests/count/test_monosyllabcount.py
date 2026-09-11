"""模块一用例 TC-A-020 ~ TC-A-021：monosyllabcount 单音节词统计。"""

from __future__ import annotations

import textstat

TA = "The quick brown fox jumps over the lazy dog."
TL = "In 2024 we win."


def test_monosyllabcount_normal_text() -> None:
    """TC-A-020：正常英文句子的单音节词数为 7。

    预期依据：The / quick / brown / fox / jumps / the / dog 为单音节词，
    over 与 lazy 为双音节词。
    """
    assert textstat.monosyllabcount(TA) == 7


def test_monosyllabcount_with_number_word() -> None:
    """TC-A-021：含数字词文本的单音节词数。

    缺陷 A1：数字词 2024 不在 cmudict 中，逐词音节统计时抛出 KeyError，
    修复前为异常，修复后返回 4。
    """
    assert textstat.monosyllabcount(TL) == 4
