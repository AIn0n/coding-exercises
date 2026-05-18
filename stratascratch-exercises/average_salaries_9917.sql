with avgs as
    (select e.department, avg(e.salary) as avg_salary
    from employee e
    group by e.department)
select 
    e.first_name,
    e.salary,
    a.department,
    a.avg_salary
from employee e
join avgs a on e.department = a.department;