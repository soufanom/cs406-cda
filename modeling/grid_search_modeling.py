import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sim1 = pd.read_csv("../datasets/sim1.csv")

models = pd.DataFrame({
    'a1': np.random.uniform(-20, 40, 250),
    'a2': np.random.uniform(-5, 5, 250)
})

# I need to find which model is the best?!

def linear_model(params, dataset):
    return params[0] + params[1] * dataset['x']

def distance(params, dataset):
    diff = dataset['y'] - linear_model(params, dataset)
    dist = np.sqrt(np.sum(diff ** 2))
    return dist

models['dist'] = models.apply(lambda parameters: distance(parameters, sim1), axis=1)

top_models = models.nsmallest(10, 'dist')

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(sim1['x'], sim1['y'], s=5, color='grey')

# Plot lines for top 10 models
for index, row in top_models.iterrows():
    ax.plot(sim1['x'], row['a1'] + row['a2'] * sim1['x'], label=f"Dist: {-row['dist']:.2f}")

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(title='Top 10 models')
plt.show()