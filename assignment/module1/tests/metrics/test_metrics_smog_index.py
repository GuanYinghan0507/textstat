from __future__ import annotations

from metrics_helpers import run_case


def test_textstat_st_rm_002(record_property) -> None:
    run_case("TEXTSTAT-ST-RM-002", record_property)
