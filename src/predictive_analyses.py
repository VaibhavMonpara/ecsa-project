import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load cleaned data
cleaned_data_path = '/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/processed/cleaned_renewable_energy_consumption.csv'
rec_data = pd.read_csv(cleaned_data_path)

# Feature Engineering (Extracting relevant features)
# rec_data['Year'] = pd.to_datetime(rec_data['Date']).dt.year
# rec_data['Month'] = pd.to_datetime(rec_data['Date']).dt.month

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
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')
