"""模块二用例 TC-M2-001 ~ TC-M2-005：长难句与复杂标点（AI 生成，人工核对）。

与模块一用例的区别：模块一使用单句与简单标点，这里使用 37 词嵌套从句、
破折号/分号/括号/引号混排的长难句，验证复杂标点不会被误判为句末。
"""

from __future__ import annotations

import textstat

LONG_EN = (
    "Although the committee had already reviewed the proposal — which, according to "
    'Dr. Smith (the lead author, e.g. the principal investigator), was "substantially '
    "incomplete\" — they decided to postpone the vote; consequently, the project timeline "
    "slipped by three weeks."
)


def test_m2_001_nested_clause_single_sentence() -> None:
    """TC-M2-001：嵌套从句 + 破折号 + 分号的长难句仍应算 1 句。

    预期依据：整句只有一个句末句号；破折号与分号不是句末标点。
    """
    assert textstat.sentence_count(LONG_EN) == 1


def test_m2_002_quoted_period() -> None:
    """TC-M2-002：引号内的句号应正常断句，预期 2 句。"""
    assert textstat.sentence_count('He said "It is fine." Then he left.') == 2


def test_m2_003_parentheses_and_dash() -> None:
    """TC-M2-003：括号与破折号嵌套的句子仍算 1 句。"""
    assert (
        textstat.sentence_count(
            "The results (which were surprising — at least to us) were published."
        )
        == 1
    )


def test_m2_004_abbreviation_heavy_sentence() -> None:
    """TC-M2-004：缩写密集的单句（Dr./e.g./i.e. + 括号）仍应算 1 句。

    缺陷 M2-D5：句中缩写与括号不应产生句末边界，当前实现返回 3。
    """
    assert (
        textstat.sentence_count(
            "Dr. Smith (e.g. the lead author, i.e. the principal investigator) approved it."
        )
        == 1
    )


def test_m2_005_long_sentence_token_integrity() -> None:
    """TC-M2-005：长难句的词数与音节数应完整计入（37 词 / 67 音节）。"""
    assert textstat.lexicon_count(LONG_EN) == 37
    assert textstat.syllable_count(LONG_EN) == 67
