with
unique_trans as (
    select distinct user_id, created_at
    from amazon_transactions
),
diffs as (
    select
        user_id,
        abs(LAG(created_at) OVER (
            partition by user_id
            order by created_at
        ) - created_at) as diff
    from unique_trans
)

select distinct user_id
from diffs where diff <= 7;
