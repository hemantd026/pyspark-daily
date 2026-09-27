# Day 007: BOSS — Data-quality report ⭐⭐⭐⭐

⏱️ ~35 min · Boss level: combines everything from this week.

## Story

It's your first week on the data platform team, and someone hands you the
`users` table "as-is from production". Your task: run a data-quality audit
and hand back a report of what you found. This is exactly what real DQ tools
(like the one in `medicare-dq`) do every night.

## Your task

Implement `solve(spark, inputs)` returning a DataFrame with:

- `check_name` (string), `violations` (int/long) — one row per check
- Exactly these 5 checks, in this order:
  1. `null_email` — rows where `email` is NULL
  2. `dup_user_id` — number of **distinct** `user_id`s that appear more than once
  3. `bad_email` — non-null emails that don't match `.+@.+\..+`
  4. `bad_age` — `age` outside `[0, 120]` (NULL age would count too — there is none)
  5. `login_before_signup` — rows where `last_login < signup_date`
- `violations` is the count of offending rows (or offending ids for #2)

Dates are ISO strings (`yyyy-MM-dd`), so string comparison works — or parse
them, your call.

Input (see `data.py`): `users(user_id, email, age, signup_date, last_login)`.

## Rules

- One DataFrame out, built from the five counts. `union` is your friend —
  or build it from a list of rows.
- No hardcoding the answers: the checks must compute from the data.

## Hints

<details>
<summary>Hint 1</summary>
Each check is a <code>filter(...).count()</code>. Collect the five
<code>(name, count)</code> pairs and <code>spark.createDataFrame</code> them.
</details>
<details>
<summary>Hint 2</summary>
For the email check in Spark 4.x, wrap the pattern: <code>F.rlike("email", F.lit(r".+@.+\..+"))</code> —
a plain string pattern is treated as a column name.
</details>

## Verify

```bash
python engine/check.py day-007
```

Beat the boss and Week 1 is yours. 🏆
