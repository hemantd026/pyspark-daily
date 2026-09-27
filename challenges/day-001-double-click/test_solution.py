"""Tests for Day 001. Run: python engine/check.py day-001"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "engine"))
from harness import load_day  # noqa: E402

DAY_DIR = os.path.dirname(os.path.abspath(__file__))
data, solution = load_day(DAY_DIR)

EXPECTED_TIMES = {
    "E1": "2024-02-01 10:00:05",
    "E2": "2024-02-01 10:01:00",
    "E3": "2024-02-01 10:02:00",
    "E4": "2024-02-01 10:03:00",
}


@pytest.fixture
def result(spark):
    try:
        return solution.solve(spark, data.load(spark))
    except NotImplementedError:
        pytest.skip("solution not implemented yet")


def test_one_row_per_event(result):
    ids = [r.event_id for r in result.collect()]
    assert len(ids) == 4
    assert sorted(ids) == ["E1", "E2", "E3", "E4"]


def test_keeps_latest_timestamp(result):
    rows = {r.event_id: r.event_time.strftime("%Y-%m-%d %H:%M:%S")
            for r in result.collect()}
    assert rows == EXPECTED_TIMES


def test_schema(result):
    assert [f.name for f in result.schema.fields] == [
        "event_id", "user_id", "event_time", "page",
    ]
    assert result.schema["event_time"].dataType.simpleString() == "timestamp"


def test_sorted(result):
    ids = [r.event_id for r in result.collect()]
    assert ids == sorted(ids)
