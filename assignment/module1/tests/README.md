# 模块一自动化测试

本目录按组内分工分成两个子目录，pytest 会自动递归收集，一键即可运行全部用例。

```text
assignment/module1/tests/
├── conftest.py                 # 公共配置：把仓库根目录加入 sys.path，保证 import textstat
├── README.md                   # 本说明
├── count/                      # 成员 A：计数与预处理功能，24 条用例（TC-A-001 ~ TC-A-024）
│   ├── test_char_count.py          TC-A-001 ~ TC-A-002
│   ├── test_letter_count.py        TC-A-003 ~ TC-A-005
│   ├── test_lexicon_count.py       TC-A-006 ~ TC-A-008
│   ├── test_sentence_count.py      TC-A-009 ~ TC-A-011
│   ├── test_syllable_count.py      TC-A-012 ~ TC-A-014
│   ├── test_difficult_words.py     TC-A-015 ~ TC-A-017、TC-A-024
│   ├── test_long_word_count.py     TC-A-018 ~ TC-A-019
│   ├── test_monosyllabcount.py     TC-A-020 ~ TC-A-021
│   └── test_polysyllabcount.py     TC-A-022 ~ TC-A-023
└── metrics/                    # 成员 B：可读性指标功能，脚本与测试数据放这里
    └── test_metrics_*.py           编号与 test_cases.xlsx 中 TEXTSTAT-ST-RM-nnn 对应
```

## 一键运行

在仓库根目录执行（收集并运行两个子目录下的全部用例）：

```bash
.venv\Scripts\python -m pytest -v
```

只运行某个成员的用例：

```bash
.venv\Scripts\python -m pytest assignment/module1/tests/count -v
.venv\Scripts\python -m pytest assignment/module1/tests/metrics -v
```

`pytest.ini` 已配置 `testpaths = assignment`、`python_files = test_*.py`，因此无需指定文件名或逐个运行。

## 用例与脚本对照（成员 A：计数与预处理）

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

用例清单见 `assignment/module1/test_cases/test_cases.xlsx`（成员 A 与成员 B 合并后的统一清单）。

## 执行结果

第一轮（textstat 0.7.7 原始代码）：成员 A 的 24 条中 17 条完全通过（OK）、
3 条部分通过（POK）、4 条失败（NG），失败与部分通过用例对应 3 个缺陷。

| 缺陷 | 涉及用例 | 状态 | 现象 |
| --- | --- | --- | --- |
| A1 | TC-A-013、TC-A-014、TC-A-017、TC-A-021、TC-A-023 | NG / POK | cmudict 未收录词或数字词抛出 `KeyError`，未回退 pyphen |
| A2 | TC-A-005 | NG | `letter_count` 把数字与下划线计入字母数 |
| A3 | TC-A-011 | NG | `sentence_count` 忽略单词数不大于 2 的短句 |

第二轮（缺陷 A1 ~ A3 修复后回归）：成员 A 的 `24 passed`，全部用例完全通过。

## 注意事项

1. 两个子目录下的测试文件不要重名（pytest 默认按文件名区分模块），建议成员 B 统一用
   `test_metrics_xxx.py` 命名。
2. `conftest.py` 放在 `tests/` 根目录，对 `count/` 与 `metrics/` 两个子目录都生效；
   成员 B 如需额外 fixture，可在 `metrics/` 下新增自己的 `conftest.py`。
3. `__pycache__`、`.pytest_cache` 已在 `.gitignore` 中，不会被提交。
