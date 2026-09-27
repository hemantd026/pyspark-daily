"""Test data for Day 004. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    customers = spark.createDataFrame(
        [("C1", "amy"), ("C2", "bob"), ("C3", "cid")],
        ["customer_id", "name"],
    )
    orders = spark.createDataFrame(
        [
            ("O1", "C1", 50.0),
            ("O2", "C2", 20.0),
            ("O3", "C9", 99.0),   # orphan — no such customer
            ("O4", "C1", 10.0),
            ("O5", "C7", 5.0),    # orphan — no such customer
        ],
        ["order_id", "customer_id", "amount"],
    )
    return {"customers": customers, "orders": orders}
