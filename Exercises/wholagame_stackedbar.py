import matplotlib.pyplot as plt
import seaborn as sns
from palmerpenguins import load_penguins

penguins = load_penguins()

# Generating counts of gender for each island
penguins_counts = penguins.groupby(['island', 'species']).size().unstack(fill_value=0)

print(penguins_counts)

penguins_counts.plot(kind='bar', stacked=True,title= 'Number of Penguins by Island and Species')

plt.show()

