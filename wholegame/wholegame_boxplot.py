import matplotlib.pyplot as plt
import seaborn as sns
from palmerpenguins import load_penguins

penguins = load_penguins()

species_order = penguins.groupby('species')['body_mass_g'].median().sort_values(ascending=False).index

print(species_order)
plt.figure()

sns.boxplot(data = penguins, x = 'species', y = 'body_mass_g', hue='species', order = species_order)

plt.show()