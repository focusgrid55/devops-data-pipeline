from pathlib import Path

def read_customers(file_path):
    with open(file_path, "r") as file:
        rows = file.readlines()

    return rows


def main():
    repo_root = Path(__file__).resolve().parent.parent
    data_file = repo_root / "data" / "customers.csv"

    if not data_file.exists():
        raise FileNotFoundError(f"Data file not found: {data_file}")

    rows = read_customers(data_file)

    print(f"Successfully read {len(rows) - 1} customer records.")


if __name__ == "__main__":
    main()