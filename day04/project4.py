from pathlib import Path

import pandas as pd


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
        raise FileNotFoundError(f"Employee dataset not found: {file_path}")

    employees = pd.read_csv(file_path)
    missing_columns = REQUIRED_COLUMNS - set(employees.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    return employees


def clean_employee_data(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees.drop_duplicates().copy()
    cleaned["department"] = (
        cleaned["department"].astype("string").str.strip().str.upper()
    )
    cleaned["salary"] = cleaned["salary"].fillna(cleaned["salary"].median())
    cleaned["performance_rating"] = cleaned["performance_rating"].fillna(
        cleaned["performance_rating"].median()
    )

    cleaned = cleaned[
        (cleaned["years_of_experience"] >= 0)
        & (cleaned["performance_rating"].between(1, 5))
        & (cleaned["salary"] > 0)
    ].copy()

    return cleaned.reset_index(drop=True)


def add_practice_columns(employees: pd.DataFrame) -> pd.DataFrame:
    cleaned = employees.copy()

    if "training_hours" not in cleaned.columns:
        cleaned["training_hours"] = (
            (cleaned["years_of_experience"] * 8)
            + (cleaned["performance_rating"] * 5)
        ).round()

    if "absence_days" not in cleaned.columns:
        cleaned["absence_days"] = (
            ((5 - cleaned["performance_rating"]) * 2)
            + (5 - cleaned["years_of_experience"]).clip(lower=0) * 0.5
        ).round()

    return cleaned


def get_salary_outliers(employees: pd.DataFrame) -> pd.DataFrame:
    salary = employees["salary"]
    first_quartile = salary.quantile(0.25)
    third_quartile = salary.quantile(0.75)
    interquartile_range = third_quartile - first_quartile
    lower_bound = first_quartile - (1.5 * interquartile_range)
    upper_bound = third_quartile + (1.5 * interquartile_range)

    return employees[(salary < lower_bound) | (salary > upper_bound)]


def print_analysis(title: str, employees: pd.DataFrame) -> None:
    print(f"\n=== {title} ===")
    print(f"Mean Salary: {employees['salary'].mean():.2f}")
    print(f"Median Salary: {employees['salary'].median():.2f}")
    print(f"Salary Standard Deviation: {employees['salary'].std():.2f}")
    print(f"Highest Salary: {employees['salary'].max():.2f}")
    print(f"Lowest Salary: {employees['salary'].min():.2f}")

    print("\nAverage Salary by Department:")
    print(employees.groupby("department")["salary"].mean().round(2))

    print("\nAverage Performance by Department:")
    print(
        employees.groupby("department")["performance_rating"]
        .mean()
        .round(2)
    )

    print("\nCorrelations:")
    print(
        "Experience and Salary: "
        f"{employees['years_of_experience'].corr(employees['salary']):.2f}"
    )
    print(
        "Training Hours and Performance: "
        f"{employees['training_hours'].corr(employees['performance_rating']):.2f}"
    )
    print(
        "Absence Days and Performance: "
        f"{employees['absence_days'].corr(employees['performance_rating']):.2f}"
    )

    print("\nSalary Outliers using IQR:")
    outliers = get_salary_outliers(employees)
    if outliers.empty:
        print("No salary outliers found.")
    else:
        print(
            outliers[
                [
                    "employee_id",
                    "name",
                    "department",
                    "salary",
                ]
            ]
        )


def add_salary_outlier(employees: pd.DataFrame) -> pd.DataFrame:
    outlier_employee = {
        "employee_id": employees["employee_id"].max() + 1,
        "name": "Outlier Employee",
        "department": "IT",
        "salary": 10000,
        "years_of_experience": employees["years_of_experience"].median(),
        "performance_rating": employees["performance_rating"].median(),
        "training_hours": employees["training_hours"].median(),
        "absence_days": employees["absence_days"].median(),
    }

    return pd.concat(
        [employees, pd.DataFrame([outlier_employee])],
        ignore_index=True,
    )


def print_bonus_comparison(
    before_outlier: pd.DataFrame,
    after_outlier: pd.DataFrame,
) -> None:
    comparison = pd.DataFrame(
        {
            "Before Outlier": [
                before_outlier["salary"].mean(),
                before_outlier["salary"].median(),
                before_outlier["salary"].std(),
            ],
            "After Outlier": [
                after_outlier["salary"].mean(),
                after_outlier["salary"].median(),
                after_outlier["salary"].std(),
            ],
        },
        index=[
            "Mean Salary",
            "Median Salary",
            "Standard Deviation",
        ],
    )

    print("\n=== Bonus Comparison ===")
    print(comparison.round(2))


def print_observations(employees: pd.DataFrame) -> None:
    average_salary = employees.groupby("department")["salary"].mean()
    average_performance = employees.groupby("department")[
        "performance_rating"
    ].mean()

    highest_salary_department = average_salary.idxmax()
    highest_performance_department = average_performance.idxmax()

    print("\n=== 5 Observations ===")
    print(
        "- Experience and salary show a "
        f"{'positive' if employees['years_of_experience'].corr(employees['salary']) > 0 else 'negative'} "
        "correlation."
    )
    print(
        "- Training hours and performance show a "
        f"{'positive' if employees['training_hours'].corr(employees['performance_rating']) > 0 else 'negative'} "
        "correlation."
    )
    print(
        "- Absence days and performance show a "
        f"{'positive' if employees['absence_days'].corr(employees['performance_rating']) > 0 else 'negative'} "
        "correlation."
    )
    print(
        f"- {highest_salary_department} has the highest average salary "
        "in this dataset."
    )
    print(
        f"- {highest_performance_department} has the highest average "
        "performance in this dataset."
    )


def main() -> None:
    file_path = Path(__file__).parent / "data" / "employees_dirty_20.csv"
    employees = load_employee_data(file_path)
    cleaned_employees = add_practice_columns(clean_employee_data(employees))
    employees_with_outlier = add_salary_outlier(cleaned_employees)

    print_analysis("Before Outlier", cleaned_employees)
    print_analysis("After Outlier", employees_with_outlier)
    print_bonus_comparison(cleaned_employees, employees_with_outlier)
    print_observations(cleaned_employees)


if __name__ == "__main__":
    main()
