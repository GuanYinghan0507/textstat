"""模块二（AI 测 · 计数与预处理）测试的公共配置。

把仓库根目录加入 sys.path，保证从任意目录运行 pytest 都能导入被测对象 textstat。
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
