import logging
import  pandas as pd


logging.basicConfig(level=logging.INFO,
                     format='%(levelname)s - %(message)s')

logger=logging.getLogger(__name__)




def create_employee_dataframe() -> pd.DataFrame:
    employees=[   {
            "name": "Ahmad",
            "department": "IT",
            "salary": 1200,
            "years_of_experience": 9,
        },
        {
            "name": "Sara",
            "department": "HR",
            "salary": 950,
            "years_of_experience": 5,
        },
        {
            "name": "Omar",
            "department": "Finance",
            "salary": 1100,
            "years_of_experience": 7,
        },
    ]

    return pd.DataFrame(employees)

def calculate_average_salary(employees: pd.DataFrame) -> float:
    if employees.empty:
        raise ValueError("The employee DataFrame is empty.")
    average_salary = employees["salary"].mean()
    logger.info(f"Average salary calculated: {average_salary:.2f}")
    return average_salary



def get_leadership_candidates(employees: pd.DataFrame , min_experience: int ) -> pd.DataFrame:
     if min_experience < 0:
        raise ValueError("Minimum experience must be a non-negative integer.")
     return employees[employees["years_of_experience"] >= min_experience]


def main()-> None:
    try:
        employees=create_employee_dataframe()
        logger.info("Employee DataFrame created successfully.")
        print(employees)

        average_salary=calculate_average_salary(employees)
        print(f"Average Salary: {average_salary:.2f}")

        candidates = get_leadership_candidates(employees,7)
        print(candidates)
 

    except (KeyError,TypeError,ValueError) as error:
            logger.error(f"An error occurred: {logging.error}")




if __name__=="__main__":
    main()