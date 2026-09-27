"""Tests for Day 000. Run: python engine/check.py day-000"""
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


def test_schema(result):
    assert [f.name for f in result.schema.fields] == [
        "order_id", "customer", "days_late",
    ]


def test_finds_exactly_the_late_orders(result):
    rows = [(r.order_id, r.customer, r.days_late) for r in result.collect()]
    assert rows == [("O2", "bob", 8), ("O4", "cid", 8)]
