# 模块一自动化测试

本目录按组内分工分成两个子目录，pytest 会自动递归收集，一键即可运行全部用例。

```text
assignment/module1/tests/
├── conftest.py                 # 公共配置：把仓库根目录加入 sys.path，保证 import textstat
├── README.md                   # 本说明
├── count/                      # 管映涵：计数与预处理功能，24 条用例（TC-A-001 ~ TC-A-024）
│   ├── test_char_count.py
│   ├── test_letter_count.py
│   ├── test_lexicon_count.py
│   ├── test_sentence_count.py
│   ├── test_syllable_count.py
│   ├── test_difficult_words.py
│   ├── test_long_word_count.py
│   ├── test_monosyllabcount.py
│   └── test_polysyllabcount.py
├── metrics_test_data.json      # 韩迎小：20 条可读性指标用例数据
└── metrics/                    # 韩迎小：16 个可读性指标函数与句数依赖用例
    ├── conftest.py
    ├── metrics_helpers.py
    ├── test_metrics_flesch_reading_ease.py
    ├── test_metrics_smog_index.py
    ├── test_metrics_flesch_kincaid_grade.py
    ├── test_metrics_coleman_liau_index.py
    ├── test_metrics_automated_readability_index.py
    ├── test_metrics_dale_chall_readability_score.py
    ├── test_metrics_difficult_words.py
    ├── test_metrics_text_standard.py
    ├── test_metrics_linsear_write_formula.py
    ├── test_metrics_gunning_fog.py
    ├── test_metrics_fernandez_huerta.py
    ├── test_metrics_szigriszt_pazos.py
    ├── test_metrics_gutierrez_polini.py
    ├── test_metrics_sentence_count_metrics.py
    ├── test_metrics_crawford.py
    ├── test_metrics_gulpease_index.py
    └── test_metrics_osman.py
```

最终合并测试用例清单见 [`../test_cases/test_cases.xlsx`](../test_cases/test_cases.xlsx)，共 44 条：管映涵 24 条、韩迎小 20 条。

## 一键运行与结果判定

在仓库根目录执行：

```bash
python -m pytest -v
```

Windows 虚拟环境可执行：

```powershell
.venv\Scripts\python -m pytest -v
```

该命令会同时收集 `count/` 和 `metrics/` 下的全部测试。

NG 用例处理说明：

- OK、POK 用例按预期通过。
- NG 用例是已知缺陷的复现用例，当前脚本不将其标记为 `xfail`，在 textstat 0.7.7 原始版本上会显示为 `failed`。因此全量运行出现失败项并返回非零退出码，属于缺陷验证的预期结果，应结合缺陷报告说明，不应通过修改断言把 NG 强行改成通过。
- NT 用例通过 `pytest.skip` 跳过，并记录跳过原因。
- 如果现场演示需要退出码为 0 的结果，应先将 NG 用例改为 `xfail`，或单独运行 OK/POK 用例；本次说明按当前脚本的实际处理方式记录。

## 用例与脚本对照（管映涵：计数与预处理）

| 用例编号 | 被测函数 | 脚本 |
| --- | --- | --- |
| TC-A-001 ~ TC-A-002 | `char_count` | `count/test_char_count.py` |
| TC-A-003 ~ TC-A-005 | `letter_count` | `count/test_letter_count.py` |
| TC-A-006 ~ TC-A-008 | `lexicon_count` | `count/test_lexicon_count.py` |
| TC-A-009 ~ TC-A-011 | `sentence_count` | `count/test_sentence_count.py` |
| TC-A-012 ~ TC-A-014 | `syllable_count` | `count/test_syllable_count.py` |
| TC-A-015 ~ TC-A-017、TC-A-024 | `difficult_words` | `count/test_difficult_words.py` |
| TC-A-018 ~ TC-A-019 | `long_word_count` | `count/test_long_word_count.py` |
| TC-A-020 ~ TC-A-021 | `monosyllabcount` | `count/test_monosyllabcount.py` |
| TC-A-022 ~ TC-A-023 | `polysyllabcount` | `count/test_polysyllabcount.py` |

## 计数与预处理部分历史执行结果（管映涵）

第一轮（textstat 0.7.7 原始代码）共执行 24 条：

```text
7 failed, 17 passed
```

说明：3 条 POK 用例内部既有通过断言也有失败断言，pytest 按整条用例记为 `failed`，
因此 4 条 NG 加 3 条 POK 共 7 条失败，与附录1 中的 NG 4 条、POK 3 条一一对应。

附录状态分布：

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| OK | 17 | 实际结果符合预期 |
| POK | 3 | 常规文本断言通过、含词典未收录词的文本抛出 `KeyError`，属部分通过 |
| NG | 4 | 数字与下划线被计入字母数、短句被忽略、音节统计抛出 `KeyError` |
| NT | 0 | 本部分无用例标记为 NT |

| 状态 | 用例 | 现象 |
| --- | --- | --- |
| POK | TC-A-014 | `syllable_count` 常规文本返回 11（通过），含 interoperability 的文本抛 `KeyError` |
| POK | TC-A-017 | `difficult_words` 常规文本返回 0（通过），含未收录词文本抛 `KeyError` |
| POK | TC-A-023 | `polysyllabcount` 常规文本返回 0（通过），含未收录词文本抛 `KeyError` |
| NG | TC-A-005 | `letter_count("3 apples")` 返回 7（应 6）、`letter_count("hello_world")` 返回 11（应 10） |
| NG | TC-A-011 | `sentence_count("Hello. World.")` 返回 1（应 2）、`sentence_count("One. Two. Three. Four. Five.")` 返回 1（应 5） |
| NG | TC-A-013 | `syllable_count("In 2024 we win.")` 抛 `KeyError: '2024'` |
| NG | TC-A-021 | `monosyllabcount("In 2024 we win.")` 抛 `KeyError: '2024'` |

