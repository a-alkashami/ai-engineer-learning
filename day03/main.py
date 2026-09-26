import logging
from pathlib import Path

import pandas as pd

from employee_cleaner import clean_employee_data, load_employee_data
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    file_path = Path(__file__).parent / "data" / "employees.csv"

    try:
        employees = load_employee_data(file_path)

        print("\nRaw Data:")
        print(employees)

        print("\nMissing Values:")
        print(employees.isna().sum())

        cleaned_employees = clean_employee_data(employees)

        print("\nClean Data:")
        print(cleaned_employees)

        logger.info(
            "Cleaning completed. Final rows: %d",
            len(cleaned_employees),
        )

    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        logger.exception("Unable to process employee dataset: %s", error)


if __name__ == "__main__":
    main()