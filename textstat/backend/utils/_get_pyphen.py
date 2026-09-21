from __future__ import annotations

from pyphen import Pyphen, language_fallback  # type: ignore

from ._typed_cache import typed_cache


@typed_cache
def get_pyphen(lang: str) -> Pyphen:
    """Get a pyphen object for the given language.

    Parameters
    ----------
    lang : str
        The language of the text.

    Returns
    -------
    Pyphen
        A Pyphen object for the given language.
    """
    if language_fallback(lang) is None:
        raise ValueError(f"Unsupported language: {lang}")
    return Pyphen(lang=lang)
