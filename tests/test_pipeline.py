from pathlib import Path

from src.pipeline import read_customers, count_customer_records, run_pipeline


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

    record_count = run_pipeline(data_file)

    assert record_count == 3