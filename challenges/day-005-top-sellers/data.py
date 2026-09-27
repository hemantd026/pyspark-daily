"""Test data for Day 005. `load(spark)` returns {name: DataFrame}."""
from pyspark.sql import SparkSession


def load(spark: SparkSession) -> dict:
    sales = spark.createDataFrame(
        [
            ("S1", "east", "ana", 100.0),
            ("S2", "east", "bob", 200.0),
            ("S3", "east", "cid", 150.0),
            ("S4", "east", "dan", 50.0),
            ("S9", "east", "bob", 25.0),    # bob's total: 225
            ("S5", "west", "eli", 300.0),
            ("S6", "west", "fay", 250.0),
            ("S7", "west", "gus", 250.0),   # tie with fay -> name breaks it
            ("S8", "west", "hal", 100.0),
        ],
        ["sale_id", "region", "salesperson", "amount"],
    )
    return {"sales": sales}
