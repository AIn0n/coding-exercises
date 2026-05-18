# Import your libraries
import pandas as pd

# Start writing code
df = ms_employee_salary.sort_values(
    ["first_name", "last_name", "department_id", "salary"]
)

df.drop_duplicates(subset=["first_name", "last_name"], keep="last")
