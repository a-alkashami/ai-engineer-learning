import pandas as pd
import logging 
from pathlib import Path


logger=logging.getLogger(__name__)

REQUIRED_COLUMNS = {
    "employee_id",
    "name",
    "department",
    "salary",
    "years_of_experience",
    "performance_rating",
}


def load_emoloyees_from_file(path:Path)->pd.DataFrame:
    if not path.exists():
        logger.error(f"file missing")
        raise FileNotFoundError(f"File {path} does not exist.")
    employees=pd.read_csv(path)
    missing_columns=REQUIRED_COLUMNS-set(employees.columns)
    if missing_columns:
      logger.error(f"Missing required columns: {missing_columns}")
      raise ValueError(f"Missing required columns: {missing_columns}")
    return employees    
    
    
def remove_duplicates(employees:pd.DataFrame)->pd.DataFrame:
    cleaned=employees.drop_duplicates().copy()
    missing_count=len(employees)-len(cleaned)
    logger.info(f"missing count is {missing_count}")
    return cleaned

def normalize_departments(employees:pd.DataFrame)->pd.DataFrame:
    cleaned=employees.copy()
    cleaned['department']=cleaned["department"].astype("string").str.strip().str.upper()
    return cleaned

      
    