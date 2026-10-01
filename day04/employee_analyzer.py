import pandas as pd

import logging

logger=logging.getLogger(__name__)

NUMERIC_COLUMNS = [
    "salary",
    "years_of_experience",
    "performance_rating",
    "training_hours",
]


def validate_employee_data(employees:pd.DataFrame)->None:
    missing_columns=set(NUMERIC_COLUMNS)-set(employees.columns)
    if missing_columns:
        logger.error(f"Missing columns: {missing_columns}")
        raise ValueError(f"Missing columns: {missing_columns}")
    if  employees.empty:
        logger.error("The DataFrame is empty")
        raise ValueError("The DataFrame is empty")
    
def get_summary_statistics(employees: pd.DataFrame) -> pd.DataFrame:
    validate_employee_data(employees)
    summary = employees[NUMERIC_COLUMNS].describe()
    return summary    
    
def get_correlation_matrix(
    employees: pd.DataFrame,
) -> pd.DataFrame:
    validate_employee_data(employees)

    return employees[NUMERIC_COLUMNS].corr()






def get_department_summary(employees: pd.DataFrame) -> pd.DataFrame:
    validate_employee_data(employees)
    department_summary = employees.groupby("department").agg(
        employee_count=("employee_id", "count"),
        average_salary=("salary", "mean"),
        average_training_hours=("training_hours", "mean"),
        average_performance=("performance_rating", "mean"),
    ).round(2).sort_values(by="average_salary", ascending=False)
    return department_summary

def find_salary_outliers(employees: pd.DataFrame) -> pd.DataFrame:
    validate_employee_data(employees)
    
    salary=employees["salary"]
    first_quartile = salary.quantile(0.25)
    third_quartile = salary.quantile(0.75)
    
    interquartile_range=third_quartile-first_quartile
    
    lower_bound = first_quartile - (1.5 * interquartile_range)
    upper_bound = third_quartile + (1.5 * interquartile_range)
    logger.info(
        "Salary outlier bounds: %.2f to %.2f",
        lower_bound,
        upper_bound,
    )

    return employees[
        (salary < lower_bound)
        | (salary > upper_bound)
    ]
