from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache


@typed_cache
def count_chars(text: str, ignore_spaces: bool) -> int:
    """Count the number of characters in a text.

    Parameters
    ----------
    text : str
        A text string.
    ignore_spaces : bool, optional
        Ignore whitespaces if True. The default is True.

    Returns
    -------
    int
        Number of characters.

    """
    # 零宽连接符（ZWJ/ZWNJ）、变体选择符等不可见控制字符不应计入字符数
    text = re.sub(r"[\u200b-\u200f\ufe0e\ufe0f\U000e0100-\U000e01ef]", "", text)
    if ignore_spaces:
        text = re.sub(r"\s", "", text)
    return len(text)
