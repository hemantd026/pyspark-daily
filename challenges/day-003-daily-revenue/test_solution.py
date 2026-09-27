"""Tests for Day 003. Run: python engine/check.py day-003"""
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
    fields = {f.name: f.dataType.simpleString() for f in result.schema.fields}
    assert fields == {"day": "date", "category": "string",
                      "revenue": "double"}


def test_values(result):
    rows = {(r.day.isoformat(), r.category): r.revenue for r in result.collect()}
    assert rows == {
        ("2024-03-01", "books"): pytest.approx(45.0),
        ("2024-03-02", "books"): pytest.approx(15.0),
        ("2024-03-02", "toys"): pytest.approx(50.0),
    }


def test_sorted(result):
    keys = [(r.day.isoformat(), r.category) for r in result.collect()]
    assert keys == sorted(keys)
