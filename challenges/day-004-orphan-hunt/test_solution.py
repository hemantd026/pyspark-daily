"""Tests for Day 004. Run: python engine/check.py day-004"""
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


def test_returns_both_tables(result):
    assert set(result.keys()) == {"orphan_orders", "inactive_customers"}


def test_orphan_orders(result):
    df = result["orphan_orders"]
    assert [f.name for f in df.schema.fields] == ["order_id", "customer_id"]
    rows = [(r.order_id, r.customer_id) for r in df.collect()]
    assert rows == [("O3", "C9"), ("O5", "C7")]


def test_inactive_customers(result):
    df = result["inactive_customers"]
    assert [f.name for f in df.schema.fields] == ["customer_id", "name"]
    rows = [(r.customer_id, r.name) for r in df.collect()]
    assert rows == [("C3", "cid")]
