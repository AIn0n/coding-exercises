select 
    d.city, 
    d.property_type, 
    avg(d.bathrooms) as n_bathrooms_avg, 
    avg(d.bedrooms) as n_bedrooms_avg 
from 
    airbnb_search_details d 
group by 
    d.city, 
    d.property_type
