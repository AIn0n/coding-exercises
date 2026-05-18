# Import your libraries
import pandas as pd
from datetime import datetime

# Start writing code
customers.head()

orders.head()

orders.drop(columns=["order_details", "id"], inplace=True)

start_date = datetime(year=2019, month=2, day=1)
end_date = datetime(year=2019, month=5, day=1)

orders = orders[orders["order_date"].between(start_date, end_date, "both")]

orders = orders.merge(
    customers[["id", "first_name"]], left_on="cust_id", right_on="id", how="left"
).drop(columns=["id", "cust_id"])

# Let's start with the day

daily_total = (
    orders.groupby(by=["first_name", "order_date"])
    .agg(max_cost=("total_order_cost", "sum"))
    .reset_index()
)

daily_maxes = (
    daily_total.groupby(by="order_date").agg(max_cost=("max_cost", "max")).reset_index()
)

daily_total.merge(daily_maxes, on=["order_date", "max_cost"], how="inner")
