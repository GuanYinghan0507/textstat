# 模块二（AI 测）测试脚本 · 计数与预处理部分

本目录存放模块二由 AI 生成、并经人工核对的 pytest 脚本，覆盖计数与预处理模块，
用例编号与 `assignment/module2/test_cases/count_ai_test_cases.xlsx` 中的
TC-M2-001 ~ TC-M2-022 一一对应。

## 运行方式

在仓库根目录执行：

```powershell
# 只跑模块二的计数部分（22 条）
.venv\Scripts\python -m pytest assignment/module2/tests/count -v

# 全量运行（模块一 + 模块二）
.venv\Scripts\python -m pytest -v
```

## 脚本与用例对照

| 脚本 | 用例编号 | 主题 |
| --- | --- | --- |
| `count/test_m2_long_sentences.py` | TC-M2-001 ~ 005 | 长难句与复杂标点（嵌套从句、破折号、引号、括号、缩写密集） |
| `count/test_m2_multilingual_counts.py` | TC-M2-006 ~ 010 | 多语言计数（德语复合词、法语撇号、俄语书名号、匈牙利语、语言配置差异） |
| `count/test_m2_charset.py` | TC-M2-011 ~ 014 | 字符集（CJK 汉字、emoji ZWJ 序列、emoji 不污染计数） |
| `count/test_m2_punctuation.py` | TC-M2-015 ~ 017 | 全角标点、省略号约定、数字与单位 |
| `count/test_m2_invariants.py` | TC-M2-018 ~ 021 | 性质测试（追加句号、换行、大小写、参数差值） |
| `count/test_m2_long_document.py` | TC-M2-022 | 长文档完整性与幂等性 |

## 执行结果

首轮执行（修复前）：

```text
16 passed, 6 failed
```

修复后执行（当前状态）：

```text
19 passed, 3 failed
```

首轮失败的 6 条对应 4 类新缺陷，其中 3 类已修复，1 类经影响评估暂缓合入：

| 缺陷 | 用例 | 现象 |
| --- | --- | --- |
| M2-D1 | TC-M2-011 | `letter_count("今天天气abc")` 返回 7（应 3），汉字被计入字母数 |
| M2-D2 | TC-M2-015 | `sentence_count("Hello！How are you？")` 返回 1（应 2），不识别全角句末标点 |
| M2-D3 | TC-M2-012 | `char_count("👨‍👩‍👧")` 返回 5（应 3），零宽连接符被计入字符数 |
| M2-D5 | TC-M2-001、TC-M2-004、TC-M2-022 | 复杂长难句/长文档中被缩写句点多切分，句数多计（当前仍复现） |

修复状态：

- M2-D1 / M2-D2 / M2-D3 已修复并回归通过（模块一 24 条与上游套件均无回归）；
- M2-D5 已定位并实现修复方案，但开启后会使上游自带测试失败数由 8 条升至 37 条，
  故通过开关 `_MASK_ABBREVIATION_DOTS`（默认关闭）暂缓合入，待与上游同步期望值。

> 说明：这些用例在模块一修复后的代码上执行，仍能复现上述问题，说明它们是模块一
> 未覆盖的新问题（语言与字符集支持），而非模块一缺陷的重复。
