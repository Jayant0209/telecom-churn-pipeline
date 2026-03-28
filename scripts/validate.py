def validate_data(df):

    # 1. Check if data is empty
    if df.shape[0] == 0:
        raise ValueError("Dataset is empty")

    # 2. Required columns check
    required_columns = ['Tenure_Months', 'Contract', 'Churn_Label']

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # 3. Check null values
    if df['Tenure_Months'].isnull().sum() > 0:
        raise ValueError("Null values found in Tenure_Months")

    # 4. Check invalid values
    if (df['Tenure_Months'] < 0).any():
        raise ValueError("Invalid tenure values found")

    print("Data validation passed")