import logging
from extract import extract_data
from transform import transform_data
from load import load_data
from validate import validate_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("Pipeline started")

    df = extract_data("data/raw/telco.csv")

    validate_data(df)

    df = transform_data(df)

    load_data(df)

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()