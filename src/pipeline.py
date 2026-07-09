from pathlib import Path
import sys


def read_customers(file_path):
    with open(file_path, "r") as file:
        rows = file.readlines()

    return rows


def count_customer_records(rows):
    return len(rows) - 1

def validate_customers(rows):
    header = rows[0].strip().split(",")
    expected_header = ["customer_id", "name", "age", "state"]

    if header != expected_header:
        return [], [{"row_number": 1, "error": "Invalid header"}]

    valid_rows = []
    validation_errors = []

    for row_number, row in enumerate(rows[1:], start=2):
        columns = row.strip().split(",")

        if len(columns) != 4:
            validation_errors.append(
                {"row_number": row_number, "error": "Invalid column count"}
            )
            continue

        customer_id, name, age, state = columns

        if not customer_id:
            validation_errors.append(
                {"row_number": row_number, "error": "Missing customer_id"}
            )
            continue

        if not name:
            validation_errors.append(
                {"row_number": row_number, "error": "Missing name"}
            )
            continue

        if not age:
            validation_errors.append(
                {"row_number": row_number, "error": "Missing age"}
            )
            continue

        if not state:
            validation_errors.append(
                {"row_number": row_number, "error": "Missing state"}
            )
            continue

        valid_rows.append(columns)

    return valid_rows, validation_errors

def run_pipeline(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    rows = read_customers(file_path)
    valid_rows, validation_errors = validate_customers(rows)

    return len(valid_rows), validation_errors


def main():
    repo_root = Path(__file__).resolve().parent.parent

    if len(sys.argv) > 1:
        data_file = Path(sys.argv[1])
    else:
        data_file = repo_root / "data" / "customers.csv"

    record_count, validation_errors = run_pipeline(data_file)

    print(f"Successfully validated {record_count} customer records.")

    if validation_errors:
        print(f"Found {len(validation_errors)} validation errors.")


if __name__ == "__main__":
    main()