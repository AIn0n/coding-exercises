select distinct g.guest_id, h.host_id
from airbnb_guests g
join airbnb_hosts h
on g.gender = h.gender and g.nationality = h.nationality;
