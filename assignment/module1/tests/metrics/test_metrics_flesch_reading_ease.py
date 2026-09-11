from __future__ import annotations

from metrics_helpers import run_case


def test_textstat_st_rm_001(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-001", record_property)


def test_textstat_st_rm_011(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-011", record_property)
