select
    p.budget,
    p.title,
    ceiling((p.end_date - p.start_date) *  (sum(le.salary) / 365)) as prorated_salary
from linkedin_projects p
inner join linkedin_emp_projects lep on lep.project_id = p.id
inner join linkedin_employees le on le.id = lep.emp_id
group by p.budget, p.title, p.end_date, p.start_date
having ceiling((p.end_date - p.start_date) *  (sum(le.salary) / 365)) > p.budget
order by p.title;
