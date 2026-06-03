# Integration and Data Handoff Checklist

Use this when the user says systems exist but data does not match.

## Map the Handoff

For each critical data object, identify:

- source system,
- downstream system,
- owner,
- timing,
- correction path,
- audit trail,
- report where the number is used.

## Critical Data Objects

- order
- payment
- refund / void
- discount / coupon
- delivery order status
- inventory receipt
- transfer
- waste
- stock count
- recipe or bill of materials
- supplier invoice
- member profile
- stored value or loyalty balance
- labor shift
- accounting entry

## Common Breakpoints

- online orders enter POS but not inventory,
- delivery cancellations do not reverse kitchen or inventory data,
- refunds affect payment but not revenue reporting,
- inventory transfers happen in chat but not in system,
- accounting receives summaries without transaction-level explanations,
- loyalty data is separate from store execution data,
- manual exports become the real integration layer.

## Output

Produce a handoff table with:

```text
Data object | Source | Destination | Owner | Failure scenario | Fix path | Check
```

