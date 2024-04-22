import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sim1 = pd.read_csv("../datasets/sim1.csv")

# Define and fit the linear model using patsy formula
model = smf.ols('y ~ x', data=sim1).fit()

# Retrieve the coefficients
coefficients = model.params

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(sim1['x'], sim1['y'], s=5, color='grey')

# Plot lines for top 10 models
ax.plot(sim1['x'], coefficients[0] + coefficients[1] * sim1['x'])

ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()