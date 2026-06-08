# 餐饮经营数字化顾问.skill

> 一个开源 Agent Skill，帮助餐饮人判断经营问题到底该靠**系统、流程、数据衔接，还是责任边界**解决。

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Runtime](https://img.shields.io/badge/runtime-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw-green)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

[English](./README.en.md)

---

很多餐饮店现在不是没有系统。收银、小程序、库存、财务、会员、外卖可能都用了，但库存还是不准，月底对账还是痛苦，门店还是有人不用系统。

这个 skill 不急着回答“该换哪套系统”。它先帮你判断：如果明天系统换了，同样的问题还会不会发生？

如果答案是“会”，问题通常不只是系统。

## 3 分钟开始使用

### 1. 安装

打开你正在用的 Agent（Claude Code、Codex、小龙虾 / OpenClaw、Cursor、Gemini CLI、OpenCode 等），告诉它：

```text
帮我安装这个 skill：https://github.com/Sean0932/restaurant-operation-digital-advisor
```

或者使用通用 skills 安装器：

```bash
npx skills add Sean0932/restaurant-operation-digital-advisor
```

手动安装路径：

| Runtime | 安装路径 |
|---|---|
| Claude Code | `~/.claude/skills/restaurant-operation-digital-advisor/` |
| Codex | `~/.codex/skills/restaurant-operation-digital-advisor/` |
| OpenClaw / 小龙虾 | `~/.openclaw/workspace/skills/restaurant-operation-digital-advisor/` |
| 其他 Agent | 放到对应 runtime 的 `skills/` 目录 |

以 Claude Code 为例：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Sean0932/restaurant-operation-digital-advisor.git \
  ~/.claude/skills/restaurant-operation-digital-advisor
```

装好后重启 Agent。

### 2. 触发

```text
请使用 restaurant-operation-digital-advisor 这个 skill，帮我做一次餐饮经营数字化体检。
```

也可以直接问一个真实问题：

```text
我们现在 3 家店，用了收银、小程序、库存系统和财务软件，
但库存和月底对账总是不准。是不是该换系统？
```

### 3. 你会得到什么

多数回答会收束成这 5 件事：

- 当前判断；
- 根因归因：系统 / 流程 / 数据衔接 / 责任；
- 主要经营链路风险；
- 下一步动作；
- 必要时给检查清单或供应商问题。

## 判断框架

这个 skill 的核心价值不是“推荐系统”，而是先把经营问题分清楚。

| 问题类型 | 典型表现 | 先看什么 |
|---|---|---|
| 系统 | 功能缺失、配置错误、集成弱、工具不匹配 | 当前系统是否真的支持关键动作 |
| 流程 | 门店动作不一致、流程过复杂、实际没人按流程做 | 订货、收货、盘点、报损、对账是否有固定路径 |
| 数据衔接 | 数据存在，但在系统、角色、报表之间对不上 | 订单、支付、库存、财务是否能一路追溯 |
| 责任边界 | 无人审核、无人修正、无人解释最终口径 | 谁创建、谁审核、谁改错、谁对结果负责 |

核心问题只有一个：

> 如果明天系统换了，同样的问题还会不会发生？

如果会，先别把问题简单定性为系统问题。

## 效果示例

```text
用户 ❯ 我们现在 3 家店，用了收银、小程序、库存系统和财务软件，
       但库存和月底对账总是不准。是不是该换系统？

顾问 ❯ 先别急着换系统。

       你这个问题更像是订单渠道、库存动作和财务口径之间没有闭环。
       先抽 10 个高频 SKU，连续 7 天核对系统库存、实盘、收货、
       销售扣减、报损、调拨和人工修改记录。

       再拿最近一笔月底对账差异，从订单、支付、退款、库存扣减、
       报损、调拨一路追到财务入账。

       如果断点集中在系统交接处，再考虑集成或换系统；
       如果断点在门店没录、仓库没审、财务月底补，
       换系统只会把问题换个界面继续发生。
```

更多示例见：

- [换系统前的问题诊断](./examples/problem-diagnosis-before-system-change.md)
- [完整体检引导流程](./examples/guided-readiness-flow.md)
- [库存异常复盘](./examples/inventory-issue-review.md)
- [系统选型顾问](./examples/vendor-selection.md)

## 它能做什么

- **经营链路体检**：判断现在是否适合上系统、换系统或做系统整合。
- **系统选型顾问**：生成供应商演示问题、验收标准和选型对比表。
- **经营流程梳理**：梳理订货、收货、备货、出餐、盘点、报损、交班、对账、会员触达等流程。
- **异常复盘**：复盘库存不准、对账差异、门店不用系统、外卖订单混乱、会员活动无效、系统数据对不上等问题。
- **扩店准备**：判断单店、成长期连锁、成熟连锁在扩店前是否准备好。
- **30 天行动陪跑**：把诊断结果拆成周计划；用户一段时间后回来时，可以做轻量复查。
- **系统衔接检查**：检查 POS、外卖、小程序、库存、财务、会员、排班、报表之间的数据交接。

完整体检会用分步选择题引导。普通聊天里可以回复 `1B, 2A, 3D` 这种编号；如果某个 Agent 支持按钮或表单，也可以把同一套流程渲染成可点击选项。

## 安装细节

这个仓库本身就是一个 skill 目录：根目录包含 `SKILL.md`、`references/`、`scripts/` 和 `examples/`。

如果你的 Agent 不支持自动加载 Agent Skills，也可以直接把 `SKILL.md` 的内容粘贴进对话。它本质是一份 Markdown + YAML frontmatter 的工作流说明。

## 诚实边界

这个 skill 明确不做几件事：

- 不默认推荐某个系统品牌。
- 不做系统排行榜、返佣推荐或带货。
- 不替代专业财务、法律、税务、食品安全或劳动合规意见。
- 不做餐饮经营百科；菜单研发、社媒营销、招聘培训、菜品定价只有在影响系统、流程、数据或责任时才纳入。
- 不做通用 IT 系统盘点；IM、打车、OA、考勤、报销等工具只有在影响门店执行、成本归集、审批责任或财务对账时才纳入。

如果用户已经有候选系统，它可以帮你做对比表、演示问题和验收清单。  
如果用户要求具体品牌推荐，需要先明确所在市场、门店规模、预算、现有系统、模块需求、集成要求、语言和合规限制。

## 仓库结构

```text
restaurant-operation-digital-advisor/
  SKILL.md
  references/
  scripts/
    score_assessment.py
  examples/
```

## 快速评分

可以用本地脚本做离线评分：

```bash
python3 scripts/score_assessment.py examples/sample-assessment.json
```

脚本支持从文件或 stdin 读取 JSON，输出总分、阶段判断、维度得分、风险标签和下一步重点。

## License

Apache-2.0. See [LICENSE](./LICENSE).
