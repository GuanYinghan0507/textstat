import pytest

import textstat


@pytest.fixture(autouse=True)
def reset_language():
    textstat.set_lang("en_US")
    yield
    textstat.set_lang("en_US")
