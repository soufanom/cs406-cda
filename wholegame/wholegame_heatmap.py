import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from palmerpenguins import load_penguins

# load the dataset
penguins = load_penguins()

# clean the data using basic filtering
penguins_numeric = penguins.select_dtypes(include=[np.number]).dropna()
penguins_numeric = penguins_numeric.drop("year", axis=1)

# apply min-max normalization
penguins_numeric_min = penguins_numeric.min()

corr = penguins_numeric.corr()

penguins_numeric = (penguins_numeric - penguins_numeric_min)/(penguins_numeric.max() - penguins_numeric_min)

# create heatmap
sns.heatmap(corr, annot=True, cmap="viridis")

plt.show()