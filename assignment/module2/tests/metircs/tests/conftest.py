from __future__ import annotations

import importlib.metadata

import pytest
from textstat import textstat


@pytest.fixture(scope="session", autouse=True)
def verify_pinned_environment():
    assert importlib.metadata.version("textstat") == "0.7.7"
    assert importlib.metadata.version("cmudict") == "1.0.32"


@pytest.fixture
def ts():
    """Independent textstat state for each test; no language-state leakage."""
    instance = type(textstat)()
    instance.set_lang("en_US")
    return instance
