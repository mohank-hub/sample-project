"""
Main ETL Job
"""

import pandas as pd
import sqlite3
import os
from transformations import apply_all_transformations


# ---------- Configuration ----------
INPUT_FILE = "data/employees_input.csv"
DB_FILE = "data/employees.db"
SQL_FOLDER = "sql"
OUTPUT_FOLDER = "output"


def extract(file_path):
    print(f"\n[EXTRACT] Reading {file_path}")
    df = pd.read_csv(file_path)
    print(f"  Records read: {len(df)}")
    return df


def transform(df):
    print(f"\n[TRANSFORM]")
    df = apply_all_transformations(df)
    print(f"  Final columns: {list(df.columns)}")
    return df


def load_to_db(df, db_file, table_name="employees"):
    print(f"\n[LOAD] Writing to SQLite DB: {db_file}")
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    print(f"  Loaded {len(df)} rows into table '{table_name}'")


def read_sql_file(sql_path):
    with open(sql_path, "r") as f:
        return f.read()


def run_query(db_file, sql_query):
    conn = sqlite3.connect(db_file)
    result = pd.read_sql_query(sql_query, conn)
    conn.close()
    return result


def write_output(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"  Saved {len(df)} rows -> {output_path}")


def run_all_reports(db_file):
    print(f"\n[REPORTS] Running SQL queries from {SQL_FOLDER}/")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    reports = [
        ("high_earners.sql", "high_earners.csv"),
        ("department_summary.sql", "department_summary.csv"),
        ("tenure_analysis.sql", "tenure_analysis.csv"),
    ]

    for sql_file, out_csv in reports:
        sql_path = os.path.join(SQL_FOLDER, sql_file)
        out_path = os.path.join(OUTPUT_FOLDER, out_csv)
        print(f"\n  Running: {sql_file}")
        query = read_sql_file(sql_path)
        result = run_query(db_file, query)
        write_output(result, out_path)


def main():
    print("=" * 60)
    print("ETL JOB STARTED")
    print("=" * 60)

    df = extract(INPUT_FILE)
    df = transform(df)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    full_output = os.path.join(OUTPUT_FOLDER, "employees_transformed.csv")
    df.to_csv(full_output, index=False)
    print(f"\n[OUTPUT] Full transformed data -> {full_output}")

    load_to_db(df, DB_FILE)
    run_all_reports(DB_FILE)

    print("\n" + "=" * 60)
    print("ETL JOB COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()