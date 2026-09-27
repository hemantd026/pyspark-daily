# Day 001: Double-click ⭐

⏱️ ~20 min

## Story

Your clickstream pipeline has a bug: impatient users double-click, and every
click lands in the event log twice (sometimes with a slightly different
timestamp). Downstream dashboards count inflated page views. Your job: produce
a clean event log with exactly one row per event.

## Your task

Implement `solve(spark, inputs)` returning a DataFrame with **one row per
`event_id`** — keep the row with the **latest `event_time`** when duplicates
exist.

- Columns: `event_id`, `user_id`, `event_time` (timestamp), `page`.
- Sort by `event_id` ascending.
- `event_time` arrives as a string (`yyyy-MM-dd HH:mm:ss`) — return it as a
  proper timestamp.

Input (see `data.py`): `events(event_id, user_id, event_time, page)`.

## Rules

- No `collect()`-then-dedup in Python — stay in Spark.
- Exact-duplicate rows (all columns equal) must also collapse to one.

## Hints

<details>
<summary>Hint 1</summary>
A window partitioned by <code>event_id</code>, ordered by <code>event_time</code>
descending, lets you number each event's rows — then keep row number 1.
</details>
<details>
<summary>Hint 2</summary>
<code>F.row_number().over(Window.partitionBy("event_id").orderBy(F.col("event_time").desc()))</code>
</details>

## Verify

```bash
python engine/check.py day-001
```
