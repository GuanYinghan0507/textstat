"""模块二用例 TC-M2-022：长文档统计完整性与幂等性（AI 生成，人工核对）。"""

from __future__ import annotations

import textstat

LONG_DOC = ("The quick brown fox jumps over the lazy dog. " * 60) + (
    "Although the committee had already reviewed the proposal — which, according to "
    "Dr. Smith, was substantially incomplete — they decided to postpone the vote."
)


def test_m2_022_long_document_completeness_and_idempotence() -> None:
    """TC-M2-022：长文档（562 词 / 61 句 / 700 音节）统计完整且可重复。

    预期依据：60 遍短句（60 句）+ 1 个长难句（1 句），共 61 句；
    修复前长难句中的 "Dr. Smith" 会把这一句切成两句，导致句数多计为 62（缺陷 M2-D5）。
    连续两次调用结果必须一致（幂等）。
    """
    assert textstat.lexicon_count(LONG_DOC) == 562
    assert textstat.sentence_count(LONG_DOC) == 61
    assert textstat.syllable_count(LONG_DOC) == 700
    assert textstat.lexicon_count(LONG_DOC) == textstat.lexicon_count(LONG_DOC)
    assert textstat.syllable_count(LONG_DOC) == textstat.syllable_count(LONG_DOC)
