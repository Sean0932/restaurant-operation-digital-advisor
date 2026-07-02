#!/usr/bin/env python3
"""Offline readiness scoring for Restaurant Operation Digital Advisor.

Input: JSON from a file path argument or stdin.
Output: JSON with score, stage, dimensions, risk tags, and next focus.
"""

from __future__ import annotations

import json
import sys
from typing import Any


ISSUE_WEIGHTS = {
    "memory_or_chat": ("store_execution", 4),
    "low_system_adoption": ("store_execution", 4),
    "after_the_fact": ("responsibility", 3),
    "training_slow": ("responsibility", 3),
    "ordering_receiving_mismatch": ("supply_inventory", 5),
    "inventory_untrusted": ("supply_inventory", 6),
    "waste_transfer_incomplete": ("supply_inventory", 4),
    "finance_late": ("finance_reconciliation", 5),
    "manual_reconciliation": ("finance_reconciliation", 5),
    "isolated_systems": ("system_data_handoff", 5),
    "manual_exports": ("system_data_handoff", 4),
    "unclear_permissions": ("responsibility", 4),
    "vendor_demo_gap": ("system_data_handoff", 3),
    "loyalty_disconnected": ("customer_loyalty", 4),
    "delivery_chaos": ("order_channel_flow", 4),
}

DIMENSION_NAMES = {
    "store_execution": "Store execution",
    "order_channel_flow": "Order and channel flow",
    "supply_inventory": "Supply and inventory loop",
    "finance_reconciliation": "Finance and reconciliation",
    "customer_loyalty": "Customer and loyalty operations",
    "system_data_handoff": "System fit and data handoff",
    "responsibility": "Responsibility and organization",
}

BASE_OFFSETS = {
    "store_execution": 8,
    "order_channel_flow": 7,
    "supply_inventory": 10,
    "finance_reconciliation": 10,
    "customer_loyalty": 3,
    "system_data_handoff": 9,
    "responsibility": 8,
}


def risk_level_for(score: int) -> str:
    if score >= 75:
        return "low"
    if score >= 60:
        return "medium"
    if score >= 45:
        return "medium_high"
    if score >= 30:
        return "high"
    return "critical"


def number(data: dict[str, Any], key: str, default: float = 0) -> float:
    try:
        return float(data.get(key, default) or default)
    except (TypeError, ValueError):
        return default


def list_value(data: dict[str, Any], key: str) -> list[str]:
    value = data.get(key, [])
    if isinstance(value, list):
        return [str(item) for item in value]
    if isinstance(value, str) and value:
        return [item.strip() for item in value.split(",") if item.strip()]
    return []


def stage_for(score: int) -> str:
    if score >= 80:
        return "Ready for limited system selection, but test exception scenarios."
    if score >= 65:
        return "Suitable for a pilot workflow before broad rollout."
    if score >= 50:
        return "Clarify workflow and responsibility before buying heavy systems."
    return "Direct system replacement is risky; fix operating basics first."


def score_assessment(data: dict[str, Any]) -> dict[str, Any]:
    store_count = number(data, "store_count", number(data, "storeCount", 1))
    system_count = number(data, "system_count", number(data, "systemCount", 0))
    sku_count = number(data, "sku_count", number(data, "skuCount", 0))
    daily_orders = number(data, "daily_orders", number(data, "dailyOrders", 0))
    labor_pressure = str(data.get("labor_pressure", data.get("laborPressure", "medium"))).lower()
    operating_model = str(data.get("operating_model", data.get("operatingModel", ""))).lower()
    issues = list_value(data, "issues")

    raw_score = 82
    raw_score -= min(18, max(0, store_count - 1) * 2)
    raw_score -= min(14, system_count * 2)
    raw_score -= 10 if sku_count > 160 else 6 if sku_count > 90 else 2 if sku_count > 0 else 0
    raw_score -= 10 if daily_orders > 800 else 6 if daily_orders > 350 else 2 if daily_orders > 0 else 0
    raw_score -= 10 if labor_pressure == "high" else 6 if labor_pressure in {"medium", "mid"} else 2
    raw_score -= min(14, max(0, len(issues) - 5) * 2)
    if operating_model in {"established_chain", "franchise", "multi_region", "multi-brand", "multi_brand"}:
        raw_score -= 4

    dimension_penalties = {key: 0 for key in DIMENSION_NAMES}
    unknown_issues: list[str] = []
    for issue in issues:
        if issue in ISSUE_WEIGHTS:
            dimension, weight = ISSUE_WEIGHTS[issue]
            dimension_penalties[dimension] += weight
        else:
            unknown_issues.append(issue)

    score = int(max(30, min(88, round(raw_score))))
    dimensions = []
    dimension_base = max(score, 42)
    for key, name in DIMENSION_NAMES.items():
        dim_score = max(24, min(88, dimension_base - BASE_OFFSETS[key] - dimension_penalties[key]))
        evidence = "issue_tag" if dimension_penalties[key] > 0 else "not_enough_specific_evidence"
        dimensions.append(
            {
                "key": key,
                "name": name,
                "score": dim_score,
                "risk_level": risk_level_for(dim_score),
                "evidence": evidence,
            }
        )

    dimensions_sorted = sorted(dimensions, key=lambda item: item["score"])
    next_focus = [item["name"] for item in dimensions_sorted[:3]]
    risk_tags = [key for key, value in sorted(dimension_penalties.items(), key=lambda item: item[1], reverse=True) if value > 0]

    return {
        "score": score,
        "stage": stage_for(score),
        "dimensions": dimensions,
        "risk_tags": risk_tags,
        "next_focus": next_focus,
        "unknown_issues": unknown_issues,
    }


def main() -> int:
    if len(sys.argv) > 2:
        print("Usage: score_assessment.py [assessment.json]", file=sys.stderr)
        return 2

    if len(sys.argv) == 2:
        with open(sys.argv[1], "r", encoding="utf-8") as handle:
            data = json.load(handle)
    else:
        data = json.load(sys.stdin)

    result = score_assessment(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
