"""Tests for Day 007. Run: python engine/check.py day-007"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "engine"))
from harness import load_day  # noqa: E402

DAY_DIR = os.path.dirname(os.path.abspath(__file__))
data, solution = load_day(DAY_DIR)

EXPECTED = [
    ("null_email", 1),
    ("dup_user_id", 1),
    ("bad_email", 1),
    ("bad_age", 1),
    ("login_before_signup", 1),
]


@pytest.fixture
def result(spark):
    try:
        return solution.solve(spark, data.load(spark))
    except NotImplementedError:
        pytest.skip("solution not implemented yet")


def test_schema(result):
    assert [f.name for f in result.schema.fields] == [
        "check_name", "violations",
    ]


def test_report_values(result):
    rows = [(r.check_name, r.violations) for r in result.collect()]
    assert rows == EXPECTED
