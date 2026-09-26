import logging 

import numpy as np
from numpy.typing  import NDArray


logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s | %(message)s'
)

logger = logging.getLogger(__name__)


# [
#     experience,
#     performance_rating,
#     training_hours
# ]

def create_employees_matrix()->NDArray[np.float64]:
    employees = np.array([
        [9, 4.5, 80],
        [3, 3.2, 25],
        [7, 4.8, 100],
        [5, 4.0, 60],
        [2, 2.8, 15],
        [10, 4.9, 120],
        [6, 3.9, 50],
        [4, 4.2, 45],
        [8, 4.6, 90],
        [1, 3.0, 10],
    ], dtype=np.float64)
    
    return employees



def get_average_experience(employees:NDArray[np.float64]) -> float:
    if employees.size==0 :
       raise ValueError("The employee matrix is empty.")
    
    average_experience=np.mean(employees[:,0])
    
    logger.info(f"Average experience calculated: {average_experience:.2f}")
    return average_experience


def avg_Performance(employyes:NDArray[np.float64])->float:
    if employyes.size==0:
        raise ValueError('The employee is empty')
    
    avg_per=np.mean(employyes[:,1])
    logger.info(f"Average Performance calculated: {avg_per:.2f}")
    
    return avg_per 
 
def get_emps_by_performance(employyes:NDArray[np.float64], min_per: float = 4.0) -> NDArray[np.float64]:

    return employyes[employyes[:, 1] >= min_per]
 
def get_emps_by_experience(employyes: NDArray[np.float64], min_exp: float = 5.0) -> NDArray[np.float64]:
    return employyes[employyes[:, 0] >= min_exp]
 
def get_emp_how_has_high_training(employyes: NDArray[np.float64], min_training: float = 50.0) -> float:
    
    max_training= np.max(employyes[:,2])
    
    return  max_training




def main() -> None:
 
 
    try:
        employees = create_employees_matrix()
        logger.info("Employee matrix created successfully.")
        print(employees)

        average_experience = get_average_experience(employees)
        print(f"Average Experience: {average_experience:.2f}")

        average_performance = avg_Performance(employees)
        print(f"Average Performance: {average_performance:.2f}")

        print("\nHigh performers:")
        candidates = get_emps_by_performance(employees, 4.0)
        print(candidates)

        print("\nExperienced employees:")
        experienced_candidates = get_emps_by_experience(employees, 5.0)
        print(experienced_candidates)

        print("\nEmployee with highest training hours:")
        max_training_hours = get_emp_how_has_high_training(employees, 50.0)
        print(max_training_hours)

    except Exception as e:
        logger.error(f"An error occurred: {e}")
 

if __name__ == "__main__":
    main()      
