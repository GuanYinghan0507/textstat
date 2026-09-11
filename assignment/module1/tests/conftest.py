"""模块一（计数与预处理）测试的公共配置。

无论从仓库根目录还是从其他目录运行 pytest，都能正确导入被测对象 textstat。
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
