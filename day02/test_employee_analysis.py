import numpy as np

from main import create_employee_matrix, calculate_average_experience, get_high_performance_candidates


def  test_average_experience()->None:
    employees=create_employee_matrix()
    
    result=calculate_average_experience(employees)
    
    assert result==6.0
    
    
    
def test_high_performers()->None:
    employees=create_employee_matrix()
      
    result=get_high_performance_candidates(employees, min_performance=4.0)    
    assert len(result) == 3
    assert np.all(result[:, 1] >= 4.0)
    
    
def test_invalid_performance_rating() -> None:
    employees = create_employee_matrix()

    try:
        get_high_performance_candidates(employees, min_performance=6.0)

        raise AssertionError("Expected ValueError was not raised.")

    except ValueError:
        pass