select sum(s.sales_revenue)
from sales_performance s
where   s.salesperson = 'Samantha' OR
        s.salesperson = 'Lisa';
