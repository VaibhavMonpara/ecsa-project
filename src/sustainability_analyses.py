import pandas as pd

# Load cleaned data
cleaned_data_path = '/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/processed/cleaned_renewable_energy_consumption.csv'
rec_data = pd.read_csv(cleaned_data_path)

# Example sustainability analysis: Energy usage by sector
sector_energy_usage = rec_data.groupby('Sector')['Total Renewable Energy'].sum().reset_index()
sector_energy_usage.columns = ['Sector', 'Energy_Usage']

# Save sustainability results
sector_energy_usage.to_csv('/Users/vaibhavmonpara/Documents/GitHub/ecsa-project/data/visualization/sustainability_results.csv', index=False)

print("Sustainability results saved.")
