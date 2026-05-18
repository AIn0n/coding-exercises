# Import your libraries
import pandas as pd

# Start writing code
df = players_results.sort_values(by=["player_id", "match_date"])
df["lag"] = df.groupby("player_id")["match_result"].transform("shift")
df["change"] = (df["match_result"] != df["lag"]).cumsum()

df["streak"] = df.groupby(by=["player_id", "change"]).cumcount() + 1
df[df["lag"] != "L"].nlargest(1, "streak", keep="all")[["player_id", "streak"]]
