from __future__ import annotations

from metrics_helpers import run_case


def test_textstat_st_rm_010(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-010", record_property)
