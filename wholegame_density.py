import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
import seaborn as sns

# load the dataset
penguins = load_penguins()

# Create density plots
plt.figure(figsize=(8, 6))  # Optional: Adjust figure size
for species in penguins['species'].unique():
    subset = penguins[penguins['species'] == species]
    sns.kdeplot(data=subset, x='body_mass_g', fill=True, alpha=0.2, label=species)

# Add legend and show the plot
plt.legend(title='Species')
plt.show()