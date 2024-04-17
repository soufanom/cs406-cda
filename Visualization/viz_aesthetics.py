import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

mpg = pd.read_csv("../datasets/mpg.csv")

plt.figure(figsize=(12, 6))

print(mpg['class'])
unique_valus, encoded_labels = np.unique(mpg['class'], return_inverse=True)
print(encoded_labels)
#encoded_labels = np.unique(mpg['class'], return_inverse=True)
#encoded_labels = encoded_labels / 10
#sns.scatterplot(data=mpg, x='displ', y='hwy', alpha=encoded_labels)

#plt.show()
