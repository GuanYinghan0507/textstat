from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ..transformations._remove_punctuation import remove_punctuation


@typed_cache
def count_letters(text: str) -> int:
    """Count letters in a text. Spaces are ignored.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        The number of letters in text.

    """
    # 只统计拉丁字母：剔除空格、标点、数字、下划线，以及汉字等非拉丁字符
    # （\w 会保留数字、下划线与 CJK 字符，因此不能用 [^\w\s] 判字母）
    return len(re.sub(r"[^A-Za-z\u00C0-\u024F\u1E00-\u1EFF]", "", text))
