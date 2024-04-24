import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sim2 = pd.read_csv("../datasets/sim2.csv")

# Linear model: lm(y ~ x, data = sim1)
sim2['x2'] = sim2['x'] ** 2
sim2['x3'] = sim2['x'] ** 3
sim2['x4'] = sim2['x'] ** 4
model1 = smf.ols('y ~ x + x2 + x3 + x4', data=sim2).fit()

# ploting
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(sim2['x'], sim2['y'], s=5, color='blue')

# calculate the predicted values and then, plot the values
min = sim2['x'].min()
max = sim2['x'].max()
x_range = np.linspace(min, max, 100)
predictions = model1.predict(exog=dict(x=x_range, x2 = x_range ** 2, x3 = x_range ** 3, x4 = x_range ** 4))

ax.plot(x_range, predictions, color='red')

ax.set_xlabel('x - independent variable')
ax.set_ylabel('y - dependent variable')

plt.show()
