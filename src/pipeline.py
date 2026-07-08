from pathlib import Path
import sys


def read_customers(file_path):
    with open(file_path, "r") as file:
        rows = file.readlines()

    return rows


def count_customer_records(rows):
    return len(rows) - 1


def run_pipeline(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    rows = read_customers(file_path)
    record_count = count_customer_records(rows)

    return record_count


def main():
    repo_root = Path(__file__).resolve().parent.parent

    if len(sys.argv) > 1:
        data_file = Path(sys.argv[1])
    else:
        data_file = repo_root / "data" / "customers.csv"

    record_count = run_pipeline(data_file)

    print(f"Successfully read {record_count} customer records.")


if __name__ == "__main__":
    main()