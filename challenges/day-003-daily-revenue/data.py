"""Test data for Day 003. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    orders = spark.createDataFrame(
        [
            ("A1", "books", 2, 15.0, "2024-03-01 09:00:00", "done"),
            ("A2", "books", 1, 15.0, "2024-03-01 15:00:00", "done"),
            ("A3", "toys", 1, 40.0, "2024-03-01 16:00:00", "cancelled"),
            ("A4", "toys", 3, 10.0, "2024-03-02 10:00:00", "done"),
            ("A5", "books", 1, 15.0, "2024-03-02 11:00:00", "done"),
            ("A6", "toys", 2, 10.0, "2024-03-02 12:00:00", "done"),
        ],
        ["order_id", "category", "qty", "unit_price", "order_ts", "status"],
    )
    return {"orders": orders}
