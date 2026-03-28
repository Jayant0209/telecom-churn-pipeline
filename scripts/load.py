import sqlite3
import logging

def load_data(df):
    logging.info("Loading data into database")

    conn = sqlite3.connect("churn.db")

    df.to_sql("customer_churn", conn, if_exists="replace", index=False)

    conn.close()

    logging.info("Data loaded successfully")