第二轮（修复缺陷 A1 ~ A3 后，全量执行）：

```text
24 passed
```

第三轮（与可读性指标用例合并后的全量运行）：计数与预处理 24 条全部通过；
全量 44 条为 `4 failed, 39 passed, 1 skipped`，失败项均在 `metrics/` 下，
由韩迎小按其缺陷记录继续处理（见上一节）。

用例清单版本：v1.00 初稿 32 条 → v1.01 精简为 24 条（删除 2 条与其他函数重复的空字符串用例、
合并 7 组重复输入用例）→ v1.02 保留全部缺陷相关用例并新增 `difficult_words` 音节阈值边界用例
TC-A-024，明细见 `../test_cases/test_cases.xlsx` 的修订记录。

## 用例与脚本对照（韩迎小：可读性指标）

韩迎小共 20 条用例，覆盖 16 项可读性指标函数及句数依赖边界。

| 用例编号 | 被测函数/场景 | 脚本 |
| --- | --- | --- |
| TEXTSTAT-ST-RM-001、011 | `flesch_reading_ease` | `metrics/test_metrics_flesch_reading_ease.py` |
| TEXTSTAT-ST-RM-002 | `smog_index` | `metrics/test_metrics_smog_index.py` |
| TEXTSTAT-ST-RM-003 | `flesch_kincaid_grade` | `metrics/test_metrics_flesch_kincaid_grade.py` |
| TEXTSTAT-ST-RM-004 | `coleman_liau_index` | `metrics/test_metrics_coleman_liau_index.py` |
| TEXTSTAT-ST-RM-005 | `automated_readability_index` | `metrics/test_metrics_automated_readability_index.py` |
| TEXTSTAT-ST-RM-006 | `dale_chall_readability_score` | `metrics/test_metrics_dale_chall_readability_score.py` |
| TEXTSTAT-ST-RM-007、019 | `difficult_words` | `metrics/test_metrics_difficult_words.py` |
| TEXTSTAT-ST-RM-008 | `text_standard` | `metrics/test_metrics_text_standard.py` |
| TEXTSTAT-ST-RM-009 | `linsear_write_formula` | `metrics/test_metrics_linsear_write_formula.py` |
| TEXTSTAT-ST-RM-010 | `gunning_fog` | `metrics/test_metrics_gunning_fog.py` |
| TEXTSTAT-ST-RM-012 | `fernandez_huerta` | `metrics/test_metrics_fernandez_huerta.py` |
| TEXTSTAT-ST-RM-013 | `szigriszt_pazos` | `metrics/test_metrics_szigriszt_pazos.py` |
| TEXTSTAT-ST-RM-014 | `gutierrez_polini` | `metrics/test_metrics_gutierrez_polini.py` |
| TEXTSTAT-ST-RM-015、020 | `sentence_count` | `metrics/test_metrics_sentence_count_metrics.py` |
| TEXTSTAT-ST-RM-016 | `crawford` | `metrics/test_metrics_crawford.py` |
| TEXTSTAT-ST-RM-017 | `gulpease_index` | `metrics/test_metrics_gulpease_index.py` |
| TEXTSTAT-ST-RM-018 | `osman` | `metrics/test_metrics_osman.py` |

## 可读性指标部分历史执行结果（韩迎小）

第一轮（textstat 0.7.7 原始代码）共执行 20 条：

```text
3 failed, 16 passed, 1 skipped
```

附录状态分布：

| 状态 | 数量 | 说明 |
| --- | ---: | --- |
| OK | 14 | 实际结果符合预期 |
| POK | 2 | SMOG 最小样本可信度有限、Text Standard 下限标签存在语义争议 |
| NG | 3 | 对应 ARI 句数依赖、缩写/小数分句、Dale-Chall 词形规则三个缺陷 |
| NT | 1 | 当前版本未提供中文可读性指标基准 |

| 状态 | 用例 | 现象 |
| --- | --- | --- |
| POK | TEXTSTAT-ST-RM-002 | SMOG 仅满足 3 句程序下限，低于规范建议的 30 句 |
| POK | TEXTSTAT-ST-RM-008 | `text_standard` 下限返回 `0th and 1st grade` |
| NG | TEXTSTAT-ST-RM-005 | 短句被少计，导致 ARI 实际值与预期值不一致 |
| NG | TEXTSTAT-ST-RM-015 | 缩写及小数点被误判为句末，句数多计 |
| NG | TEXTSTAT-ST-RM-019 | Dale-Chall 规则变形和所有格被误判为难词 |
| NT | TEXTSTAT-ST-RM-011 | 中文场景缺少可执行的中文可读性指标基准 |

## 注意事项

1. `count/` 与 `metrics/` 下的测试文件不能重名；韩迎小统一使用 `test_metrics_*.py` 前缀，避免 pytest 模块名冲突。
2. `conftest.py` 放在 `tests/` 根目录，对两个子目录都生效；`metrics/conftest.py` 额外负责测试前后重置语言设置。
3. `__pycache__`、`.pytest_cache` 已在 `.gitignore` 中，不会被提交。
