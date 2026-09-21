# textstat 0.7.7 可读性指标自动化测试

本工程对应《模块二方案2_AI测_textstat0.7.7可读性指标_测试用例清单.xlsx》中的 `TEXTSTAT-UT-001` 至 `TEXTSTAT-UT-037`，每个编号对应 `tests/test_readability.py` 中的一个 `pytest` 测试。测试对象固定为 [textstat 0.7.7](https://github.com/textstat/textstat/releases/tag/0.7.7) 的公开可读性指标接口。

## 一键运行

需要 Python 3.10 或更新版本，以及首次安装依赖时的网络连接。在工程目录执行：

```bash
python run_tests.py
```

Windows 也可双击 `run_tests.bat`（需要安装 Python Launcher，即 `py` 命令）。入口脚本会自动创建两个隔离虚拟环境、安装固定依赖并运行全部 37 条用例。首次运行需要下载依赖，之后会复用虚拟环境。运行结束会生成 `results/junit.xml`，可供 CI 或测试报告读取。退出码 `0` 表示全部通过，`1` 表示存在失败用例，`2` 表示安装或环境错误。

常规环境固定 `textstat==0.7.7` 和 `cmudict==1.0.32`。`UT-037` 使用第二个环境，专门验证 `cmudict==1.1.3` 与 textstat 0.7.7 的兼容性；它不会污染其他用例。请使用 PyPI 分发版本核对版本号：`importlib.metadata.version("textstat")`。0.7.7 包内的 `textstat.__version__` 元组仍显示 `(0, 7, 6)`，不宜用它判断安装版本。

## 文件说明

- `run_tests.py`：一键建环境、安装依赖、执行测试。
- `run_tests.bat`：Windows 双击入口。
- `requirements-main.txt`：常规测试依赖。
- `requirements-compat.txt`：兼容性隔离环境依赖。
- `tests/conftest.py`：版本守卫和每例独立的 `textstat` 实例。
- `tests/test_readability.py`：37 条测试，函数名与 Excel 用例编号一一对应。

## 如何解读失败

标有 `defect_probe` 的用例是按合理预期设计的缺陷探测，不使用 `xfail`、跳过或放宽断言。0.7.7 原始版本上，SMOG 不足 3 句、纯空白文本、负阅读耗时参数、非法语言报错信息及新版 `cmudict` 兼容性等测试可能失败。这些失败是待分析的缺陷线索，不应直接等同于已确认的缺陷；提交缺陷清单前需记录实际输出、复现步骤与修复验证。其他数值用例的预期以 0.7.7 与锁定依赖的实测结果为基线，尤其不要沿用后续版本 `text_standard` 的 1～18 年级钳制结果。

本工程首次验证（2026-09-21，Python 3.12）执行了全部 37 条：32 条通过、5 条失败。失败编号为 `UT-013`、`UT-025`、`UT-027`、`UT-030`、`UT-037`；具体堆栈以本机重新运行生成的 `results/junit.xml` 为准。

单独重跑某例：

```bash
.venv-main/Scripts/python -m pytest -q tests/test_readability.py -k ut_013
```

上例是 Windows 路径；Linux/macOS 使用 `.venv-main/bin/python`。单独运行 `UT-037` 时需先运行一次 `python run_tests.py`，并设置环境变量 `TEXTSTAT077_COMPAT_PYTHON` 指向 `.venv-compat` 内的 Python 解释器。常规提交与演示建议直接运行统一入口。

## AI 辅助与版本管理

测试数据、断言和用例映射由 AI 辅助生成，再以固定版本源码和实际执行结果核对。建议将本工程、用例清单、执行日志及关键 AI 对话记录放入小组 Git 仓库；各成员使用自己的账号提交真实工作。`.gitignore` 已排除虚拟环境与本地测试结果。
