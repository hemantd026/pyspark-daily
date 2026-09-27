# Day 000: Late shipments (worked example) ⭐

⏱️ ~15 min · This one is fully solved — read it to learn the format.

## Story

You own the shipping dashboard for an online store. Customer support keeps
getting "where is my order?" tickets, and you suspect some orders are
consistently delivered late. Time to find them with Spark.

## Your task

Implement `solve(spark, inputs)` so it returns a DataFrame of **late orders**:

- An order is *late* if `delivery_date` is **more than 5 days** after `ship_date`.
- Columns: `order_id` (string), `customer` (string), `days_late` (int).
- Sort by `order_id` ascending.

Input (see `data.py`): `orders(order_id, customer, amount, ship_date, delivery_date)` —
dates are ISO strings (`yyyy-MM-dd`).

## Rules

- Do it with DataFrame operations (no RDDs, no `collect()`-then-Python).
- Exactly 5 days is on time — only *more than* 5 counts.

## How this was solved

See `solution.py` — `datediff` gives the day difference, `filter` keeps the
late ones, `select` + `orderBy` shape the result. The test then checks the
exact rows.

## Verify

```bash
python engine/check.py day-000
```
