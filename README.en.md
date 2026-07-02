# Restaurant Operation Digital Advisor.skill

[中文](./README.md) | English

> An open-source agent skill for restaurant operation diagnosis: decide whether an operating problem should be solved by **systems, workflows, data handoff, or organizational responsibility**.

Restaurant Operation Digital Advisor is an agent-agnostic skill pack for restaurant owners, store leaders, chain operators, and restaurant digital consultants.

Many restaurants already use POS, online ordering, inventory, accounting, loyalty, delivery, and reporting tools. The hard question is not always "which system should we buy?" It is often:

> If we replaced the system tomorrow, would the same problem still happen?

If the answer is yes, the problem is not only a system problem.

## Questions You Can Ask

```text
Delivery, POS, inventory, loyalty, and accounting each have their own data.
Should we integrate first or replace systems?
```

```text
Inventory and month-end reconciliation are wrong. Is this a system issue,
a workflow issue, or a data handoff issue?
```

```text
We are expanding from 5 stores to 20. Can our current workflows and systems scale?
```

```text
The owner wants a system replacement in 3 months, but store and franchise data are messy.
How should we proceed?
```

## Start in 3 Minutes

### 1. Install

Ask the agent you use, such as Claude Code, Codex, OpenClaw, Cursor, Gemini CLI, or OpenCode:

```text
Install this skill: https://github.com/Sean0932/restaurant-operation-digital-advisor
```

Or use a generic skills installer:

```bash
npx skills add Sean0932/restaurant-operation-digital-advisor
```

Manual install paths:

| Runtime | Install path |
|---|---|
| Claude Code | `~/.claude/skills/restaurant-operation-digital-advisor/` |
| Codex | `~/.codex/skills/restaurant-operation-digital-advisor/` |
| OpenClaw | `~/.openclaw/workspace/skills/restaurant-operation-digital-advisor/` |
| Other agents | Put this repository in the runtime's `skills/` directory |

Claude Code example:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Sean0932/restaurant-operation-digital-advisor.git \
  ~/.claude/skills/restaurant-operation-digital-advisor
```

Restart the agent after installation.

### 2. Trigger

```text
Use the restaurant-operation-digital-advisor skill to run a restaurant operation readiness check.
```

You can also ask with a real operating problem:

```text
We have 3 stores and use POS, online ordering, inventory, and accounting software,
but inventory and month-end reconciliation are always wrong. Should we replace systems?
```

### 3. Expected Output

Most responses should be structured around:

- Current judgment;
- Root-cause attribution: systems / workflows / data handoff / responsibility;
- Main operating-chain risks;
- Next actions;
- Checklists or vendor questions when needed.

## Diagnosis Framework

This skill is not primarily a vendor recommender. It helps users classify the operating problem first.

| Root cause | Typical signs | What to inspect first |
|---|---|---|
| Systems | Missing features, weak configuration, poor integration, mismatched tools | Whether the current systems support the required operating actions |
| Workflows | Inconsistent store execution, overly complex process, unmanaged exceptions | Ordering, receiving, counting, waste, reconciliation, and handoff paths |
| Data handoff | Data exists but cannot move cleanly across roles, systems, and reports | Order, payment, inventory, and accounting traceability |
| Responsibility | Nobody owns creation, review, correction, or final interpretation | Who creates, reviews, fixes, and explains the numbers |

The central question:

> If the system changed tomorrow, would the same issue still happen?

If yes, do not treat it as a pure system-selection problem.

## Example

```text
User ❯ We have 3 stores and use POS, online ordering, inventory, and accounting software,
       but inventory and month-end reconciliation are always wrong. Should we replace systems?

Advisor ❯ Do not rush to replace systems.

          This looks more like a broken loop between order channels,
          inventory actions, and accounting rules.

          First, take 10 high-frequency SKUs and compare system stock,
          physical count, receiving, sales deduction, waste, transfers,
          and manual adjustment records for 7 consecutive days.

          Then take one recent month-end reconciliation gap and trace it
          from order, payment, refund, inventory deduction, waste, and transfer
          all the way to accounting entry.

          If the breakpoints concentrate at system handoff points,
          integration or replacement may be relevant.
          If the breakpoints are store recording, warehouse review,
          or month-end accounting correction, replacing systems will only
          move the same problem into a new interface.
```

More examples:

- [Problem diagnosis before system replacement](./examples/problem-diagnosis-before-system-change.md)
- [Data fragmentation review](./examples/data-fragmentation-review.md)
- [Large-chain system replacement risk](./examples/large-chain-system-replacement-risk.md)
- [Guided readiness flow](./examples/guided-readiness-flow.md)
- [Inventory issue review](./examples/inventory-issue-review.md)
- [Vendor selection](./examples/vendor-selection.md)

## Working Modes

- **Readiness Check**: decide whether the restaurant is ready to buy, replace, or integrate systems.
- **Vendor & System Selection**: define system categories, compare user-provided options, and prepare demo questions and acceptance checks.
- **Operating Workflow Design**: design or clean up ordering, receiving, prep, service, inventory count, waste, handoff, reconciliation, and member engagement.
- **Issue Diagnosis**: review inventory mismatch, reconciliation gaps, low system adoption, delivery order chaos, failed campaigns, or disconnected data.
- **Expansion Readiness**: assess whether workflows, data, and responsibility can scale to more stores or regions.
- **30-Day Action Plan**: turn diagnosis into weekly actions and lightweight follow-up review.
- **Integration & Data Handoff**: inspect data handoff across POS, delivery, inventory, accounting, loyalty/CRM, scheduling, and reporting.

Full readiness checks can be guided by short multiple-choice steps. In plain chat, users can answer with codes such as `1B, 2A, 3D`; agents with interactive UI can render the same flow as buttons or form choices.

## Vendor Recommendation Boundary

This skill does not provide default vendor rankings, affiliate-style recommendations, or paid placement.

It helps users define system requirements, compare user-provided options, and design vendor evaluation scenarios. If asked for specific vendor recommendations, first ask for market, scale, budget, current stack, required modules, integration needs, and language or compliance constraints. Only name specific vendors when the user provides candidate vendors or explicitly asks for current vendor research. Do not invent vendor capabilities, pricing, availability, or local support.

## Quick Scoring

Run the offline scoring script with a JSON assessment:

```bash
python3 scripts/score_assessment.py examples/sample-assessment.json
```

The script accepts JSON from a file or stdin and returns a score, readiness stage, dimension scores, risk tags, and suggested next focus.
Dimension results include risk levels and evidence status so high-risk reports do not mechanically assign the same score to every dimension.

## License

Apache-2.0. See [LICENSE](./LICENSE).
