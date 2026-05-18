# Import your libraries
import pandas as pd

# Start writing code
df = oscar_nominees[oscar_nominees.winner == True]

top_winners = (
    df.groupby("nominee")
    .agg(count=("winner", "count"))
    .reset_index()
    .nlargest(1, "count", keep="all")
    .sort_values("nominee")
)

top_winners.merge(nominee_information, left_on="nominee", right_on="name")[
    ["top_genre"]
]
