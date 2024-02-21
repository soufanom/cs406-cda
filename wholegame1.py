import numpy as np
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
import seaborn as sns

# load the dataset
penguins = load_penguins()

for selected_species in penguins['species'].unique():
    subset = penguins[penguins['species'] == selected_species]
    # generate main plot
    sns.regplot(data = subset, x = 'flipper_length_mm', y = 'body_mass_g', lowess=True, label=selected_species)

# customize or enhance the plot
plt.title('Body mass and flipper lenght')
plt.xlabel('Flipper lenght')
plt.ylabel('Body mass')

plt.legend(title="Species")

plt.show()