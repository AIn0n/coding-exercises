# Import your libraries
import pandas as pd

# Start writing code
worker.head()

merged = worker.merge(
    title[["worker_ref_id", "worker_title"]],
    left_on="worker_id",
    right_on="worker_ref_id",
)
merged.nlargest(1, "salary", keep="all")[["worker_title"]]
