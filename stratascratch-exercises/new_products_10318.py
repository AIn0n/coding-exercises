# Import your libraries
import pandas as pd

yearly_products = car_launches.groupby(by=["company_name", "year"], as_index=False).agg(
    count=("product_name", "count")
)
per_year = yearly_products.pivot(
    index="company_name", columns="year", values="count"
).reset_index()
per_year["diff"] = per_year[2020] - per_year[2019]
per_year[["company_name", "diff"]].rename(columns={"diff": "net_new_products"})
