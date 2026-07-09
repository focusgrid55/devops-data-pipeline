from pathlib import Path

from src.pipeline import read_customers, count_customer_records, run_pipeline,validate_customers

def test_read_customers_returns_all_rows():
    repo_root = Path(__file__).resolve().parent.parent
    data_file = repo_root / "data" / "customers.csv"

    rows = read_customers(data_file)

    assert len(rows) == 4
    assert rows[0] == "customer_id,name,age,state\n"


def test_count_customer_records_excludes_header():
    rows = [
        "customer_id,name,age,state\n",
        "1,Alice,25,OH\n",
        "2,Bob,17,TX\n",
        "3,Charlie,42,CA\n",
    ]

    record_count = count_customer_records(rows)

    assert record_count == 3
    
def test_run_pipeline_returns_customer_count():
    repo_root = Path(__file__).resolve().parent.parent
    data_file = repo_root / "data" / "customers.csv"

    record_count , validation_errors = run_pipeline(data_file)


    assert record_count == 3
    assert validation_errors == []

def test_validate_customers_returns_errors_for_invalid_rows():
    rows = [
        "customer_id,name,age,state\n",
        "1,Alice,25,OH\n",
        "2,Bob,,TX\n",
        "3,Charlie,42\n",
        "4,,35,CA\n",
    ]

    valid_rows, validation_errors = validate_customers(rows)

    assert len(valid_rows) == 1
    assert len(validation_errors) == 3
    assert validation_errors[0] == {"row_number": 3, "error": "Missing age"}
    assert validation_errors[1] == {"row_number": 4, "error": "Invalid column count"}
    assert validation_errors[2] == {"row_number": 5, "error": "Missing name"}