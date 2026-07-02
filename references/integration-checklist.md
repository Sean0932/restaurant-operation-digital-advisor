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

Start by identifying the system of record. If every platform keeps its own number, ask which number is allowed to become the final business truth.

Use this chain for restaurant data-fragmentation problems:

```text
order -> payment -> discount/refund -> inventory deduction -> waste/transfer -> member balance -> accounting entry -> management report
```

For each arrow, ask:

- Is the handoff automatic, manual export, manual entry, or not connected?
- What is the timing: real time, end of day, weekly, month-end, or only when someone remembers?
- Who owns correction when two systems disagree?
- Which report does the owner use to make decisions?
- Can one real transaction be traced from source order to accounting entry?

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
- each platform owns a separate sales total and nobody defines the final source of truth,
- delivery cancellations do not reverse kitchen or inventory data,
- refunds affect payment but not revenue reporting,
- inventory transfers happen in chat but not in system,
- accounting receives summaries without transaction-level explanations,
- loyalty data is separate from store execution data,
- membership recharge, consumption, refund, and franchise settlement use different ledgers,
- manual exports become the real integration layer.

## Output

Produce a handoff table with:

```text
Data object | Source | Destination | Owner | Failure scenario | Fix path | Check
```

Also produce a source-of-truth table:

```text
Metric | Current sources | Final source of truth | Conflict rule | Owner
Sales amount | POS / delivery platform / accounting | TBD | TBD | TBD
Inventory quantity | inventory system / store count / central kitchen | TBD | TBD | TBD
Member balance | CRM / POS / mini program | TBD | TBD | TBD
```

If the user asks whether to integrate or replace systems, do not start from vendor categories. Start from the missing source-of-truth decisions and the broken handoff points.
