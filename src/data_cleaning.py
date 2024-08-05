import data_loading

def clean_data(df):
    """Cleans the data by handling missing values and outliers."""

    # Dropping rows with missing values
    df = df.dropna()
    # Dropping columns with missing values
    df = df.dropna(axis=1)
    # Dropping duplicate rows
    df = df.drop_duplicates()

    return df

cleaned_rec_data = clean_data(data_loading.renewable_energy_consumption_data)

cleaned_rec_data.to_csv('/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/processed/cleaned_renewable_energy_consumption.csv', index=False)
