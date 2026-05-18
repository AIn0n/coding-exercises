select
    o.cust_id, c.first_name, sum(o.total_order_cost)
from orders o
join customers c
on c.id = o.cust_id
group by o.cust_id, c.first_name
order by first_name;
