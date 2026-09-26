import logging
from pathlib import Path

import pandas as pd

from employee_analyzer import (
    find_salary_outliers,
    get_correlation_matrix,
    get_department_summary,
    get_summary_statistics,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def load_employee_data(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(
            f"Employee dataset not found: {file_path}"
        )

    return pd.read_csv(file_path)


def main() -> None:
    file_path = Path(__file__).parent / "data" / "employees.csv"

    try:
        employees = load_employee_data(file_path)

        print("\n=== Summary Statistics ===")
        print(get_summary_statistics(employees))

        print("\n=== Correlation Matrix ===")
        print(get_correlation_matrix(employees).round(2))

        print("\n=== Department Summary ===")
        print(get_department_summary(employees))

        print("\n=== Potential Salary Outliers ===")
        salary_outliers = find_salary_outliers(employees)

        if salary_outliers.empty:
            print("No salary outliers detected.")
        else:
            print(
                salary_outliers[
                    [
                        "employee_id",
                        "name",
                        "department",
                        "salary",
                    ]
                ]
            )

    except (
        FileNotFoundError,
        ValueError,
        pd.errors.ParserError,
    ) as error:
        logger.exception(
            "Employee analysis failed: %s",
            error,
        )


if __name__ == "__main__":
    main()