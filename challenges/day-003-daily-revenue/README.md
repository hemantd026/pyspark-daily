# Day 003: Daily revenue ⭐⭐

⏱️ ~20 min

## Story

The BI team wants a daily revenue table: one row per day per category. The
raw orders table has quantities, unit prices, timestamps — and cancelled
orders that must not count. Classic aggregation day.

## Your task

Implement `solve(spark, inputs)` returning a DataFrame with:

- `day` (date) — calendar date of the order
- `category` (string)
- `revenue` (double) — `sum(qty * unit_price)` for that day & category
- Only orders with `status = 'done'` count

Sort by `day`, then `category`.

Input (see `data.py`):
`orders(order_id, category, qty, unit_price, order_ts, status)` —
`order_ts` is a string (`yyyy-MM-dd HH:mm:ss`).

## Rules

- Compute revenue per order line first, then aggregate. Don't average averages.

## Hints

<details>
<summary>Hint 1</summary>
<code>to_date(to_timestamp("order_ts"))</code> gives you the calendar day.
</details>

## Verify

```bash
python engine/check.py day-003
```
