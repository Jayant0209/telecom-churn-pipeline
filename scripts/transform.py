import pandas as pd
def transform_data(df):
    
    # Convert to numeric first
    df['Total_Charges'] = pd.to_numeric(df['Total_Charges'], errors='coerce')

    # Then handle missing values
    df['Total_Charges'] = df['Total_Charges'].fillna(df['Total_Charges'].median())

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Feature Engineering
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

    print("Transformation completed")
    return df