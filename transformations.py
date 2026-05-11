"""
Transformations Module
----------------------
All data transformation logic kept here, separate from the main ETL flow.
Each function does ONE clear thing — easy to test, easy to read.
"""

import pandas as pd
from datetime import datetime


def add_bonus(df, bonus_pct=0.10):
    """Add bonus column (default 10% of salary)."""
    df["bonus"] = df["salary"] * bonus_pct
    return df


def add_total_compensation(df):
    """Add total_compensation = salary + bonus."""
    df["total_compensation"] = df["salary"] + df["bonus"]
    return df


def parse_dates(df):
    """Convert join_date to datetime and extract join_year."""
    df["join_date"] = pd.to_datetime(df["join_date"])
    df["join_year"] = df["join_date"].dt.year
    return df


def add_tenure(df):
    """Calculate tenure in years from join_date till today."""
    today = pd.Timestamp(datetime.now().date())
    df["tenure_years"] = ((today - df["join_date"]).dt.days / 365).round(1)
    return df


def add_salary_band(df):
    """Categorize employees by salary band."""
    def band(salary):
        if salary >= 85000:
            return "High"
        elif salary >= 70000:
            return "Mid"
        else:
            return "Low"
    df["salary_band"] = df["salary"].apply(band)
    return df


def clean_data(df):
    """Basic data quality checks - drop nulls and duplicates."""
    initial_count = len(df)
    df = df.dropna(subset=["emp_id", "salary"])
    df = df.drop_duplicates(subset=["emp_id"])
    final_count = len(df)
    if initial_count != final_count:
        print(f"  Cleaned: removed {initial_count - final_count} bad rows")
    return df


def apply_all_transformations(df):
    """Run all transformations in sequence."""
    print("Applying transformations...")
    df = clean_data(df)
    df = add_bonus(df, bonus_pct=0.10)
    df = add_total_compensation(df)
    df = parse_dates(df)
    df = add_tenure(df)
    df = add_salary_band(df)
    print("All transformations done.")
    return df