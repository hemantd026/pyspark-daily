"""Scaffold a new challenge day.

Usage: python engine/new_day.py "dedup events"
Creates challenges/day-008-dedup-events/ with README, data.py,
solution.py (stub) and test_solution.py templates.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENGINE = os.path.dirname(os.path.abspath(__file__))

README_TMPL = """# Day {num}: {title}

⭐ Difficulty: {difficulty} · ⏱️ ~{minutes} min

## Story

TODO: one-paragraph scenario. Why does this task exist in a real pipeline?

## Your task

TODO: what must `solve(spark, inputs)` return? Be precise about column names
and types — the tests check them.

- Input tables (see `data.py`): TODO
- Output: TODO

## Rules

- ...

## Hints

<details>
<summary>Hint 1</summary>
TODO
</details>

## Verify

```bash
python engine/check.py day-{num}
```
"""

DATA_TMPL = '''"""Test data for Day {num}. `load(spark)` returns {{name: DataFrame}}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    # TODO: build your input DataFrames here. Keep them small and deterministic.
    raise NotImplementedError("write the test data")
'''

SOLUTION_TMPL = '''"""Day {num} solution — implement solve() below."""


def solve(spark, inputs):
    """TODO: implement.

    Args:
        spark: the SparkSession (from the test fixture).
        inputs: dict of DataFrames from data.load(spark).

    Returns:
        TODO: DataFrame (or dict of DataFrames).
    """
    raise NotImplementedError("Your turn!")
'''

TEST_TMPL = '''"""Tests for Day {num}. Run: python engine/check.py day-{num}"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "engine"))
from harness import load_day  # noqa: E402

DAY_DIR = os.path.dirname(os.path.abspath(__file__))
data, solution = load_day(DAY_DIR)


@pytest.fixture
def result(spark):
    try:
        return solution.solve(spark, data.load(spark))
    except NotImplementedError:
        pytest.skip("solution not implemented yet")


def test_placeholder(result):
    # TODO: replace with real assertions
    assert result is not None
'''


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python engine/new_day.py "short slug"')
    slug = re.sub(r"[^a-z0-9]+", "-", sys.argv[1].lower()).strip("-")
    cdir = os.path.join(ROOT, "challenges")
    existing = sorted(d for d in os.listdir(cdir)
                      if re.match(r"day-\d+", d)) if os.path.isdir(cdir) else []
    num = f"{(int(existing[-1].split('-')[1]) + 1) if existing else 0:03d}"
    day_dir = os.path.join(cdir, f"day-{num}-{slug}")
    os.makedirs(day_dir, exist_ok=False)
    title = sys.argv[1].strip().capitalize()
    files = {
        "README.md": README_TMPL.format(num=num, title=title,
                                        difficulty="⭐", minutes=30),
        "data.py": DATA_TMPL.format(num=num),
        "solution.py": SOLUTION_TMPL.format(num=num),
        "test_solution.py": TEST_TMPL.format(num=num),
    }
    for name, content in files.items():
        with open(os.path.join(day_dir, name), "w") as f:
            f.write(content)
    print(f"Created {day_dir}")
    print("Next: fill in README.md, data.py and test_solution.py, then add a row to PROGRESS.md.")


if __name__ == "__main__":
    main()
