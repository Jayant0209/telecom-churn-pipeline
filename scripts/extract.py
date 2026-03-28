import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)

    # Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    print("Data extracted successfully")
    return df