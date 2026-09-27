"""Test data for Day 006. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    history = spark.createDataFrame(
        [
            ("C1", "addr A", "2020-01-01", "2022-06-01"),
            ("C1", "addr B", "2022-06-01", None),        # current
            ("C2", "addr X", "2021-03-01", "2023-01-01"),
            ("C2", "addr Y", "2023-01-01", None),        # current
            ("C3", "addr M", "2019-05-01", "2020-05-01"),
            ("C3", "addr N", "2020-05-01", "2021-05-01"),  # no NULL row!
        ],
        ["customer_id", "address", "valid_from", "valid_to"],
    )
    return {"history": history}
