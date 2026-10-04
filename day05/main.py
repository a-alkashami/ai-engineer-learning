import logging

import pandas as pd

from salary_model import predict_salary, train_salary_model


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)


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
            ],
            "salary": [
                700,
                800,
                900,
                1000,
                1100,
                1200,
                1300,
            ],
        }
    )


def main() -> None:
    employees = create_training_data()

    model = train_salary_model(employees)

    predicted_salary = predict_salary(
        model=model,
        years_of_experience=8,
    )

    print(
        f"Predicted salary for 8 years of experience: "
        f"{predicted_salary:.2f}"
    )


if __name__ == "__main__":
    main()