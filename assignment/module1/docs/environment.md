# 测试环境说明

## 硬件与操作系统

- 操作系统：Windows
- 终端：PowerShell
- 日期：2026-09-10

## Python 环境

- Python：3.11.4
- 虚拟环境目录：`.venv`
- 虚拟环境创建命令：`python -m venv .venv`

## 被测对象

- 项目：textstat
- 作业分支：`assignment`
- Git tag：`0.7.7`

## 依赖与测试框架

| 组件 | 版本 |
| --- | --- |
| pytest | 9.1.1 |
| pluggy | 1.6.0 |
| pytest-cov | 7.1.0 |
| pyphen | 已安装 |
| cmudict | 已安装 |

安装命令：

```bash
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pip install -r assignment\requirements.txt
```

## 环境验证命令与输出

```bash
.venv\Scripts\python -c "import textstat, pyphen, cmudict, pytest; print('env ok')"
```

输出：

```text
env ok
```

```bash
.venv\Scripts\python -c "import textstat; print('textstat version:', getattr(textstat, '__version__', 'unknown'))"
```

输出：

```text
textstat version: (0, 7, 6)
```

```bash
.venv\Scripts\python -m pytest -v
```

输出：

```text
collected 0 items
no tests ran
```

当前测试目录还没有用例，因此 pytest 收集结果为 0 条。

## 测试运行方式

在仓库根目录执行：

```bash
.venv\Scripts\python -m pytest -v
```
