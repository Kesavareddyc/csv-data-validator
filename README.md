
# CSV Data Validator

A Python project that validates CSV files and generates
a detailed validation report.

## Features

- Validate required CSV headers
- Detect missing values
- Validate email formats
- Detect duplicate IDs and emails
- Validate numeric IDs and age ranges
- Detect malformed CSV rows
- Count valid and invalid rows
- Generate a detailed validation report

## Technologies

- Python
- csv module
- Regular expressions
- os module

## Project Structure

csv-data-validator/
├── data/
├── reports/
├── main.py
└── README.md

## How to Run

1. Install Python.
2. Clone or download this project.
3. Open the project folder in a terminal.
4. Run:

   python main.py

## Output

The validator displays a validation summary
and saves a detailed report to:

reports/validation_report.txt