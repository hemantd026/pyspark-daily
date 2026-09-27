"""Day 000 solution (worked example)."""
from pyspark.sql import functions as F


def solve(spark, inputs):
    orders = inputs["orders"]
    days_late = F.datediff(
        F.to_date("delivery_date"), F.to_date("ship_date")
    )
    return (
        orders.withColumn("days_late", days_late)
        .filter(F.col("days_late") > 5)
        .select("order_id", "customer", "days_late")
        .orderBy("order_id")
    )
