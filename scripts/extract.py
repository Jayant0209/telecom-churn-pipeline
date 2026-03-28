import pandas as pd
import logging

def extract_data(path):
    logging.info("Extracting data...")

    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    logging.info(f"Data extracted with shape: {df.shape}")

    return df