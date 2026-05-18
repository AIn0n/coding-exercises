# Import your libraries
import pandas as pd


# Start writing code
df = sf_events.sort_values(["user_id", "record_date"])

df["lag_1"] = df.groupby("user_id")["record_date"].shift(1)

df["lag_2"] = df.groupby("user_id")["lag_1"].shift(1)

df = df.dropna(axis="rows", subset=["lag_1", "lag_2"])

df[
    (df.record_date == df.lag_1 + pd.Timedelta(days=1))
    & (df.lag_1 == df.lag_2 + pd.Timedelta(days=1))
][["user_id"]]
