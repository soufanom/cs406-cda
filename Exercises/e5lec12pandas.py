import pandas as pd

# Task 1: Create a DataFrame from dictionary
# Data for creating DataFrame
data = {
    'Product': ['Apples', 'Oranges', 'Bananas', 'Strawberries', 'Grapes'],
    'Sales': [230, 150, 300, 220, 170],
    'Price': [1.20, 0.80, 0.50, 1.50, 2.00]
}

# TODO: Create a DataFrame from the above data
# Hint: Use the pd.DataFrame() constructor to create a new DataFrame.
# Complete the code below to create a DataFrame.
df = __________(data)

print("DataFrame from dictionary:")
print(df)
print("\n")  # Adding new line for better readability

# Task 2: Read data from a CSV file into a DataFrame
# Suppose you have a CSV file 'sales_data.csv' with the same structure as the 'data' dictionary.
# TODO: Read the CSV file into a DataFrame
# Hint: Use the pd.read_csv() method.; also, you can store the previous dataframe using df.to_save
# Complete the code below to read the CSV file.
df_csv = pd.read_csv(__________)  # Fill in the missing part to read 'sales_data.csv'

print("DataFrame from CSV file:")
print(df_csv)
print("\n")

# Task 3: Apply a function to the 'Sales' column using the map() function
# Let's say you want to add 10% tax to each sale.
# TODO: Create a function that adds 10% tax to a sale and then use the map function to apply it.
# Define your function here
def add_tax(__________):
    return __________ * 1.10

# Apply the function to the 'Sales' column
# Hint: use map()
df['Sales with Tax'] = df['Sales'].__________

print("DataFrame after applying tax using map():")
print(df)
print("\n")

# Task 4: Use apply() to subtract 5 units from each 'Sales' value
# TODO: Write a lambda function to perform this and use the apply method.
# Hint: the format of the Lambda function is lambda x:expression(x)
df['Sales after deduction'] = df['Sales'].apply(__________)

print("DataFrame after applying deduction using apply():")
print(df)
print("\n")

# Task 5: Stack and unstack the DataFrame
# TODO: Stack and then unstack the DataFrame and print the result.
stacked_df = df.__________
unstacked_df = stacked_df.__________

print("DataFrame after stacking and unstacking:")
print(unstacked_df)
print("\n")

# Task 6: Join, merge, and concat different DataFrames
# Suppose you have another DataFrame with additional information.
extra_data = {
    'Product': ['Apples', 'Oranges', 'Bananas'],
    'Category': ['Fruit', 'Citrus', 'Tropical']
}
extra_df = pd.DataFrame(extra_data)

# TODO: Perform an inner join of df and extra_df on the 'Product' column.
joined_df = df.merge(__________, on='Product', how='inner')

print("DataFrame after joining:")
print(joined_df)
print("\n")

# TODO: Concatenate df and a new row.
# Hint: Create a new DataFrame with the same columns as df and then use pd.concat.
new_row = pd.DataFrame({'Product': ['Peaches'], 'Sales': [95], 'Price': [1.80]})
concatenated_df = pd.concat([df, __________], ignore_index=True)

print("DataFrame after concatenation:")
print(concatenated_df)
print("\n")

# Task 7: Reshape data using pivot
# Suppose your df_csv has another column 'Year' with all values as '2022'. Convert this 'Year' column as part of the multi-index using pivot.
# TODO: Create a new DataFrame with 'Year', 'Product' as the index and 'Sales' as the values using pivot.
# Note: First add a 'Year' column to df_csv for demonstration.
df_csv['Year'] = 2022
pivot_df = df_csv.pivot(index='Year', columns='Product', values='Sales')

print("DataFrame after reshaping using pivot:")
print(pivot_df)