"""Test data for Day 002. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    transactions = spark.createDataFrame(
        [
            ("T1", "$1,234.56", "2024-01-15"),
            ("T2", "($45.00)", "15/01/2024"),     # -45.00, 15 Jan 2024
            ("T3", "$0.99", "Jan 16, 2024"),
            ("T4", "N/A", "2024-01-16"),          # null amount
            ("T5", "$2,000", "2024/01/17"),
        ],
        ["txn_id", "amount_str", "date_str"],
    )
    return {"transactions": transactions}
