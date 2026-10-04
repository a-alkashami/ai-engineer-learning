import logging

import pandas as pd
from sklearn.linear_model import LinearRegression


def create_training_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "years_of_experience": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
            ],
            "salary": [
                700,
                930,
                980,
                1000,
                1190,
                1150,
                1200,
                1350,
                1456,
                1500,
                1645,
                1700,
                1800,
                1925,
                2000,
                2187,
                2200,
                2300,
                2490,
                2544,
                2600,
            ],
        }
    )
    
feature_column = "years_of_experience"
target_column = "salary"


def train_model()->LinearRegression:
    employees = create_training_data()
    X = employees[[feature_column]]
    y = employees[target_column]
    model = LinearRegression()
    model.fit(X, y)
    logging.info("Salary model trained successfully.")
    return model


def predict_salary(model: LinearRegression, years_of_experience: float) -> float:
    if years_of_experience < 0:
        logging.error("Years of experience cannot be negative.")
        raise ValueError("Years of experience cannot be negative.")
    prediction_data = pd.DataFrame({feature_column: [years_of_experience]})
    predicted_salary = model.predict(prediction_data)[0]
    logging.info(
        "Predicted salary for %f years of experience: %f",
        years_of_experience,
        predicted_salary,
    )
    return predicted_salary
   
  
    
    

