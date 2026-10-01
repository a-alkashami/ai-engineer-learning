# Project Context

## Project Name
ai-engineer-learning

## Project Purpose
Python learning exercises organized by day.

## Tech Stack
- Python
- pandas
- pytest

## Project Structure
- `day03/`: employee data cleaning exercises.
- `day04/`: employee analysis exercises.
- `day04/data/`: CSV datasets used by day04 scripts.

## Main Modules
- `day03/employee_cleaner.py`: loads and cleans employee datasets.
- `day04/employee_analyzer.py`: analysis helper functions for employee data.
- `day04/project4.py`: standalone day04 assignment script using `employees_dirty_20.csv`.

## Setup Commands
- Run day04 project: `.venv\Scripts\python.exe day04\project4.py`
- Run day04 tests: `.venv\Scripts\python.exe -m pytest day04`

## Latest Changes
- 2026-09-27
  - Changed files: `day04/project4.py`
  - What changed: added salary, department, correlation, IQR outlier, observation, and bonus before/after outlier analysis.
  - Why it changed: complete the day04 employee analysis assignment using `employees_dirty_20.csv`.
  - Risks or important notes: `employees_dirty_20.csv` does not include `training_hours` or `absence_days`, so `project4.py` adds deterministic practice columns when those fields are missing.
