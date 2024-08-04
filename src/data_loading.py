import os
import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)

# Getting the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Defining the relative path to the data file
relative_ers_path = '../data/raw/electricity_retail_sales.csv'
relative_rec_path = '../data/raw/renewable_energy_consumption.csv'

# Constructing the absolute path
ers_path = os.path.join(script_dir, relative_ers_path)
rec_path = os.path.join(script_dir, relative_rec_path)

electricity_retail_sales_data = load_data(ers_path)
renewable_energy_consumption_data = load_data(rec_path)
