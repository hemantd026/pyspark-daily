"""Tests for Day 006. Run: python engine/check.py day-006"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "engine"))
from harness import load_day  # noqa: E402

DAY_DIR = os.path.dirname(os.path.abspath(__file__))
data, solution = load_day(DAY_DIR)

EXPECTED = {"C1": "addr B", "C2": "addr Y", "C3": "addr N"}


@pytest.fixture
def result(spark):
    try:
        return solution.solve(spark, data.load(spark))
    except NotImplementedError:
        pytest.skip("solution not implemented yet")


def test_schema(result):
    assert [f.name for f in result.schema.fields] == [
        "customer_id", "address",
    ]


def test_current_addresses(result):
    rows = {r.customer_id: r.address for r in result.collect()}
    assert rows == EXPECTED


def test_one_row_per_customer(result):
    ids = [r.customer_id for r in result.collect()]
    assert sorted(ids) == ["C1", "C2", "C3"]
