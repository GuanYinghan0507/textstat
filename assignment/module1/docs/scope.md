# 模块一测试范围说明

## 被测对象

- textstat 0.7.7
- 被测代码固定于 Git tag `0.7.7`

## 被测功能

| 序号 | 功能 | 说明 | 负责人 |
| --- | --- | --- | --- |
| 1 | `char_count` | 统计字符数量 | 成员 A |
| 2 | `letter_count` | 统计字母数量 | 成员 A |
| 3 | `lexicon_count` | 统计词数 | 成员 A |
| 4 | `sentence_count` | 统计句子数量 | 成员 A |
| 5 | `syllable_count` | 统计音节数量 | 成员 A |
| 6 | `difficult_words` | 统计困难词数量 | 成员 A |
| 7 | `flesch_reading_ease` | Flesch 阅读易读度 | 成员 B |
| 8 | `flesch_kincaid_grade` | Flesch-Kincaid 年级水平 | 成员 B |
| 9 | `smog_index` | SMOG 指数 | 成员 B |
| 10 | `coleman_liau_index` | Coleman-Liau 指数 | 成员 B |
| 11 | `automated_readability_index` | 自动可读性指数 | 成员 B |
| 12 | `dale_chall_readability_score` | Dale-Chall 可读性分数 | 成员 B |
| 13 | `gunning_fog` | Gunning Fog 指数 | 成员 B |
| 14 | `text_standard` | 综合年级水平判断 | 成员 B |
| 15 | `linsear_write_formula` | Linsear Write 公式 | 成员 B |

## 不测范围

- 不测试阿拉伯语等非英语专用指标；
- 不测试命令行工具和打包发布流程；
- 不修改 textstat 的原有测试文件。

## 测试环境

- Python 3.x
- pytest
- textstat 0.7.7 本地源码
- NLTK cmudict 词典

## 运行方式

在仓库根目录执行：

```bash
python -m pytest -v
```
