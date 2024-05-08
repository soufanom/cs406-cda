import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor

data = pd.read_csv('../datasets/sim2.csv')

X = np.asarray(data['x']).reshape(-1, 1)
y = data['y']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = GaussianProcessRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

plt.figure(figsize=(10, 12))

x_range = np.linspace(X_train.min(), X_train.max(), 1000).reshape(-1, 1)
plt.scatter(x = X_train, y= y_train, color='black')
plt.scatter(x = x_range, y= model.predict(x_range), color='orange')

plt.show()

