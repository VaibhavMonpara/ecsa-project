import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def analyses(rec_data):
    # Define features and target
    X = rec_data[['Year', 'Month']]
    y = rec_data['Total Renewable Energy']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)

    # Evaluate model performance
    return mean_squared_error(y_test, predictions)
    

# Load cleaned data
cleaned_data_path = '/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/processed/cleaned_renewable_energy_consumption.csv'
renewable_energy_consumption_data = pd.read_csv(cleaned_data_path)


# Prepare data for prediction (example)
X = renewable_energy_consumption_data[['Year', 'Month']]
y = renewable_energy_consumption_data['Total Renewable Energy']

model = LinearRegression()
model.fit(X, y)
renewable_energy_consumption_data['Prediction'] = model.predict(X)

# Creating a new column by combining year and month
renewable_energy_consumption_data['Date'] = pd.to_datetime(renewable_energy_consumption_data[['Year', 'Month']].assign(day=1))

# Save predictive results
renewable_energy_consumption_data[['Date', 'Prediction']].to_csv('/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/visualization/predictive_results.csv', index=False)

print("Predictive results saved.")
mes = analyses(renewable_energy_consumption_data)