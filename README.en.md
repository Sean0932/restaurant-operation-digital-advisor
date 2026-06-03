# Restaurant Operation Digital Advisor.skills

[中文](./README.md) | English

Restaurant Operation Digital Advisor is an open, agent-agnostic skill pack for restaurant digital operations.

It helps restaurant owners, store leaders, chain operators, and restaurant digital consultants decide whether an operating problem should be solved by a system, a workflow change, better data handoff, or clearer responsibility.

It is not a vendor ranking list, not a paid recommendation engine, and not a full restaurant management playbook. It focuses on restaurant operating chains: store execution, ordering, receiving, inventory, waste, reconciliation, loyalty, delivery, reporting, and the handoff between systems and people.

## What It Helps With

- Check whether a restaurant is ready to buy, replace, or integrate systems.
- Diagnose problems such as inventory mismatch, reconciliation gaps, low system adoption, delivery order chaos, or loyalty campaign failure.
- Prepare vendor demo questions and acceptance checks.
- Design workflows for ordering, receiving, prep, service, inventory count, waste, shift handoff, reconciliation, and member engagement.
- Assess expansion readiness from one store to multiple locations or from one region to another.
- Create a 30-day action plan after a readiness check, then run a lightweight follow-up review when the user returns after taking action.

For a full readiness check, the skill can guide users with short multiple-choice steps. In plain chat, users can answer with codes such as `1B, 2A, 3D`; in agents that support interactive UI, the same flow can be rendered as buttons or form choices.

## Design Principles

- Agent-agnostic: works as a readable skill pack for Codex, Claude Code, OpenClaw-style agents, and other agents that can load `SKILL.md`.
- Progressive disclosure: `SKILL.md` stays small; detailed knowledge lives in `references/`.
- Deterministic scoring: `scripts/score_assessment.py` keeps baseline readiness scores consistent across agents.
- Localized answers: the same framework is used globally, while terminology and examples adapt to the user's language and market.
- Open-source boundary: the public skill includes the framework, templates, scoring baseline, and examples; it excludes private prompts, customer data, payment logic, and commercial report templates.

## Install

This repository is a single skill folder: the repo root contains `SKILL.md`, `references/`, `scripts/`, and `examples/`.

### Claude Code

Claude Code discovers skills from `~/.claude/skills/<skill-name>/SKILL.md`.

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/Sean0932/restaurant-operation-digital-advisor.git \
  ~/.claude/skills/restaurant-operation-digital-advisor
```

Restart Claude Code, then ask:

```text
Use the restaurant-operation-digital-advisor skill to run a restaurant operation readiness check.
```

### Codex

Codex builds that support local skills commonly discover them from `~/.codex/skills/<skill-name>/SKILL.md`.

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Sean0932/restaurant-operation-digital-advisor.git \
  ~/.codex/skills/restaurant-operation-digital-advisor
```

Restart Codex, then ask:

```text
Use the restaurant-operation-digital-advisor skill.
```

If your Codex environment includes the `$skill-installer`, you can also ask Codex:

```text
$skill-installer install https://github.com/Sean0932/restaurant-operation-digital-advisor
```

### OpenClaw / 小龙虾

If your OpenClaw build supports Git skill installation:

```bash
openclaw skills install git:Sean0932/restaurant-operation-digital-advisor@main
```

Then enable or allow the skill according to your OpenClaw workspace configuration, restart the agent session if needed, and ask:

```text
Use the restaurant-operation-digital-advisor skill.
```

Manual install also works: clone or copy this repository into your OpenClaw skills directory so the final layout contains:

```text
restaurant-operation-digital-advisor/SKILL.md
```

## Vendor Recommendation Boundary

This skill does not provide default vendor rankings, affiliate-style recommendations, or paid placement.

It helps users define system requirements, compare user-provided options, and design vendor evaluation scenarios. If asked for specific vendor recommendations, first ask for market, scale, budget, current stack, required modules, integration needs, and language or compliance constraints. Only name specific vendors when current market information is available or provided by the user.

## Quick Scoring

Run the offline scoring script with a JSON assessment:

```bash
python3 scripts/score_assessment.py examples/sample-assessment.json
```

The script accepts JSON from a file or stdin and returns a score, readiness stage, dimension scores, risk tags, and suggested next focus.

## License

Apache-2.0. See [LICENSE](./LICENSE).

