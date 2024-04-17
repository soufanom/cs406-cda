import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
atlantic_cases = pd.read_csv("Datasets/13100775.csv")

# Create a boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Exposure', y='Cases', hue='Age', data=atlantic_cases)

# Set plot title and labels
plt.title('COVID-19 Exposures in the Atlantic')
plt.xlabel('Exposure')
plt.ylabel('Cases')

# Show the plot
plt.show()