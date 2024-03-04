import pandas as pd

# Data for creating DataFrame
data = {
    'Product': ['Apples', 'Oranges', 'Bananas', 'Strawberries', 'Grapes'],
    'Sales': [230, 150, 300, 220, 170],
    'Price': [1.20, 0.80, 0.50, 1.50, 2.00]
}

# Task 1: Create a DataFrame
# First, you need to create a pandas DataFrame from the following data. Fill in the missing lines to complete the DataFrame creation.
# Hint: Use the pd.DataFrame() constructor to create a new DataFrame.
# TODO: Create a DataFrame from the above data
df = ____________(data)

print(df)

# Task 2: Add a 'Revenue' Column
# Calculate the revenue (Sales * Price) for each product and add this as a new column in the DataFrame.
# Hint: You can calculate the revenue by multiplying the 'Sales' and 'Price' columns.
# TODO: Calculate Revenue for each product and add it as a new column
df['Revenue'] = ____________

print(df)

# Task 3: Group Data by Product
# Group the data by 'Product' and calculate the total sales and average price for each product. Fill in the missing lines to complete the grouping and aggregation.
# Hint: Use the agg() function with a dictionary specifying the operations for each column, e.g., {'Sales': 'sum', 'Price': 'mean'}.
# TODO: Group the data by 'Product' and calculate total sales and average price
grouped_data = df.groupby('Product').agg(__________)

print(grouped_data)

# Task 4: Filter Data
# Filter the original DataFrame to show only products with sales greater than 200.
# Hint: Use a boolean condition inside the DataFrame indexing, e.g., df[df['Sales'] > 200].
# TODO: Filter the DataFrame to show only products with sales greater than 200
filtered_data = df[__________]

print(filtered_data)

