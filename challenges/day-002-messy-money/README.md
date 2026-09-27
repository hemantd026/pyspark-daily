# Day 002: Messy money ⭐⭐

⏱️ ~25 min

## Story

Finance exported transactions from three different systems into one CSV, and
every system formats money and dates its own way. Amounts look like
`"$1,234.56"`, `"($45.00)"` (parentheses mean negative — accounting style),
or `"N/A"`. Dates are `yyyy-MM-dd`, `dd/MM/yyyy`, `MMM d, yyyy`, even
`yyyy/MM/dd`. Your job: one clean table.

## Your task

Implement `solve(spark, inputs)` returning a DataFrame with:

- `txn_id` (string)
- `amount` (double) — `"$1,234.56"` → `1234.56`, `"($45.00)"` → `-45.0`,
  `"N/A"` → `NULL`
- `txn_date` (date) — parse all four formats above

Sort by `txn_id` ascending.

Input (see `data.py`): `transactions(txn_id, amount_str, date_str)` — all strings.

## Rules

- Malformed values must become `NULL`, never crash the job. (Spark's ANSI
  mode throws on bad casts — plan for it.)
- No Python UDFs — use Spark SQL functions.

## Hints

<details>
<summary>Hint 1</summary>
<code>regexp_replace</code> can strip <code>$</code>, commas and parentheses in
one go. Detect the accounting-style negative with
<code>F.col("amount_str").startswith("(")</code> and multiply by -1. There is
no Python-side <code>F.try_cast</code> — use it through Spark SQL:
<code>F.expr("try_cast(regexp_replace(amount_str, '[$,()]', '') as double)")</code>,
which returns NULL on garbage instead of throwing.
</details>
<details>
<summary>Hint 2</summary>
<code>coalesce(try_to_date(col, "yyyy-MM-dd"), try_to_date(col, "dd/MM/yyyy"), ...)</code>
tries each format in order. (<code>try_to_date</code> exists in Spark 4.x; on
Spark 3.x use <code>to_date</code> with ANSI off.)
</details>

## Verify

```bash
python engine/check.py day-002
```
