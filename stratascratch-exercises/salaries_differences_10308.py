# Import your libraries
import pandas as pd
import numpy as np

# Start writing code
db_employee.head()

merged = db_employee.merge(db_dept, left_on="department_id", right_on="id")
grouped = merged.groupby(by="department", as_index=False).agg(
    max_salary=("salary", "max")
)
diff = grouped.merge(grouped, how="cross", suffixes=("_1", "_2"))
diff["salary_difference"] = np.abs(diff["max_salary_1"] - diff["max_salary_2"])
diff[(diff["department_1"] == "engineering") & (diff["department_2"] == "marketing")][
    "salary_difference"
]
