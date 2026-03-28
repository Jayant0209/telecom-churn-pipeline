from extract import extract_data
from transform import transform_data
from load import load_data
from validate import validate_data

def run_pipeline():
    df = extract_data("data/raw/telco.csv")

    validate_data(df)

    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_pipeline()


