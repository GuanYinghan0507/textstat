# textstat 软件测试与质量保证实践作业

本仓库基于 `textstat` 0.7.7 完成《软件测试与质量保证实践》模块一和模块二作业。

## 被测对象

- 项目：textstat（Python 文本统计与可读性指标库）
- 被测版本：`0.7.7`（Git tag：`0.7.7`）
- 上游地址：https://github.com/textstat/textstat
- 作业分支：`assignment`

textstat 源码位于仓库根目录，作为被测对象基线保留。小组的测试、用例、缺陷记录和报告统一放在 `assignment/` 下，与上游自带测试分开，便于教师检查个人贡献。

## 目录结构

```text
assignment/
  module1/
    tests/           # 模块一手写 pytest 测试
    test_cases/      # 附录1：测试用例清单（Excel）
    defects/         # 附录2：缺陷报告（Word）
    reports/         # 附录3：模块一测试报告（Word）
    docs/            # 测试范围、环境说明
  module2/
    tests/           # 模块二 AI 生成并人工核对的 pytest 测试
    test_cases/      # 附录1：AI 生成测试用例清单（Excel）
    defects/         # 附录2：缺陷报告（Word）
    reports/         # 附录4：模块二测试报告（Word）
    ai_dialogues/    # 关键 AI 对话记录
```

## 环境配置

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -r assignment/requirements.txt
```

如果当前环境尚未安装 textstat，可先在仓库根目录执行：

```bash
pip install -e .
```

textstat 0.7.7 依赖 pyphen、cmudict 和 setuptools。音节计算需要 cmudict 词典数据，按仓库根目录的 requirements.txt 安装依赖即可；如果网络受限，可以配置国内镜像后重新安装。

## 运行测试

在仓库根目录执行：

```bash
python -m pytest -v
```

pytest.ini 已配置为只收集 assignment/ 下的测试，不会把上游自带的 tests/ 误算为本小组工作量。

## 模块说明

模块一为人工测试实践。测试用例和自动化脚本由小组成员手写，不使用 AI 生成。

模块二为 AI 测方案。使用 AI 工具生成不少于 15 条测试用例、测试数据和 pytest 脚本，并对比人工修正前后的差异；AI 对话记录存放在 assignment/module2/ai_dialogues/。

## 分工约定

管映涵负责计数与预处理功能，韩迎小负责可读性指标功能。两人分别编写各自模块的测试用例和自动化脚本，并交叉复核对方至少 2 条用例。所有提交使用个人 GitHub 账号，提交信息说明实际改动内容。

最终贡献度按实际提交和工作量填写，两人占比总和应等于 100%。

## 提交信息示例

docs: 初始化作业目录与测试环境说明
test: 添加syllable_count边界值用例
test: 添加flesch_reading_ease等价类用例
docs: 记录缺陷A1的复现步骤与原因分析
fix: 修复text_standard年级边界缺陷
