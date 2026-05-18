select DENSE_RANK() over (
        order by sum_n_messages desc
    ),
    *
from
(
    select
        a.id_guest,
        sum(a.n_messages) as sum_n_messages
    from airbnb_contacts a
    group by a.id_guest
    order by sum(a.n_messages)
);
