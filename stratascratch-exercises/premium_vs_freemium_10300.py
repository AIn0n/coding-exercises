import pandas as pd

# Start writing code
ms_user_dimension.head()

accounts = ms_user_dimension.merge(ms_acc_dimension, on="acc_id")
downloads = ms_download_facts.merge(
    accounts[["user_id", "paying_customer"]], on="user_id"
)
pivoted = (
    downloads.pivot_table(
        index="date", columns="paying_customer", values="downloads", aggfunc="sum"
    )
    .reset_index()
    .rename(columns={"no": "non_paying", "yes": "paying"})
)
pivoted[pivoted["non_paying"] > pivoted["paying"]]
