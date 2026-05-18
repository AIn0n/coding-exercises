# Import your libraries
import pandas as pd

# Start writing code
sent_df = fb_friend_requests[fb_friend_requests["action"] == "sent"]
accepted_df = fb_friend_requests[fb_friend_requests["action"] == "accepted"]

merged = sent_df.merge(
    accepted_df,
    on=["user_id_sender", "user_id_receiver"],
    how="outer",
)

merged["accepted"] = ~merged["action_y"].isna()
by_date = (
    merged.groupby("date_x")
    .agg(acceptance_sum=("accepted", "sum"), all_sum=("action_x", "count"))
    .reset_index()
)

by_date["acceptance_rate"] = by_date["acceptance_sum"] / by_date["all_sum"]
by_date[["date_x", "acceptance_rate"]]
