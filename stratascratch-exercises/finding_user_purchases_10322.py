# Import your libraries
import pandas as pd

# Start writing code
df = amazon_transactions.sort_values(by=["user_id", "created_at"])

df["prev"] = df.groupby(by=["user_id"])["created_at"].shift(1)
df["diff"] = (df["created_at"] - df["prev"]).dt.days

df = df.dropna(subset="diff", axis="rows")
df = df.groupby("user_id").first().reset_index()

df[(df["diff"] < 7) & (df["diff"] >= 1)].drop_duplicates(subset="user_id")[["user_id"]]
