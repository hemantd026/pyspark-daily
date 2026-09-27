"""Test data for Day 001. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    events = spark.createDataFrame(
        [
            ("E1", "u1", "2024-02-01 10:00:00", "/home"),
            ("E2", "u1", "2024-02-01 10:01:00", "/cart"),
            ("E1", "u1", "2024-02-01 10:00:05", "/home"),      # dup of E1, later
            ("E3", "u2", "2024-02-01 10:02:00", "/home"),
            ("E2", "u1", "2024-02-01 10:00:59", "/cart"),      # dup of E2, earlier
            ("E4", "u2", "2024-02-01 10:03:00", "/checkout"),
            ("E4", "u2", "2024-02-01 10:03:00", "/checkout"),  # exact dup
        ],
        ["event_id", "user_id", "event_time", "page"],
    )
    return {"events": events}
