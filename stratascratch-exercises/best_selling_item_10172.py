# Import your libraries
import pandas as pd

# Start writing code
online_retail.head()

df = online_retail[~online_retail["invoiceno"].str.startswith("C")][
    ["description", "quantity", "unitprice", "invoicedate"]
]

df["month"] = df.invoicedate.dt.month

df["total_paid"] = df.quantity * df.unitprice

summed = df.groupby(by=["month", "description"], as_index=False).agg(
    total_paid=("total_paid", "sum")
)

summed[summed.groupby("month")["total_paid"].transform("max") == summed["total_paid"]]
