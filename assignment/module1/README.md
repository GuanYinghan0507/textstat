# 模块一：测试基础实践

## 交付物

1. 测试用例清单（附录1 Excel，至少 30 条，覆盖等价类、边界值、场景法中的至少 2 种）
2. 自动化测试脚本（一键运行全部用例，附运行说明）
3. 缺陷清单（附录2 Word，至少 3 个有效缺陷）
4. 模块一测试报告（附录3 Word）
5. 成果汇报 PPT 与演示视频

## 测试用例清单

最终合并用例清单见 [`test_cases/test_cases.xlsx`](test_cases/test_cases.xlsx)，共 44 条：

- 管映涵：`TC-A-001` 至 `TC-A-024`
- 韩迎小：`TEXTSTAT-ST-RM-001` 至 `TEXTSTAT-ST-RM-020`

## 自动化测试运行说明

自动化脚本位于 `tests/`，目录结构、用例与脚本对照及运行方式见 [`tests/README.md`](tests/README.md)。

在仓库根目录执行：

```bash
python -m pytest -v
```

Windows 虚拟环境可执行：

```powershell
.venv\Scripts\python -m pytest -v
```

## 测试范围

管映涵负责计数与预处理功能：

- `char_count`
- `letter_count`
- `lexicon_count`
- `sentence_count`
- `syllable_count`
- `difficult_words`
- `long_word_count`
- `monosyllabcount`
- `polysyllabcount`

韩迎小负责可读性指标功能及指标句数依赖，共覆盖 20 条测试用例：

- `flesch_reading_ease`
- `smog_index`
- `flesch_kincaid_grade`
- `coleman_liau_index`
- `automated_readability_index`
- `dale_chall_readability_score`
- `difficult_words`
- `text_standard`
- `linsear_write_formula`
- `gunning_fog`
- `fernandez_huerta`
- `szigriszt_pazos`
- `gutierrez_polini`
- `sentence_count`（可读性指标句数依赖）
- `crawford`
- `gulpease_index`
- `osman`

## 测试设计方法

- 等价类划分：区分合法英文文本、空文本、纯标点、纯数字、中英混排等输入类型。
- 边界值分析：覆盖空字符串、极短文本、极长文本、单词边界、句子边界和公式阈值。
- 场景法：验证“输入文本到统计结果”的完整调用链，以及不同语言配置下的行为。

## 缺陷要求

缺陷必须能够稳定复现，并记录现象、复现步骤、预期结果、实际结果、原因分析、修复提交和回归结果。不要提交无法复现或仅凭主观判断的问题。

## 合规提醒

本模块禁止使用 AI 生成测试用例和自动化测试脚本。用例设计、测试数据和 pytest 代码由两名成员自行完成。
