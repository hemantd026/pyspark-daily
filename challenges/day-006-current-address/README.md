# Day 006: Where do they live now? ⭐⭐⭐

⏱️ ~25 min

## Story

Customer addresses change over time, and the CRM keeps full history: every
address has a `valid_from` date and a `valid_to` date (`NULL` means "still
current"). The shipping team needs exactly one row per customer — the current
address. Sounds easy until you meet customer C3, who has no `NULL` row at all.

## Your task

Implement `solve(spark, inputs)` returning a DataFrame with:

- `customer_id` (string), `address` (string) — the customer's **current**
  address
- Current = the row with `valid_to IS NULL`; if a customer has no such row,
  take the row with the **latest `valid_from`**
- One row per customer. Sort by `customer_id`.

Input (see `data.py`):
`history(customer_id, address, valid_from, valid_to)` — dates are ISO strings.

## Rules

- Handle both cases (NULL `valid_to` present / absent) in one query.

## Hints

<details>
<summary>Hint 1</summary>
Order each customer's rows by "is current" first, then <code>valid_from</code>
descending: <code>orderBy(F.col("valid_to").isNull().desc(), F.col("valid_from").desc())</code>
inside a window partitioned by customer — then keep row 1.
</details>

## Verify

```bash
python engine/check.py day-006
```
