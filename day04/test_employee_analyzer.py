import pandas as pd

from day04.employee_analyzer import (
 
    normalize_departments,
    remove_duplicates,  
    clean_employee_data,
)


def create_test_data() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "employee_id": 1,
                "name": "Ahmad",
                "department": "IT",
                "salary": 1200,
                "years_of_experience": 9,
                "performance_rating": 4.5,
            },
            {
                "employee_id": 2,
                "name": "Sara",
                "department": " it ",
                "salary": None,
                "years_of_experience": 5,
                "performance_rating": 4.2,
            },
            {
                "employee_id": 2,
                "name": "Sara",
                "department": " it ",
                "salary": None,
                "years_of_experience": 5,
                "performance_rating": 4.2,
            },
        ]
    )
    
    
def test_remove_duplicates():
    employees = create_test_data()
    cleaned = remove_duplicates(employees)
    assert len(cleaned) == 2
    
def test_normalize_departments():
    employees = create_test_data()
    cleaned = normalize_departments(employees)
    assert cleaned["department"].iloc[1] == "IT"

def test_clean_employee_data() -> None:
    employees = create_test_data()

    result = clean_employee_data(employees)

    assert len(result) == 2
    assert result["salary"].isna().sum() == 0
    assert result["department"].tolist() == ["IT", "IT"]