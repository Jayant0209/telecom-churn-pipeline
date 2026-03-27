import pandas as pd
import sqlite3
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Step 1: Extract
    logging.info("Reading data...")
    df = pd.read_csv("data/raw/telco.csv")

    # 🔥 Fix column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    logging.info(f"Columns: {df.columns.tolist()}")
    logging.info(f"Initial shape: {df.shape}")

    # Step 2: Transform

    # Convert numeric columns
    df['Total_Charges'] = pd.to_numeric(df['Total_Charges'], errors='coerce')
    df['Monthly_Charges'] = pd.to_numeric(df['Monthly_Charges'], errors='coerce')

    # Handle missing values
    df['Total_Charges'] = df['Total_Charges'].fillna(df['Total_Charges'].median())

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # 🔥 Feature Engineering

    # Tenure Group
    def tenure_group(x):
        if x < 3:
            return "0-3 Months"
        elif x < 12:
            return "3-12 Months"
        else:
            return "12+ Months"

    df['tenure_group'] = df['Tenure_Months'].apply(tenure_group)

    # Contract flag
    df['is_monthly'] = df['Contract'].apply(
        lambda x: 1 if x == "Month-to-month" else 0
    )

    logging.info("Transformation completed")

    # Step 3: Load
    conn = sqlite3.connect("churn.db")

    df.to_sql("customer_churn", conn, if_exists="replace", index=False)

    conn.close()

    logging.info("Data successfully loaded into SQLite")

except Exception as e:
    logging.error(f"Error occurred: {e}")