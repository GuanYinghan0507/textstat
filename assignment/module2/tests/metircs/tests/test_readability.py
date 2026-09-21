"""One pytest test per TEXTSTAT-UT-001 through TEXTSTAT-UT-037 workbook case."""

from __future__ import annotations

import math
import os
import subprocess

import pytest


SIMPLE = "The cat sat on the mat."
MEDIUM = (
    "Reading develops vocabulary, strengthens concentration, and helps "
    "people communicate complex ideas clearly."
)
COMPLEX = (
    "Epistemological paradigms invariably necessitate hermeneutic scrutiny "
    "of phenomenological constructs through dialectical methodologies."
)
THREE_SIMPLE = "The cat sat. The dog ran. The sun rose."
POLY_ONE_SENTENCE = "Extraordinary circumstances complicate communication."
SPANISH = "Hoy es un lindo día."
ITALIAN = "Roma è un comune italiano, capitale della Repubblica Italiana."
ARABIC = "ذهب هند وأحمد الى المدرسة. هند تحب الرسم والمطالعة."
GERMAN = (
    "Alle meine Entchen schwimmen auf dem See. Köpfchen unters Wasser, "
    "Schwänzchen in die Höh."
)


def close(actual: float, expected: float, places: int = 3) -> None:
    """Check the workbook's explicitly stated decimal precision."""
    tolerance = 10 ** (-places) / 2
    assert math.isclose(actual, expected, abs_tol=tolerance, rel_tol=0), (
        f"expected {expected} to {places} decimal places, got {actual}"
    )


def test_ut_001_flesch_simple(ts):
    assert isinstance(ts.flesch_reading_ease(SIMPLE), float)
    close(ts.flesch_reading_ease(SIMPLE), 116.145)


def test_ut_002_flesch_easy_vs_complex(ts):
    easy = ts.flesch_reading_ease(SIMPLE)
    hard = ts.flesch_reading_ease(COMPLEX)
    assert easy > hard
    close(easy, 116.145)
    close(hard, -108.495)


def test_ut_003_flesch_punctuation_variant(ts):
    close(ts.flesch_reading_ease(SIMPLE), 116.145)
    close(ts.flesch_reading_ease("The cat, sat; on the mat!!!"), 116.145)


def test_ut_004_flesch_language_switch(ts):
    ts.set_lang("en_US")
    close(ts.flesch_reading_ease(SIMPLE), 116.145)
    ts.set_lang("de_DE")
    close(ts.flesch_reading_ease(SIMPLE), 115.500)
    ts.set_lang("en_US")
    close(ts.flesch_reading_ease(SIMPLE), 116.145)


def test_ut_005_flesch_kincaid_simple(ts):
    close(ts.flesch_kincaid_grade(SIMPLE), -1.450)


def test_ut_006_ari_medium(ts):
    close(ts.automated_readability_index(MEDIUM), 22.250)


def test_ut_007_coleman_liau_medium(ts):
    close(ts.coleman_liau_index(MEDIUM), 26.683)


def test_ut_008_gunning_fog_medium(ts):
    close(ts.gunning_fog(MEDIUM), 21.467)


def test_ut_009_dale_chall_medium(ts):
    close(ts.dale_chall_readability_score(MEDIUM), 16.074)


def test_ut_010_spache_simple_float(ts):
    value = ts.spache_readability(SIMPLE, float_output=True)
    assert isinstance(value, float)
    close(value, 1.685)


def test_ut_011_mcalpine_simple(ts):
    close(ts.mcalpine_eflaw(SIMPLE), 12.0)


def test_ut_012_smog_three_sentences(ts):
    close(ts.smog_index(THREE_SIMPLE), 3.1291, places=4)


@pytest.mark.defect_probe
def test_ut_013_smog_under_three_sentences(ts):
    # Workbook permits either a clear rejection or 0.0 for invalid sample size.
    try:
        result = ts.smog_index(POLY_ONE_SENTENCE)
    except ValueError:
        return
    assert result == 0.0, f"SMOG should reject <3 sentences; got {result}"


def test_ut_014_linsear_simple(ts):
    close(ts.linsear_write_formula(SIMPLE), 2.0)


def test_ut_015_linsear_strict_lower(ts):
    close(ts.linsear_write_formula("The cat sat.", strict_lower=True), 0.0)


def test_ut_016_linsear_first_100_words(ts):
    text100 = ("dog " * 100) + "."
    text101 = ("dog " * 100) + "extraordinary."
    close(ts.linsear_write_formula(text100), 50.0)
    close(ts.linsear_write_formula(text101), 50.0)


def test_ut_017_linsear_disable_upper_limit(ts):
    text101 = ("dog " * 100) + "extraordinary."
    close(ts.linsear_write_formula(text101, strict_upper=False), 51.5)
    assert ts.linsear_write_formula(text101, strict_upper=False) != ts.linsear_write_formula(text101)


def test_ut_018_text_standard_float(ts):
    value = ts.text_standard(SIMPLE, float_output=True)
    assert isinstance(value, float)
    close(value, 2.0)


def test_ut_019_text_standard_string(ts):
    value = ts.text_standard(SIMPLE, float_output=False)
    assert isinstance(value, str)
    assert value == "1st and 2nd grade"


