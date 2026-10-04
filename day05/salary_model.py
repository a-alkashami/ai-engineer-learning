import logging
import pandas as pd
from sklearn.linear_model import LinearRegression

logger = logging.getLogger(__name__)


FEATURE_COLUMN = "years_of_experience"
TARGET_COLUMN = "salary"


def validate_training_data(employees: pd.DataFrame) -> None:
    required_columns = {
        FEATURE_COLUMN,
        TARGET_COLUMN,
    }

    missing_columns = required_columns - set(employees.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    if employees.empty:
        raise ValueError("Training dataset cannot be empty.")

    if employees[[FEATURE_COLUMN, TARGET_COLUMN]].isna().any().any():
        raise ValueError("Training data contains missing values.")

    
def train_salary_model(employees: pd.DataFrame) -> LinearRegression:
    validate_training_data(employees)
    X = employees[[FEATURE_COLUMN]]
    y = employees[TARGET_COLUMN]
    model = LinearRegression()
    model.fit(X, y)
    logger.info("Salary model trained successfully.")
    return model   

def predict_salary(model: LinearRegression, years_of_experience: float) -> float:
    if years_of_experience < 0:
        logger.error("Years of experience cannot be negative.")
        raise ValueError("Years of experience cannot be negative.")
    prediction_data= pd.DataFrame({FEATURE_COLUMN: [years_of_experience]})
    predicted_salary = model.predict(prediction_data)[0]
    logger.info("Predicted salary for %f years of experience: %f", years_of_experience, predicted_salary)
    return predicted_salary 