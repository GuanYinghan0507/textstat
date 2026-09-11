from __future__ import annotations

import json
from pathlib import Path

import pytest

import textstat


DATA_FILE = Path(__file__).resolve().parents[1] / "metrics_test_data.json"
CASE_MAP = {
    case["case_id"]: case
    for case in json.loads(DATA_FILE.read_text(encoding="utf-8"))["cases"]
}


def run_case(case_id: str, record_property) -> None:
    """Execute one Appendix 1 case and record its appendix status."""

    case = CASE_MAP[case_id]
    record_property("appendix-status", case["status"])

    if case["status"] == "NT":
        pytest.skip("NT: 当前被测版本未提供中文可读性指标基准，无法执行有效验证。")

    textstat.set_lang(case["lang"])
    result = getattr(textstat, case["function"])(case["input"])
    expected = case["expected"]

    if isinstance(expected, float):
        assert result == pytest.approx(expected, abs=1e-3), (
            f"{case_id}: {case['function']} returned {result!r}, expected {expected!r}"
        )
    else:
        assert result == expected, (
            f"{case_id}: {case['function']} returned {result!r}, expected {expected!r}"
        )
