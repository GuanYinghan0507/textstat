"""模块二用例 TC-M2-006 ~ TC-M2-010：多语言计数（AI 生成，人工核对）。

与模块一用例的区别：模块一只有英语为主加少量单句多语言，这里覆盖德语超长
复合词、法语撇号连字符、俄语非 ASCII 标点、匈牙利语长词，以及语言配置对
计数结果的影响。
"""

from __future__ import annotations

import textstat

DE_TEXT = (
    "Alle Parteien widmen dem Thema rein quantitativ betrachtet nennenswerte "
    "Aufmerksamkeit."
)


def teardown_module(module) -> None:
    """恢复默认语言，避免影响其他测试。"""
    textstat.set_lang("en_US")


def test_m2_006_german_compound_word() -> None:
    """TC-M2-006：德语超长复合词的音节数（pyphen 德语断词），预期 9。

    预期依据：de_DE 断词结果为 Le-bens-ver-si-che-rungs-ge-sell-schaft，共 9 个音节；
    若错误地使用英语断词（en_US）只会得到 4 个，说明语言配置必须生效。
    """
    textstat.set_lang("de_DE")
    assert textstat.syllable_count("Lebensversicherungsgesellschaft") == 9


def test_m2_007_french_apostrophe_and_hyphen() -> None:
    """TC-M2-007：法语撇号与连字符文本的词数，预期 5。"""
    textstat.set_lang("fr_FR")
    assert textstat.lexicon_count("L'école des enfants s'appelle Jean-Jacques.") == 5


def test_m2_008_russian_guillemets() -> None:
    """TC-M2-008：俄语书名号 «» 不影响断句，预期 2 句。"""
    textstat.set_lang("ru_RU")
    assert textstat.sentence_count("Игра «слова» была важной. Дети играли долго.") == 2


def test_m2_009_hungarian_long_word() -> None:
    """TC-M2-009：匈牙利语长词的音节数，预期 11。"""
    textstat.set_lang("hu_HU")
    assert textstat.syllable_count("Mondok neked egy nyelvtani fejtörőt.") == 11


def test_m2_010_language_config_changes_result() -> None:
    """TC-M2-010：同一文本在不同语言配置下的音节数应不同（26 / 19 / 24）。"""
    textstat.set_lang("de_DE")
    de_syllables = textstat.syllable_count(DE_TEXT)
    textstat.set_lang("en_US")
    en_syllables = textstat.syllable_count(DE_TEXT)
    textstat.set_lang("es_ES")
    es_syllables = textstat.syllable_count(DE_TEXT)
    assert (de_syllables, en_syllables, es_syllables) == (26, 19, 24)
