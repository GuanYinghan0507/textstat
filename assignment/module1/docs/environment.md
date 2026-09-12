# 测试环境说明

## 硬件与操作系统

- 操作系统：Windows
- 终端：PowerShell
- 文档更新日期：2026-09-12

## Python 环境

- Python：3.11.4
- 虚拟环境目录：`.venv`
- 虚拟环境创建命令：`python -m venv .venv`

## 被测对象

- 项目：textstat
- 作业分支：`assignment`
- 基线版本：textstat 0.7.7（Git tag 0.7.7）
- 说明：源码中的 `__version__` 或包元数据可能保留上游内部版本号，本作业版本以 Git tag 0.7.7 和仓库提交历史为准。

## 依赖与测试框架

| 组件 | 版本 |
| --- | --- |
| pytest | 9.1.1 |
| pluggy | 1.6.0 |
| pytest-cov | 7.1.0 |
| pyphen | 已安装 |
| cmudict | 已安装 |

## 安装命令

```powershell
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pip install -r assignment\requirements.txt
```

## 环境验证

```powershell
.venv\Scripts\python -c "import textstat, pyphen, cmudict, pytest; print('env ok')"
```

输出：

```text
env ok
```

## 测试运行方式

在仓库根目录执行：

```powershell
.venv\Scripts\python -m pytest -v
```

该命令会同时收集 `assignment/module1/tests/count/` 和 `assignment/module1/tests/metrics/` 下的全部测试。

## 当前测试结果统计

最终合并测试用例清单见 `assignment/module1/test_cases/test_cases.xlsx`，共 44 条：

- 管映涵：24 条（`TC-A-001` 至 `TC-A-024`）
- 韩迎小：20 条（`TEXTSTAT-ST-RM-001` 至 `TEXTSTAT-ST-RM-020`）

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| OK | 31 | 实际结果符合预期 |
| POK | 5 | 部分通过，需结合备注和测试报告说明 |
| NG | 7 | 已知缺陷复现用例；在当前原始版本上会显示为失败，属于预期结果 |
| NT | 1 | 当前版本未提供可执行基准，运行时会跳过 |

全量运行 `pytest` 时可能出现失败项并返回非零退出码，原因是 NG 用例未被标记为 `xfail`；这是缺陷验证结果，不应被误判为测试环境故障。
