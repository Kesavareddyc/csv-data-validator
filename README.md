# CSV Data Validator

A Python-based tool that validates CSV files, identifies data quality issues, and generates detailed validation reports.

## Features

* Validate required CSV headers
* Detect missing values
* Validate email formats
* Detect duplicate IDs and email addresses
* Validate numeric IDs and age ranges
* Detect malformed CSV rows
* Calculate valid and invalid row counts
* Generate detailed validation reports
* Handle missing files and invalid file paths
* Display clear error messages

## Technologies

* Python
* csv module
* Regular expressions
* os module
* unittest

## Project Structure

```text
csv-data-validator/
├── data/
│   ├── combined_test.csv
│   ├── duplicate_emails_test.csv
│   ├── duplicate_ids_test.csv
│   ├── empty_test.csv
│   ├── invalid_age_test.csv
│   ├── invalid_email_test.csv
│   ├── invalid_id_test.csv
│   ├── malformed_rows_test.csv
│   ├── missing_headers_test.csv
│   └── missing_values_test.csv
├── reports/
│   └── validation_report.txt
├── tests/
│   └── test_validator.py
├── main.py
├── .gitignore
└── README.md
```

## Requirements

* Python 3.8 or later
* No external Python packages required

## How to Run

1. Clone or download this repository.

2. Open the project folder in your terminal.

3. Run the application:

   ```bash
   python main.py
   ```

4. Enter the path of the CSV file when prompted.

   Example:

   ```text
   Enter the CSV file path: data/combined_test.csv
   ```

## CSV File Format

The CSV file must contain these required headers:

```csv
id,name,email,age,city
1,Kesava,kesava@example.com,22,Bengaluru
2,Ravi,ravi@example.com,25,Chennai
```

The validator checks the required columns and validates the data in each row.

## Validation Checks

| Check            | Description                                      |
| ---------------- | ------------------------------------------------ |
| Headers          | Checks for required columns                      |
| Missing values   | Identifies empty fields                          |
| Email            | Checks email format                              |
| Duplicate IDs    | Detects repeated IDs                             |
| Duplicate emails | Detects repeated email addresses                 |
| Numeric ID       | Checks that IDs are positive integers            |
| Age              | Checks that ages are integers between 18 and 100 |
| Row structure    | Detects rows with an incorrect number of columns |

## Sample Output

```text
CSV DATA VALIDATOR

HEADER VALIDATION
Header validation: Passed

VALIDATION SUMMARY
------------------
Total rows: 5
Valid rows: 2
Invalid rows: 3
Total errors: 4
Status: FAILED

Report saved to: reports/validation_report.txt
```

The sample output illustrates the combined test dataset. Actual results depend on the CSV file provided.

## Validation Report

After validation, a detailed report is saved to:

```text
reports/validation_report.txt
```

The report includes:

* Validation status
* Total number of rows
* Valid and invalid row counts
* Total number of errors
* Detailed validation errors

## Automated Testing

The project includes automated unit tests using Python's built-in `unittest` framework.

To run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

The project currently has 17 passing automated tests covering validation and error-handling scenarios.

## Error Handling

The application handles:

* Empty file paths
* Unsupported file extensions
* Missing CSV files
* File-reading errors
* Report-writing errors

## Future Improvements

* Support configurable validation rules
* Export invalid rows to a separate CSV file
* Support command-line arguments

## Author

Kesava Reddy
