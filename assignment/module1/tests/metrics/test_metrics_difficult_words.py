from __future__ import annotations

from metrics_helpers import run_case


def test_textstat_st_rm_007(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-007", record_property)


def test_textstat_st_rm_019(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-019", record_property)
