import pandas as pd
import numpy as np
from palmerpenguins import load_penguins

# load the dataset
penguins = load_penguins()
print(penguins)
# Data Cleaning
print(penguins.isnull())  # Identify missing values
df_filled = penguins.ffill()  # Fill missing values forward
df_dropped = penguins.dropna()  # Drop rows with any missing values

# Data Filtering
filtered_df = penguins[penguins['flipper_length_mm'] > 200]  # Filter rows
query_df = penguins.query('flipper_length_mm > 200')  # Using query method

# Data Transformation
# Convert flipper length from mm to cm
penguins['flipper_length_cm'] = penguins['flipper_length_mm'].apply(lambda x: x / 10)
# Map species names to a simplified version
penguins['species_long'] = penguins['species'].map({'Adelie': 'Adelie Penguin (Pygoscelis adeliae)',
                                         'Chinstrap' : 'Chinstrap penguin (Pygoscelis antarctica)',
                                         'Gentoo' : 'Gentoo penguin (Pygoscelis papua)'})

print(penguins)
# Grouping and Aggregating Data
# Group data by species
grouped = penguins.groupby('species')
# Aggregate data after grouping
agg_penguins = grouped.agg({'body_mass_g': ['mean', 'median'], 'flipper_length_mm': ['mean', 'median']})

# Merging and Joining DataFrames
# Creating another example DataFrame for demonstration
island_data = {
    'island': ['Torgersen', 'Biscoe', 'Dream'],
    'ice_coverage': [30, 20, 45]  # hypothetical data
}
penguins2 = pd.DataFrame(island_data)
# Merging DataFrames on a common column
merged_df = pd.merge(penguins, penguins2, on='island')
print(merged_df)
# Joining DataFrames
joined_df = penguins.join(penguins2.set_index('island'), on='island')

# Display the final joined DataFrame
print(joined_df)

# Assuming 'df' is your DataFrame and 'flipper_length_mm' is one of the columns
# Fill missing values in 'flipper_length_mm' column with the column's average
average_flipper_length = penguins['flipper_length_mm'].mean()
penguins['flipper_length_mm'] = penguins['flipper_length_mm'].fillna(average_flipper_length)

# Assuming 'df' is your DataFrame
# Fill missing values in each column with that column's average
df = penguins.apply(lambda x: x.fillna(x.mean()) if x.dtype.kind in 'biufc' else x)
print(df['body_mass_g'])