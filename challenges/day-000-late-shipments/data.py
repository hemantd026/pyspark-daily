"""Test data for Day 000. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    orders = spark.createDataFrame(
        [
            ("O1", "amy", 120.0, "2024-01-01", "2024-01-03"),  # 2 days — ok
            ("O2", "bob", 75.5, "2024-01-02", "2024-01-10"),   # 8 days — LATE
            ("O3", "amy", 40.0, "2024-01-03", "2024-01-08"),   # 5 days — ok
            ("O4", "cid", 200.0, "2024-01-04", "2024-01-12"),  # 8 days — LATE
            ("O5", "bob", 15.0, "2024-01-05", "2024-01-06"),   # 1 day — ok
            ("O6", "dee", 99.9, "2024-01-06", "2024-01-11"),   # 5 days — ok
        ],
        ["order_id", "customer", "amount", "ship_date", "delivery_date"],
    )
    return {"orders": orders}
