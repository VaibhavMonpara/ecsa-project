import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
cleaned_data_path = '/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/processed/cleaned_renewable_energy_consumption.csv'
rec_data = pd.read_csv(cleaned_data_path)
print(rec_data.head())

# Creating a new column by combining year and month
rec_data['Date'] = pd.to_datetime(rec_data[['Year', 'Month']].assign(day=1))

print(rec_data[['Year', 'Month']].head())

# Converting date column to datetime
rec_data['Date'] = pd.to_datetime(rec_data['Date'])

# Plot renewable energy production over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Total Renewable Energy', data=rec_data)
plt.title('Renewable Energy Production Over Time')
plt.xlabel('Date')
plt.ylabel('Energy Production (MWh)')
plt.grid(True)
plt.show()
