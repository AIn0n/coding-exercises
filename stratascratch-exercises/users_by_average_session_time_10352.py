# Import your libraries
import pandas as pd

df = facebook_web_log[
    facebook_web_log["action"].isin(["page_load", "page_exit"])
].sort_values(["user_id", "timestamp"])
df["day"] = df["timestamp"].dt.date

loads = df[df["action"] == "page_load"][["user_id", "timestamp", "day"]]
exits = df[df["action"] == "page_exit"][["user_id", "timestamp", "day"]]

loads = loads.groupby(by=["user_id", "day"]).max()
exits = exits.groupby(by=["user_id", "day"]).min()

merged = loads.merge(exits, on=["user_id", "day"], suffixes=("_load", "_exit"))

merged = merged[merged["timestamp_exit"] > merged["timestamp_load"]]
merged["duration"] = (merged.timestamp_exit - merged.timestamp_load).dt.seconds
merged.groupby("user_id").duration.mean().reset_index()
