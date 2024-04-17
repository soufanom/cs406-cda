import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
atlantic_cases = pd.read_csv("Datasets/13100775.csv")

# Set the style to mimic ggplot2 from R
sns.set(style="whitegrid")

# Create a boxplot with ggplot2-like aesthetics
plt.figure(figsize=(10, 6))
boxplot = sns.boxplot(x='Exposure', y='Cases', hue='Age', data=atlantic_cases, palette="muted")

# Set plot title and labels with more customization
plt.title('COVID-19 Exposures in the Atlantic', fontsize=16)
plt.xlabel('Exposure', fontsize=14)
plt.ylabel('Cases', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Improve legend aesthetics
plt.legend(title='Age', title_fontsize='13', fontsize='12')

# Show the plot
plt.show()
