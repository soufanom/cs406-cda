import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sim1 = pd.read_csv("../datasets/sim1.csv")

# Create a DataFrame similar to the tibble in R
models = pd.DataFrame({
    'a1': np.random.uniform(-20, 40, 250),
    'a2': np.random.uniform(-5, 5, 250)
})

# Simulated data for plotting
# Assuming 'sim1' needs to have 'x' and 'y' which you might have previously defined.
# Here I'll create some dummy 'x' values and calculate 'y' based on 'a1' and 'a2'
x = np.linspace(0, 10, 250)
y = models['a1'][0] + models['a2'][0] * x  # Using the first set of coefficients as an example

plt.figure(figsize=(10, 6))

# Plot lines for each model
for index, row in models.iterrows():
    plt.plot(x, row['a1'] + row['a2'] * x, alpha=index/1000, color='black')

# Add points to the plot
sns.scatterplot(data = sim1, x='x', y='y', color='blue')  # Plotting dummy 'y' values

plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot with Multiple Models and Points')
plt.show()
