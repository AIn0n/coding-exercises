# Import your libraries
import pandas as pd

# Start writing code
df = google_gmail_emails

grouped = (
    df.groupby(by="from_user").agg(total_emails=("to_user", "count")).reset_index()
)

grouped["rank"] = grouped["total_emails"].rank(ascending=False)

grouped.sort_values(by=["rank", "from_user"]).assign(
    activity_rank=range(1, len(grouped) + 1)
).drop(columns="rank")
