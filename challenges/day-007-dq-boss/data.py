"""Test data for Day 007. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    users = spark.createDataFrame(
        [
            ("U1", "amy@example.com", 30, "2024-01-01", "2024-06-01"),
            ("U2", "bob-at-example.com", 25, "2024-01-02", "2024-06-02"),
            ("U3", "cid@example.com", -5, "2024-01-03", "2024-06-03"),
            ("U4", None, 40, "2024-01-04", "2024-06-04"),
            ("U1", "amy@example.com", 30, "2024-01-01", "2024-06-01"),
            ("U5", "dee@example.com", 22, "2024-05-01", "2024-04-01"),
        ],
        ["user_id", "email", "age", "signup_date", "last_login"],
    )
    return {"users": users}
