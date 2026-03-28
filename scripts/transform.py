import pandas as pd
import logging

def transform_data(df):
    logging.info("Starting transformation")

    df['Total_Charges'] = pd.to_numeric(df['Total_Charges'], errors='coerce')
    df['Total_Charges'] = df['Total_Charges'].fillna(df['Total_Charges'].median())

    df.drop_duplicates(inplace=True)

    def tenure_group(x):
        if x < 3:
            return "0-3 Months"
        elif x < 12:
            return "3-12 Months"
        else:
            return "12+ Months"

    df['tenure_group'] = df['Tenure_Months'].apply(tenure_group)

    df['is_monthly'] = df['Contract'].apply(
        lambda x: 1 if x == "Month-to-month" else 0
    )

    logging.info("Transformation completed")

    return df