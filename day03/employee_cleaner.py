import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = {
    "employee_id",
    "name",
    "department",
    "salary",
    "years_of_experience",
    "performance_rating",
}



def load_employee_data(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        raise FileNotFoundError(f"File {file_path} does not exist.")
    employees=pd.read_csv(file_path)
    missing_columns=REQUIRED_COLUMNS - set(employees.columns)
    if missing_columns:
        logger.error(f"Missing required columns: {missing_columns}")
        raise ValueError(f"Missing required columns: {missing_columns}")
    return employees

def remove_duplicates(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees.drop_duplicates().copy()

    removed_count = len(employees) - len(cleaned)

    logger.info("Removed %d duplicate rows.", removed_count)

    return cleaned


def normalize_departments(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees.copy()
    cleaned["department"] = (cleaned["department"].astype("string").str.strip().str.upper())
    return cleaned


def fill_missing_salary(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees.copy()
    median_salary = cleaned["salary"].median()
    if pd.isna(median_salary):
        raise ValueError("Cannot calculate salary median.")

    cleaned["salary"] = cleaned["salary"].fillna(median_salary)
    return cleaned


def fill_missing_performance(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees.copy()

    median_performance = cleaned["performance_rating"].median()

    if pd.isna(median_performance):
        raise ValueError("Cannot calculate performance median.")

    cleaned["performance_rating"] = (
        cleaned["performance_rating"]
        .fillna(median_performance)
    )

    return cleaned



def remove_invalid_rows(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees[
        (employees["years_of_experience"] >= 0)
        & (employees["performance_rating"].between(1, 5))
        & (employees["salary"] > 0)
    ].copy()
    removed_count = len(employees) - len(cleaned)

    logger.warning("Removed %d invalid rows.", removed_count)

    return cleaned


def clean_employee_data(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = remove_duplicates(employees)
    cleaned = normalize_departments(cleaned)
    cleaned = fill_missing_salary(cleaned)
    cleaned = fill_missing_performance(cleaned)
    cleaned = remove_invalid_rows(cleaned)

    return cleaned.reset_index(drop=True)
