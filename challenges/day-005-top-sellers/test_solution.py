"""Tests for Day 005. Run: python engine/check.py day-005"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "engine"))
from harness import load_day  # noqa: E402

DAY_DIR = os.path.dirname(os.path.abspath(__file__))
data, solution = load_day(DAY_DIR)

# (region, salesperson) -> (total, rank)
EXPECTED = {
    ("east", "bob"): (225.0, 1),
    ("east", "cid"): (150.0, 2),
    ("east", "ana"): (100.0, 3),
    ("west", "eli"): (300.0, 1),
    ("west", "fay"): (250.0, 2),
    ("west", "gus"): (250.0, 3),
}


@pytest.fixture
def result(spark):
    try:
        return solution.solve(spark, data.load(spark))
    except NotImplementedError:
        pytest.skip("solution not implemented yet")


def test_schema(result):
    fields = {f.name: f.dataType.simpleString() for f in result.schema.fields}
    assert fields == {"region": "string", "salesperson": "string",
                      "total": "double", "rank": "int"}


def test_top3_per_region(result):
    rows = {(r.region, r.salesperson): (r.total, r.rank)
            for r in result.collect()}
    assert len(rows) == 6
    for key, (total, rank) in EXPECTED.items():
        assert rows[key][0] == pytest.approx(total), key
        assert rows[key][1] == rank, key


def test_sorted(result):
    keys = [(r.region, r.rank) for r in result.collect()]
    assert keys == sorted(keys)
