select shipable * 100.0 / orders_count as percent_shipable
from
(
    select
        count(*) filter (where c.address is not Null) as shipable,
        count(*) as orders_count
    from orders o
    join customers c
    on o.cust_id = c.id
);
