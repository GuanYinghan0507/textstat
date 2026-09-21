from __future__ import annotations

from pyphen import Pyphen  # type: ignore
import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "lang",
    [
        "en_US",
        "en",
        "es_ES",
        "es",
        "de_DE",
        "de",
        "fr_FR",
    ],
)
def test_get_pyphen(lang: str) -> None:
    assert isinstance(utils.get_pyphen(lang), Pyphen)


def test_get_pyphen_reports_unsupported_language() -> None:
    with pytest.raises(ValueError, match="xx_XX"):
        utils.get_pyphen("xx_XX")
