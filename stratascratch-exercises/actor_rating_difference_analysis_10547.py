# Import your libraries
import pandas as pd

# Start writing code
pick_last = actor_rating_shift.groupby("actor_name")["release_date"].transform("max")

recent_df = actor_rating_shift[pick_last == actor_rating_shift["release_date"]][
    ["actor_name", "film_rating"]
].rename(columns={"film_rating": "latest_rating"})

without_recent = actor_rating_shift[~(actor_rating_shift["release_date"] == pick_last)]

avg_df = (
    without_recent.groupby("actor_name")
    .agg(
        avg_rating=("film_rating", "mean"),
    )
    .reset_index()
)

res = recent_df.merge(avg_df, on="actor_name", how="left")

res["avg_rating"].fillna(res["latest_rating"], inplace=True)
res.assign(rating_difference=res["latest_rating"] - res["avg_rating"])
