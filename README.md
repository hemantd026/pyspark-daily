# 🥋 PySpark Daily Dojo

One small PySpark challenge every day. Realistic data-engineering scenarios —
dedup, messy types, joins, window functions, slowly changing dimensions —
not abstract puzzles.

## How to play

1. Open today's challenge: `challenges/day-001-double-click/README.md`
2. Read the story and the task. Look at `data.py` to see the input shape.
3. Write your solution in `solution.py` — implement `solve(spark, inputs)`.
4. Verify: `python engine/check.py day-001`
5. When tests pass, commit: `git add challenges/day-001-double-click && git commit -m "Day 001: ..."`
6. Come back tomorrow.

Day 000 is a fully worked example — start there.

## Rules

- **No peeking at solutions.** The tests are the judge.
- **One day, one commit.** That's what keeps the habit (and the graph) honest.
- A challenge is done only when `check.py` passes.
- Stuck for >30 minutes? Read the hints in the challenge README, then move on —
  come back to it on a review day.

## The green squares

Every committed solution lands on your contribution graph — that's GitHub
recognizing real work. The graph is a side effect, not the target: what matters
is that in 30 days you can dedup, clean, join, window and aggregate in your
sleep. Don't game it (empty commits, backdating) — it only fools you.

## Setup

You need Python 3.9+ and Java 8+ (`java -version`).

```bash
pip install -r requirements.txt
python engine/check.py day-000   # should pass — it's the worked example
```

## Adding new challenges

```bash
python engine/new_day.py "short slug"   # scaffolds challenges/day-008-<slug>/
```

Then fill in `README.md`, `data.py` and `test_solution.py`.
`PROGRESS.md` tracks the journey.
