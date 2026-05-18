select
    inspection_type,
    count(*) filter (where risk_category is null) as no_risk_results,
    count(*) filter (where risk_category = 'Low Risk') as low_risk_results,
    count(*) filter (where risk_category = 'Moderate Risk') as moderate_risk_results,
    count(*) filter (where risk_category = 'High Risk') as high_risk_results,
    count(*) as total_inspections
from sf_restaurant_health_violations
group by inspection_type
order by count(*) desc;
