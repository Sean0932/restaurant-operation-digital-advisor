# Scoring Rules

The public score is directional. It is designed to be explainable, not mathematically perfect.

Use `scripts/score_assessment.py` when structured inputs are available.

## Overall Score

Start from 82 points. Deduct for operating complexity and risk:

- store count above 1,
- number of major systems,
- SKU/menu complexity,
- order volume,
- labor pressure,
- number of selected operating issues,
- expansion model complexity.

Clamp the score between 30 and 88 as an internal calibration guardrail. Do not present 88 as the denominator.

User-facing format:

- Correct: `Score: 58` / `58 points` / `综合得分：58 分`
- Avoid: `58/88`, `58 out of 88`, or `58 / 88`

## Stage

- **80-88**: Ready for limited system selection, but test exception scenarios.
- **65-79**: Suitable for a pilot workflow before broad rollout.
- **50-64**: Clarify workflow and responsibility before buying heavy systems.
- **30-49**: Direct system replacement is risky; fix operating basics first.

## Dimension Scores

Dimension scores are derived from the overall score and issue tags:

- Store execution
- Supply and inventory loop
- Finance and reconciliation
- Customer and loyalty operations
- System fit and data handoff
- Responsibility and organization

Even when the overall score is in the 30-49 high-risk range, do not mechanically assign the same score to every dimension. Dimension scores must reflect the evidence the user provided:

- If a dimension has clear issue evidence, mark it as high risk and lower its score.
- If a dimension has weak or missing evidence, do not force it to the floor; mark the evidence as insufficient or use "待确认" in narrative output.
- Prefer a risk-level table when the inputs are not structured enough for precise dimension scores.
- Avoid claims such as "all dimensions hit bottom" unless the user explicitly provided severe evidence for every dimension.

Recommended user-facing risk levels:

| Score range | Risk level | Chinese label |
|---|---|---|
| 75-88 | low | 低风险 |
| 60-74 | medium | 中风险 |
| 45-59 | medium_high | 中高风险 |
| 30-44 | high | 高风险 |
| 24-29 | critical | 极高风险 |

Keep the explanation tied to user inputs. Do not present the score as an objective audit result.
