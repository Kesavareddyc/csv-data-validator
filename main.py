
import csv
import re
import os

# File paths
report_path = "reports/validation_report.txt"
expected_headers = ["id", "name", "email", "age", "city"]

error_count = 0
errors = []
invalid_rows = set()


def add_error(message, row_number=None):
    """Store an error and update the error count."""
    global error_count

    errors.append(message)
    error_count += 1

    if row_number is not None:
        invalid_rows.add(row_number)


def validate_csv(file_path):
    """Read and validate a CSV file."""
    global error_count

    try:
        with open(
            file_path, mode="r", newline="", encoding="utf-8"
        ) as file:
            reader = csv.reader(file)
            headers = next(reader, [])
            rows = list(reader)

    except (OSError, UnicodeDecodeError, csv.Error) as error:
        print(f"Error reading CSV file: {error}")
        return False

    total_rows = len(rows)
    valid_rows = []

    print("\nCSV DATA VALIDATOR")
    print("------------------")

    # Header validation
    print("\nHEADER VALIDATION")

    missing_headers = [
        header for header in expected_headers
        if header not in headers
    ]

    if missing_headers:
        print("Missing headers:", missing_headers)

        for header in missing_headers:
            add_error(f"Missing required header: {header}")
    else:
        print("Header validation: Passed")

    # Field-level validation
    if missing_headers:
        print(
            "\nField-level validation skipped: "
            "required headers are missing."
        )
    else:
        # Row structure validation
        print("\nROW STRUCTURE CHECK")
        expected_columns = len(headers)

        for row_number, row in enumerate(rows, start=2):
            actual_columns = len(row)

            if actual_columns != expected_columns:
                message = (
                    f"Malformed row | Row: {row_number} | "
                    f"Expected: {expected_columns} | "
                    f"Found: {actual_columns}"
                )
                print(message)
                add_error(message, row_number)
                continue

            valid_rows.append((row_number, row))

        # Missing value validation
        print("\nMISSING VALUE CHECK")

        for row_number, row in valid_rows:
            for column_index, value in enumerate(row):
                if value.strip() == "":
                    message = (
                        f"Missing value | Row: {row_number} | "
                        f"Column: {headers[column_index]}"
                    )
                    print(message)
                    add_error(message, row_number)

        # Email format validation
        print("\nEMAIL FORMAT CHECK")
        email_pattern = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
        email_index = headers.index("email")

        for row_number, row in valid_rows:
            email = row[email_index].strip()

            if email and not re.fullmatch(email_pattern, email):
                message = (
                    f"Invalid email | Row: {row_number} | "
                    f"Email: {email}"
                )
                print(message)
                add_error(message, row_number)

        # Duplicate ID validation
        print("\nDUPLICATE ID CHECK")
        id_index = headers.index("id")
        seen_ids = set()

        for row_number, row in valid_rows:
            record_id = row[id_index].strip()

            if not record_id:
                continue

            if record_id in seen_ids:
                message = (
                    f"Duplicate ID | Row: {row_number} | "
                    f"ID: {record_id}"
                )
                print(message)
                add_error(message, row_number)
            else:
                seen_ids.add(record_id)

        # Numeric validation
        print("\nNUMERIC VALIDATION")
        age_index = headers.index("age")

        for row_number, row in valid_rows:
            # Validate ID
            record_id = row[id_index].strip()

            try:
                numeric_id = int(record_id)

                if numeric_id <= 0:
                    message = (
                        f"Invalid ID | Row: {row_number} | "
                        "ID must be positive"
                    )
                    print(message)
                    add_error(message, row_number)

            except ValueError:
                message = (
                    f"Invalid ID | Row: {row_number} | "
                    "ID must be an integer"
                )
                print(message)
                add_error(message, row_number)

            # Validate age
            age_value = row[age_index].strip()

            try:
                age = int(age_value)

                if age < 18 or age > 100:
                    message = (
                        f"Invalid age | Row: {row_number} | "
                        f"Age: {age}"
                    )
                    print(message)
                    add_error(message, row_number)

            except ValueError:
                message = (
                    f"Invalid age | Row: {row_number} | "
                    "Age must be an integer"
                )
                print(message)
                add_error(message, row_number)

        # Duplicate email validation
        print("\nDUPLICATE EMAIL CHECK")
        seen_emails = set()

        for row_number, row in valid_rows:
            email = row[email_index].strip().lower()

            if not email:
                continue

            if email in seen_emails:
                message = (
                    f"Duplicate email | Row: {row_number} | "
                    f"Email: {email}"
                )
                print(message)
                add_error(message, row_number)
            else:
                seen_emails.add(email)

    # Calculate summary
    invalid_row_count = len(invalid_rows)
    valid_row_count = total_rows - invalid_row_count
    status = "PASSED" if error_count == 0 else "FAILED"

    print("\nVALIDATION SUMMARY")
    print("------------------")
    print("Total rows:", total_rows)
    print("Valid rows:", valid_row_count)
    print("Invalid rows:", invalid_row_count)
    print("Total errors:", error_count)
    print("Status:", status)

    # Save report
    try:
        os.makedirs("reports", exist_ok=True)

        with open(report_path, mode="w", encoding="utf-8") as report:
            report.write("CSV DATA VALIDATION REPORT\n")
            report.write("--------------------------\n")
            report.write(f"Status: {status}\n")
            report.write(f"Total rows: {total_rows}\n")
            report.write(f"Valid rows: {valid_row_count}\n")
            report.write(f"Invalid rows: {invalid_row_count}\n")
            report.write(f"Total errors: {error_count}\n")
            report.write("\nDETAILED ERRORS\n")
            report.write("--------------------------\n")

            if errors:
                for error in errors:
                    report.write(error + "\n")
            else:
                report.write("No errors found.\n")

        print(f"\nReport saved to: {report_path}")

    except OSError as error:
        print(f"Error saving report: {error}")

    return True


def main():
    file_path = input("Enter the CSV file path: ").strip()

    if not file_path:
        print("Error: Please enter a CSV file path.")
        raise SystemExit(1)

    if not file_path.lower().endswith(".csv"):
        print("Error: Please provide a CSV file.")
        raise SystemExit(1)

    if not os.path.isfile(file_path):
        print(f"Error: File not found: {file_path}")
        raise SystemExit(1)

    if not validate_csv(file_path):
        raise SystemExit(1)


if __name__ == "__main__":
    main()