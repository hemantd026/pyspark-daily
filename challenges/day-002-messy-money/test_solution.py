"""Tests for Day 002. Run: python engine/check.py day-002"""
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
    assert fields == {"txn_id": "string", "amount": "double",
                      "txn_date": "date"}


def test_amounts(result):
    rows = {r.txn_id: r.amount for r in result.collect()}
    assert rows["T1"] == pytest.approx(1234.56)
    assert rows["T2"] == pytest.approx(-45.0)
    assert rows["T3"] == pytest.approx(0.99)
    assert rows["T4"] is None
    assert rows["T5"] == pytest.approx(2000.0)


def test_dates(result):
    rows = {r.txn_id: r.txn_date.isoformat() for r in result.collect()}
    assert rows == {
        "T1": "2024-01-15",
        "T2": "2024-01-15",
        "T3": "2024-01-16",
        "T4": "2024-01-16",
        "T5": "2024-01-17",
    }


def test_sorted(result):
    assert [r.txn_id for r in result.collect()] == ["T1", "T2", "T3", "T4", "T5"]
