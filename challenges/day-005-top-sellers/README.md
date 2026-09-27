# Day 005: Top sellers ⭐⭐⭐

⏱️ ~25 min

## Story

Sales leadership wants a leaderboard: the top 3 salespeople in each region by
total sales. Ties are broken alphabetically by name (so the ranking is
deterministic — dashboards hate ties).

## Your task

Implement `solve(spark, inputs)` returning a DataFrame with:

- `region` (string), `salesperson` (string), `total` (double), `rank` (int)
- One row per salesperson, but only the **top 3 per region** by `total`
  descending; ties broken by `salesperson` ascending
- `rank` is 1-based within each region

Sort by `region`, then `rank`.

Input (see `data.py`): `sales(sale_id, region, salesperson, amount)`.

## Rules

- Aggregate first (a salesperson may have multiple sales), then rank.
- Window functions are the intended tool. `rank()` vs `dense_rank()` vs
  `row_number()` — pick the one that guarantees exactly 3 rows per region.

## Hints

<details>
<summary>Hint 1</summary>
<code>row_number().over(Window.partitionBy("region").orderBy(F.col("total").desc(), "salesperson"))</code>
numbers each region's salespeople deterministically — then filter to rank ≤ 3.
</details>

## Verify

```bash
python engine/check.py day-005
```
