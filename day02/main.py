import logging 

import numpy as np
from numpy.typing import NDArray


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s | %(message)s'
)

logger = logging.getLogger(__name__)


def create_employee_matrix()->NDArray[np.float64]:
     employees=np.array(
          [
            [9, 4.5, 80],
            [3, 3.2, 25],
            [7, 4.8, 100],
            [5, 4.0, 60],
          ]
     )
     return employees
def calculate_average_experience(employees: NDArray[np.float64]) -> float:
    if employees.size == 0:
        raise ValueError("The employee matrix is empty.")
    
    average_experience = np.mean(employees[:, 0])
        #employees[:, 0]
        # هات جميع الصفوف
        # لكن فقط العمود رقم 0

    logger.info(f"Average experience calculated: {average_experience:.2f}")
    return average_experience

def get_high_performance_candidates(employees: NDArray[np.float64], min_performance: float=4.0) -> NDArray[np.float64]:
    if not 0 <= min_performance <= 5:
        raise ValueError("Performance rating must be between 0 and 5.")
    return employees[employees[:, 1] >= min_performance]




def main() -> None:
    try:
        employees = create_employee_matrix()
        logger.info("Employee matrix created successfully.")
        print(employees)

        average_experience = calculate_average_experience(employees)
        print(f"Average Experience: {average_experience:.2f}")


        print("\nHigh performers:")
        candidates = get_high_performance_candidates(employees, 4.0)
        print(candidates)

    except Exception as e:
        logger.error(f"An error occurred: {e}") 


if __name__ == "__main__":
    main()      
