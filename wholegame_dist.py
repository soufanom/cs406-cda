import numpy as np
import matplotlib.pyplot as plt
from palmerpenguins import load_penguins
import seaborn as sns

# load the dataset
penguins = load_penguins()


# create a bar plot using sns
plt.figure(1)
sns.histplot(data = penguins, x='body_mass_g')
plt.figure(2)
subset = penguins[penguins['species'] == 'Adelie']
sns.histplot(data = subset, x='body_mass_g')

plt.figure(2)
subset = penguins[penguins['species'] == 'Gentoo']
sns.kdeplot(data = subset, x='body_mass_g', color='orange')

plt.figure(2)
subset = penguins[penguins['species'] == 'Chinstrap']
sns.kdeplot(data = subset, x='body_mass_g', color='purple')

# Count the occurrences of each species
# species_counts = penguins['species'].value_counts()
#
# # Create a bar plot
# plt.bar(species_counts.index, species_counts.values)

# Adding labels and title for clarity
plt.xlabel('Body Mass')
plt.ylabel('Count')
plt.title('Count of Penguin Species')

# Display the plot
plt.show()



