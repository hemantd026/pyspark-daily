# Day 004: Orphan hunt ⭐⭐

⏱️ ~20 min

## Story

Two tables, no foreign keys — welcome to the real world. Some orders reference
customers that don't exist (bad ETL), and some customers have never ordered
(churn-risk list for marketing). Find both groups.

## Your task

Implement `solve(spark, inputs)` returning a **dict of two DataFrames**:

- `"orphan_orders"`: orders whose `customer_id` has no match in customers.
  Columns: `order_id`, `customer_id`. Sort by `order_id`.
- `"inactive_customers"`: customers with zero orders.
  Columns: `customer_id`, `name`. Sort by `customer_id`.

Input (see `data.py`):
`customers(customer_id, name)`, `orders(order_id, customer_id, amount)`.

## Rules

- Use joins, not `collect()` + Python `in` checks. Think about which join
  type finds "rows with no match".

## Hints

<details>
<summary>Hint 1</summary>
A <code>left_anti</code> join returns rows from the left side with no match on
the right. You need it twice — once in each direction.
</details>

## Verify

```bash
python engine/check.py day-004
```
