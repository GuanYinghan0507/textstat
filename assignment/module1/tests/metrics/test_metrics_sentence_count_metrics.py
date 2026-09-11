from __future__ import annotations

from metrics_helpers import run_case


def test_textstat_st_rm_015(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-015", record_property)


def test_textstat_st_rm_020(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-020", record_property)
