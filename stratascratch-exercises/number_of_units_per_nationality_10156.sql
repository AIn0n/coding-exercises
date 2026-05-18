with unique_hosts as (
    select distinct host_id, age, nationality
    from airbnb_hosts
)

select h.nationality, count(*)
from airbnb_units u
join unique_hosts h
on h.host_id = u.host_id
where
    u.unit_type = 'Apartment' and
    h.age < 30
group by h.nationality;
