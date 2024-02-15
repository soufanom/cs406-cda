import numpy as np
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins

# load the dataset
penguins = load_penguins()

for selected_species in penguins['species'].unique():
    subset = penguins[penguins['species'] == selected_species]
    x = subset['flipper_length_mm']
    y = subset['body_mass_g']
    # generate main plot
    plt.scatter(x, y, label=selected_species)

# customize or enhance the plot
plt.title('Body mass and flipper lenght')
plt.xlabel('Flipper lenght')
plt.ylabel('Body mass')

plt.legend(title="Species")

plt.show()