def test_ut_020_text_standard_empty_077_baseline(ts):
    # 0.7.7 has no lower-bound clamping; this is a version-specific baseline.
    close(ts.text_standard("", float_output=True), 0.0)


def test_ut_021_text_standard_complex_077_baseline(ts):
    # 0.7.7 has no upper-bound clamping; do not assert the later 18.0 behavior.
    close(ts.text_standard(COMPLEX, float_output=True), 31.0)


def test_ut_022_reading_time_default(ts):
    close(ts.reading_time(SIMPLE), 0.26442, places=5)


def test_ut_023_reading_time_custom(ts):
    close(ts.reading_time("abcd ef", ms_per_char=20), 0.12, places=5)


def test_ut_024_reading_time_zero_speed(ts):
    close(ts.reading_time("abcd ef", ms_per_char=0), 0.0, places=5)


@pytest.mark.defect_probe
def test_ut_025_reading_time_negative_speed(ts):
    with pytest.raises((ValueError, TypeError), match=r"(?i)(negative|non.?negative|ms_per_char|speed|time)"):
        ts.reading_time("abcd ef", ms_per_char=-1)


def test_ut_026_empty_string_zero_metrics(ts):
    metrics = [
        ts.flesch_reading_ease,
        ts.flesch_kincaid_grade,
        ts.smog_index,
        ts.coleman_liau_index,
        ts.automated_readability_index,
        ts.dale_chall_readability_score,
        ts.linsear_write_formula,
        ts.gunning_fog,
    ]
    for metric in metrics:
        assert metric("") == 0.0, f"{metric.__name__} was nonzero on empty text"


@pytest.mark.defect_probe
def test_ut_027_whitespace_only_zero_metrics(ts):
    text = "   \n\t  "
    metrics = [
        ts.flesch_reading_ease,
        ts.flesch_kincaid_grade,
        ts.smog_index,
        ts.coleman_liau_index,
        ts.automated_readability_index,
        ts.dale_chall_readability_score,
        ts.linsear_write_formula,
        ts.gunning_fog,
    ]
    for metric in metrics:
        assert metric(text) == 0.0, f"{metric.__name__} was nonzero on whitespace-only text"


def test_ut_028_none_input_type_error(ts):
    with pytest.raises(TypeError):
        ts.flesch_reading_ease(None)


def test_ut_029_integer_input_type_error(ts):
    with pytest.raises(TypeError):
        ts.flesch_reading_ease(123)


@pytest.mark.defect_probe
def test_ut_030_invalid_language_clear_error(ts):
    ts.set_lang("xx_XX")
    try:
        with pytest.raises((ValueError, KeyError)) as caught:
            ts.flesch_reading_ease("The cat sat.")
        message = str(caught.value)
        assert message and ("xx" in message.lower() or "lang" in message.lower()), (
            f"error must identify unsupported language, got {message!r}"
        )
    finally:
        ts.set_lang("en_US")


def test_ut_031_spanish_formulas(ts):
    ts.set_lang("es_ES")
    close(ts.fernandez_huerta(SPANISH), 129.740)
    close(ts.szigriszt_pazos(SPANISH), 127.080)
    close(ts.gutierrez_polini(SPANISH), 64.350)
    close(ts.crawford(SPANISH), -1.627)
    ts.set_lang("en_US")


def test_ut_032_italian_gulpease(ts):
    ts.set_lang("it_IT")
    close(ts.gulpease_index(ITALIAN), 62.333)
    ts.set_lang("en_US")


def test_ut_033_arabic_osman(ts):
    ts.set_lang("ar")
    close(ts.osman(ARABIC), 102.186)
    ts.set_lang("en_US")


def test_ut_034_german_wiener_variant_one(ts):
    ts.set_lang("de_DE")
    close(ts.wiener_sachtextformel(GERMAN, 1), 2.600)
    ts.set_lang("en_US")


def test_ut_035_repeat_calls_deterministic(ts):
    values = [ts.flesch_reading_ease(MEDIUM) for _ in range(100)]
    assert all(value == values[0] for value in values)
    assert isinstance(values[0], float)


def test_ut_036_long_text_finite(ts):
    text = "The cat sat on the mat. " * 10000
    values = [
        ts.flesch_reading_ease(text),
        ts.flesch_kincaid_grade(text),
        ts.text_standard(text, float_output=True),
    ]
    assert all(math.isfinite(value) for value in values)
    close(values[2], -4.0)


@pytest.mark.compatibility
@pytest.mark.defect_probe
def test_ut_037_cmudict_113_compatibility():
    compat_python = os.environ.get("TEXTSTAT077_COMPAT_PYTHON")
    assert compat_python, "Run python run_tests.py to prepare the separate cmudict 1.1.3 environment"
    program = (
        "import importlib.metadata as m, math; "
        "from textstat import textstat; "
        "assert m.version('textstat') == '0.7.7'; "
        "assert m.version('cmudict') == '1.1.3'; "
        f"value = textstat.flesch_reading_ease({COMPLEX!r}); "
        "assert math.isfinite(value)"
    )
    completed = subprocess.run(
        [compat_python, "-c", program], capture_output=True, text=True, check=False
    )
    assert completed.returncode == 0, (
        "0.7.7 readability calculation failed with cmudict 1.1.3:\n"
        + completed.stderr
    )
