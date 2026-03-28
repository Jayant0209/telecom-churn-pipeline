import sqlite3

def load_data(df):
    conn = sqlite3.connect("churn.db")

    df.to_sql("customer_churn", conn, if_exists="replace", index=False)

    conn.close()

    print("Data loaded into database")