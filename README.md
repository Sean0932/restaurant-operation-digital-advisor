# 餐饮经营数字化顾问.skill

> 「别急着换系统，先判断问题到底是不是系统能解决。」

![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue)
![Runtime](https://img.shields.io/badge/runtime-Claude%20Code%20%7C%20Codex%20%7C%20OpenClaw-green)
![License](https://img.shields.io/badge/license-Apache--2.0-lightgrey)

餐饮经营数字化顾问帮餐饮老板、门店负责人、连锁经营团队判断：库存、对账、会员、外卖、门店执行这些问题，到底该靠**系统、流程、数据衔接，还是责任边界**来解决。

会用 Agent 的餐饮人，可以免费安装这个 skill 自查。  
不会安装 Agent 的餐饮老板，可以使用线上产品付费生成完整报告。

[English](./README.en.md)

---

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

再来一个更像连锁品牌的场景：

```text
用户 ❯ 我们是 30-50 家咖啡/茶饮门店，直营+加盟混合。
       POS 能用，但 ERP 弱，成本数据和盘盈盘亏经常对不上。

顾问 ❯ 现在不应该只问“换哪套 ERP”。

       先把「采购 → 中心仓 → 门店收货 → 报损/报溢 → 月底盘点
       → 成本核算 → 财务入账」这条链路拆开。

       你最该先验证三个断点：
       1. 门店收货、报损、盘点有没有当天进入系统；
       2. 加盟店库存总部到底能不能看到；
       3. ERP 到财务软件之间是自动校验，还是人工导表。

       供应商演示时，不要只看标准流程，要拿真实异常去考。
```

---

## 它能做什么

- **经营链路体检**：判断现在是否适合上系统、换系统或做系统整合。
- **系统选型顾问**：生成供应商演示问题、验收标准和选型对比表。
- **经营流程梳理**：梳理订货、收货、备货、出餐、盘点、报损、交班、对账、会员触达等流程。
- **异常复盘**：复盘库存不准、对账差异、门店不用系统、外卖订单混乱、会员活动无效、系统数据对不上等问题。
- **扩店准备**：判断单店、成长期连锁、成熟连锁在扩店前是否准备好。
- **30 天行动陪跑**：把诊断结果拆成周计划；用户一段时间后回来时，可以做轻量复查。
- **系统衔接检查**：检查 POS、外卖、小程序、库存、财务、会员、排班、报表之间的数据交接。

完整体检会用分步选择题引导。普通聊天里可以回复 `1B, 2A, 3D` 这种编号；如果某个 Agent 支持按钮或表单，也可以把同一套流程渲染成可点击选项。

---

## 安装

这个仓库本身就是一个 skill 目录：根目录包含 `SKILL.md`、`references/`、`scripts/` 和 `examples/`。

### 方式一：一行命令（推荐）

打开你正在用的 Agent（Claude Code、Codex、Cursor、小龙虾 / OpenClaw、Gemini CLI、OpenCode 等），告诉它：

```text
帮我安装这个 skill：https://github.com/Sean0932/restaurant-operation-digital-advisor
```

或者使用通用 skills 安装器：

```bash
npx skills add Sean0932/restaurant-operation-digital-advisor
```

需要指定 runtime 时，可按你的安装器支持情况加类似参数，例如 `-a claude-code` / `-a codex` / `-a openclaw`。

### 方式二：手动安装

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

装好后，重启 Agent，告诉它：

```text
请使用 restaurant-operation-digital-advisor 这个 skill，帮我做一次餐饮经营数字化体检。
```

### 方式三：作为参考资料使用

即使你的 Agent 不支持自动加载 Agent Skills，也可以直接把 `SKILL.md` 的内容粘贴进对话。它本质是一份 Markdown + YAML frontmatter 的工作流说明。

---

## 工作原理

这个 skill 不直接给“买哪套系统”的答案，而是先判断问题属于哪一类：

| 根因桶 | 说明 |
|---|---|
| 系统 | 功能缺失、配置错误、集成弱、工具不匹配 |
| 流程 | 实际运营路径不清晰、过于复杂、或没有被遵守 |
| 数据衔接 | 数据存在，但无法在角色、系统、报表之间干净流转 |
| 责任 | 无人对创建、审核、修正、最终解释负责 |

核心问题只有一个：

> 如果明天系统换了，同样的问题还会不会发生？

如果答案是“会”，就不能把问题简单定性为系统问题。

---

## 诚实边界

这个 skill 明确不做几件事：

- 不默认推荐某个系统品牌。
- 不做系统排行榜、返佣推荐或带货。
- 不替代专业财务、法律、税务、食品安全或劳动合规意见。
- 不做餐饮经营百科；菜单研发、社媒营销、招聘培训、菜品定价只有在影响系统、流程、数据或责任时才纳入。
- 不做通用 IT 系统盘点；IM、打车、OA、考勤、报销等工具只有在影响门店执行、成本归集、审批责任或财务对账时才纳入。

如果用户已经有候选系统，它可以帮你做对比表、演示问题和验收清单。  
如果用户要求具体品牌推荐，需要先明确所在市场、门店规模、预算、现有系统、模块需求、集成要求、语言和合规限制。

---

## 仓库结构

```text
restaurant-operation-digital-advisor/
  SKILL.md
  references/
    operating-chain-framework.md
    advisor-modes.md
    questionnaire.md
    scoring-rules.md
    report-templates.md
    vendor-evaluation.md
    integration-checklist.md
    common-failure-patterns.md
    localization-guide.md
    open-source-boundary.md
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

