"""
Simple ETL Script
-----------------
Reads: employees_input.csv
Transforms: adds bonus column, filters high earners
Writes: employees_output.csv (all data with bonus)
        high_earners.csv (only employees earning > 70000)
"""

import pandas as pd
import os

# ---------- Step 1: Define file paths ----------
INPUT_FILE = "employees_input.csv"
OUTPUT_FILE_ALL = "EMP_output.csv"
OUTPUT_FILE_HIGH = "high_earners_7K.csv"


# ---------- Step 2: Read the input file ----------
def read_data(file_path):
    print(f"Reading file: {file_path}")
    df = pd.read_csv(file_path)
    print(f"Total records read: {len(df)}")
    return df


# ---------- Step 3: Transform the data ----------
def transform_data(df):
    print("Transforming data...")

    # Add a bonus column (10% of salary)
    df["bonus"] = df["salary"] * 0.10

    # Add total compensation column
    df["total_compensation"] = df["salary"] + df["bonus"]

    # Convert join_date to datetime and extract year
    df["join_date"] = pd.to_datetime(df["join_date"])
    df["join_year"] = df["join_date"].dt.year

    print("Transformation complete.")
    return df


# ---------- Step 4: Write the output files ----------
def write_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Written {len(df)} records to: {output_path}")


# ---------- Step 5: Main flow ----------
def main():
    print("=" * 50)
    print("Starting ETL Job")
    print("=" * 50)

    # Read
    df = read_data(INPUT_FILE)

    # Transform
    df_transformed = transform_data(df)

    # Write all employees to output file
    write_data(df_transformed, OUTPUT_FILE_ALL)

    # Filter and write high earners (salary > 70000)
    high_earners = df_transformed[df_transformed["salary"] > 70000]
    write_data(high_earners, OUTPUT_FILE_HIGH)

    print("=" * 50)
    print("ETL Job Completed Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()
