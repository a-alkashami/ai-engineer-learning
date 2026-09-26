import pandas as pd

def create_employee_dataframe() -> pd.DataFrame:
    employees = [
        {
            "name": "Ahmad",
            "department": "IT",
            "salary": 1200,
            "performance_rating": 9,
             "years_of_experience": 5,
        },
        {
            "name": "Sara",
            "department": "HR",
            "salary": 950,
            "performance_rating": 5,
            "years_of_experience": 3,
        },
        {
            "name": "Omar",
            "department": "Finance",
            "salary": 1100,
            "performance_rating": 7,
            "years_of_experience": 4,
        },
        {
            "name": "Layla",
            "department": "Marketing",
            "salary": 1000,
            "performance_rating": 6,
            "years_of_experience": 2,
        },
        {
            "name": "Hassan",
            "department": "IT",
            "salary": 1300,
            "performance_rating": 8,
            "years_of_experience": 6,
        },
        {
            "name": "Nadia",
            "department": "HR",
            "salary": 900,
            "performance_rating": 4,
            "years_of_experience": 2,
        },
        {
            "name": "Khalid",
            "department": "Finance",
            "salary": 1150,
            "performance_rating": 7,
            "years_of_experience": 5,
        },
        {
            "name": "Mona",
            "department": "Marketing",
            "salary": 1050,
            "performance_rating": 6,
            "years_of_experience": 3,
        },
        
    ]

    return pd.DataFrame(employees)


def print_employee_dataframe(employees: pd.DataFrame) -> None:
    if employees.empty:
        print("The employee DataFrame is empty.")
    else:
        print("Employee DataFrame:")
        print(employees)

def calculate_average_salary(employees: pd.DataFrame) -> float:
    if employees.empty:
        raise ValueError("The employee DataFrame is empty.")
    average_salary = employees["salary"].mean()
    return average_salary

def get_employees_by_experience(employees: pd.DataFrame, min_experience: int) -> pd.DataFrame:
    if min_experience < 0:
        raise ValueError("Minimum experience must be a non-negative integer.")
    return employees[employees["years_of_experience"] >= min_experience]


def group_employees_by_department(employees: pd.DataFrame) -> pd.DataFrame:
    if employees.empty:
        raise ValueError("The employee DataFrame is empty.")
    return employees.groupby("department").agg(
        average_salary=pd.NamedAgg(column="salary", aggfunc="mean"),
        average_performance_rating=pd.NamedAgg(column="performance_rating", aggfunc="mean"),
        total_employees=pd.NamedAgg(column="name", aggfunc="count")
    ).reset_index()


def main() -> None:
    try:
        employees = create_employee_dataframe()
        print_employee_dataframe(employees)

        average_salary = calculate_average_salary(employees)
        print(f"Average Salary: {average_salary:.2f}")

        experienced_employees = get_employees_by_experience(employees, 4)
        print("Employees with at least 4 years of experience:")
        print(experienced_employees)

        department_summary = group_employees_by_department(employees)
        print("Department Summary:")
        print(department_summary)

    except (KeyError, TypeError, ValueError) as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main() 