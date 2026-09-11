"""模块一用例 TC-A-006 ~ TC-A-008：lexicon_count 词数统计。"""

from __future__ import annotations

import textstat

TD = "They're here, and they're there."


def test_lexicon_count_normal_text() -> None:
    """TC-A-006：正常英文句子的词数（默认参数）。

    预期依据：They're / here / and / they're / there，收缩词按一个词计，共 5。
    """
    assert textstat.lexicon_count(TD) == 5


def test_lexicon_count_split_contractions() -> None:
    """TC-A-007：split_contractions=True 时收缩词拆开统计，共 7。"""
    assert textstat.lexicon_count(TD, split_contractions=True) == 7


def test_lexicon_count_punctuation_handling() -> None:
    """TC-A-008：纯标点文本与保留标点分支（边界值）。

    预期依据：removepunct 默认 True 时纯标点不产生单词（0）；
    removepunct=False 时 "hello ... world" 中的省略号被当作一个词（3）。
    """
    assert textstat.lexicon_count("!!!") == 0
    assert textstat.lexicon_count("hello ... world", removepunct=False) == 3
