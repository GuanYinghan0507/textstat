"""模块一用例 TC-A-009 ~ TC-A-011：sentence_count 句子计数。"""

from __future__ import annotations

import textstat

TK = (
    "The sun rises in the east. Birds fly south in winter. "
    "Children play outside after school."
)


def test_sentence_count_normal_text() -> None:
    """TC-A-009：多句英文文本的句子数为 3。"""
    assert textstat.sentence_count(TK) == 3


def test_sentence_count_empty_and_unterminated_text() -> None:
    """TC-A-010：空字符串与无句末标点文本（边界值）。

    预期依据：空字符串为 0；无终止标点的 "Hello world" 仍算 1 句。
    """
    assert textstat.sentence_count("") == 0
    assert textstat.sentence_count("Hello world") == 1


def test_sentence_count_short_sentences() -> None:
    """TC-A-011：短句文本的句子数。

    缺陷 A3：count_sentences 会忽略单词数不大于 2 的句子，
    "Hello. World." 应返回 2、"One. Two. Three. Four. Five." 应返回 5，
    修复前两者都返回 1（见附录2 缺陷报告）。
    """
    assert textstat.sentence_count("Hello. World.") == 2
    assert textstat.sentence_count("One. Two. Three. Four. Five.") == 5
