import pandas as pd
import pytest

from employee_analyzer import (
    find_salary_outliers,
    get_correlation_matrix,
    get_summary_statistics,
)


@pytest.fixture
def employees() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "employee_id": 1,
                "name": "Ahmad",
                "department": "IT",
                "salary": 1000,
                "years_of_experience": 5,
                "performance_rating": 4.0,
                "training_hours": 40,
            },
            {
                "employee_id": 2,
                "name": "Sara",
                "department": "HR",
                "salary": 1200,
                "years_of_experience": 7,
                "performance_rating": 4.5,
                "training_hours": 60,
            },
            {
                "employee_id": 3,
                "name": "Omar",
                "department": "Finance",
                "salary": 1400,
                "years_of_experience": 9,
                "performance_rating": 4.8,
                "training_hours": 80,
            },
        ]
    )


def test_summary_contains_salary(
    employees: pd.DataFrame,
) -> None:
    result = get_summary_statistics(employees)

    assert "salary" in result.columns


def test_correlation_matrix_is_square(
    employees: pd.DataFrame,
) -> None:
    result = get_correlation_matrix(employees)

    assert result.shape == (4, 4)


def test_no_salary_outliers(
    employees: pd.DataFrame,
) -> None:
    result = find_salary_outliers(employees)

    assert result.empty


def test_empty_dataset_is_rejected() -> None:
    empty = pd.DataFrame(
        columns=[
            "salary",
            "years_of_experience",
            "performance_rating",
            "training_hours",
        ]
    )

    with pytest.raises(ValueError):
        get_summary_statistics(empty)