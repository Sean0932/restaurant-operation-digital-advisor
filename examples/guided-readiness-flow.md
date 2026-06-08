# Example: Guided Readiness Flow

Use this when the user says they want to experience the full readiness check.

Trigger phrases may include:

- 做一次诊断
- 做一次体检
- 带我走一遍流程
- 完整体检
- 完整诊断

## Chinese Opening

```text
可以，我们用 5 步做一次餐饮经营数字化体检。

这次不是一上来判断“该不该换系统”，而是先看清：
问题到底卡在系统、流程、数据衔接，还是责任边界。

你可以直接回复编号，比如：1B、2A、3D。

第 1 步：先看经营画像和目标

1. 你现在主要在哪个市场经营？
A. 中国大陆
B. 港澳台或海外华人市场
C. 北美
D. 东南亚
E. 其他 / 不确定

2. 现在的经营形态更接近哪一种？
A. 单店
B. 2-10 家直营或小连锁
C. 10 家以上连锁
D. 直营 + 加盟混合
E. 中央厨房 / 多品牌 / 多区域

3. 这次最想解决什么？
A. 看看现在数字化准备度
B. 准备上新系统
C. 想换掉现有系统
D. 多个系统数据对不上，想整合
E. 准备扩店
F. 复盘一个具体问题，比如库存不准、对账乱、门店不用系统
```

After the user answers, confirm the interpretation and ask the next step.

## English Opening

```text
We can run a 5-step restaurant operation digital readiness check.

The goal is not to decide "which system to buy" first.
The goal is to diagnose whether the problem sits in systems, workflows,
data handoff, or responsibility boundaries.

You can reply with codes such as 1B, 2A, 3D.

Step 1: Business profile and goal

1. Market
A. Mainland China
B. Chinese-speaking market outside Mainland China
C. North America
D. Southeast Asia
E. Other / not sure

2. Operating model
A. Single store
B. 2-10 direct-owned stores or emerging chain
C. 10+ store chain
D. Mixed direct-owned and franchise operation
E. Central kitchen / multi-brand / multi-region operation

3. Main goal
A. Understand current readiness
B. Buy a new system
C. Replace existing systems
D. Integrate disconnected systems
E. Expand stores
F. Diagnose a specific issue such as inventory mismatch, reconciliation gaps, or low system adoption
```

## Follow-up Rhythm

Use this rhythm after each reply:

```text
我先确认一下：
- [short interpretation 1]
- [short interpretation 2]

这一步重要，是因为 [one sentence explaining why the next dimension matters].

下一步我们看 [next step name]：
[3-5 choices]
```

Do not produce the final diagnosis until the minimum required inputs are collected, unless the user explicitly asks for an early diagnosis.

When scoring in the final report, write `Score: 58` or `综合得分：58 分`. Do not write `58/88`.

Do not include specific vendor, platform, or software brand names in default guided questions. Use neutral categories such as POS, online ordering, delivery platform, inventory system, accounting system, loyalty/CRM system, scheduling system, or BI/reporting dashboard.
