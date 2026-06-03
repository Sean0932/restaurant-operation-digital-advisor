# 餐饮经营数字化顾问.skills

中文 | [English](./README.en.md)

餐饮经营数字化顾问是一个平台无关的开源 Agent Skill Pack。

它面向餐饮老板、门店负责人、连锁经营团队和餐饮数字化顾问，帮助他们在上系统、换系统、扩店、流程梳理、异常复盘时判断：问题到底该靠系统、流程、数据衔接，还是组织责任来解决。

它不是系统品牌排行榜，不是带货推荐，也不是餐饮经营百科。它关注的是餐饮经营链路：门店执行、订货、收货、库存、报损、对账、会员、外卖、报表，以及系统和人之间的交接。

## 能解决什么

- 判断现在是否适合上系统、换系统或做系统整合。
- 复盘库存不准、对账差异、门店不用系统、外卖订单混乱、会员活动无效、系统数据对不上等问题。
- 生成供应商演示问题、验收标准和选型对比表。
- 梳理订货、收货、备货、出餐、盘点、报损、交班、对账、会员触达等流程。
- 判断单店、成长期连锁、成熟连锁在扩店前是否准备好。
- 把诊断结果拆成 30 天行动计划；用户一段时间后回来时，可以做轻量复查，判断下一阶段该继续理流程、做试点，还是进入选型。

如果用户想体验完整体检，skill 可以用分步选择题引导。普通聊天里可以回复 `1B, 2A, 3D` 这种编号；如果某个 agent 支持按钮或表单，也可以把同一套流程渲染成可点击选项。

## 设计原则

- 不绑定某个 agent：Codex、Claude Code、小龙虾 / OpenClaw 类 agent，或任何能读取 `SKILL.md` 的 agent 都可以使用。
- 渐进加载：`SKILL.md` 只放流程和边界，详细框架放在 `references/`。
- 规则评分：`scripts/score_assessment.py` 固化基础评分，避免不同 agent 算分漂移。
- 全球框架，本地表达：核心诊断框架不变，但会根据语言和市场调整术语、例子和语气。
- 开源有边界：开放方法论、题库、基础评分、模板和样例；不开放真实客户数据、支付逻辑、私有提示词和商业版完整报告。

## 默认不直接推荐系统品牌

默认不直接推荐某个系统品牌。先帮你看清该选哪类系统、该用哪些真实场景考供应商。如果你已经有几个候选系统，可以帮你做对比表和演示问题清单。

如果用户一定要具体品牌推荐，需要先明确所在市场、门店规模、预算、现有系统、需要的模块、集成要求、语言和合规限制；没有当前市场信息时，不编造系统能力、价格、可用性或本地服务。

## 安装使用

这个仓库本身就是一个 skill 目录：根目录包含 `SKILL.md`、`references/`、`scripts/` 和 `examples/`。

### Claude Code

Claude Code 通常会从 `~/.claude/skills/<skill-name>/SKILL.md` 发现 skill。

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Sean0932/restaurant-operation-digital-advisor.git \
  ~/.claude/skills/restaurant-operation-digital-advisor
```

重启 Claude Code 后可以这样问：

```text
请使用 restaurant-operation-digital-advisor 这个 skill，帮我做一次餐饮经营数字化体检。
```

### Codex

支持本地 skills 的 Codex 通常会从 `~/.codex/skills/<skill-name>/SKILL.md` 发现 skill。

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Sean0932/restaurant-operation-digital-advisor.git \
  ~/.codex/skills/restaurant-operation-digital-advisor
```

重启 Codex 后可以这样问：

```text
请使用 restaurant-operation-digital-advisor 这个 skill。
```

如果你的 Codex 环境带 `$skill-installer`，也可以直接让 Codex 执行：

```text
$skill-installer install https://github.com/Sean0932/restaurant-operation-digital-advisor
```

### OpenClaw / 小龙虾

如果你的小龙虾 / OpenClaw 版本支持 Git skill 安装，可以尝试：

```bash
openclaw skills install git:Sean0932/restaurant-operation-digital-advisor@main
```

然后按你的 OpenClaw 工作区配置启用或允许该 skill，必要时重启 agent 会话。

也可以手动安装：把这个仓库 clone 或复制到 OpenClaw 的 skills 目录中，确保最终结构是：

```text
restaurant-operation-digital-advisor/SKILL.md
```

### 其它 Agent

只要 agent 支持 `SKILL.md` 约定，就把这个仓库作为一个完整 skill 目录安装。最终结构应该是：

```text
<skills-directory>/restaurant-operation-digital-advisor/SKILL.md
<skills-directory>/restaurant-operation-digital-advisor/references/
<skills-directory>/restaurant-operation-digital-advisor/scripts/
<skills-directory>/restaurant-operation-digital-advisor/examples/
```

## 快速评分

可以用本地脚本做离线评分：

```bash
python3 scripts/score_assessment.py examples/sample-assessment.json
```

脚本支持从文件或 stdin 读取 JSON，输出总分、阶段判断、维度得分、风险标签和下一步重点。

## 许可证

Apache-2.0。详见 [LICENSE](./LICENSE)。
