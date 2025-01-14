# Random Forest Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("regression/task7-randam-forest-regression/Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


############# Training the Random Forest Regression model on the whole dataset #############
from sklearn.ensemble import RandomForestRegressor

# In this case, the forecast is made by constructing 10 decision trees and averaging the results.
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)

# Predicting a new result
print("regressor.predict([[6.5]] : ", regressor.predict([[6.5]]))


############# Visualising the Random Forest Regression results (higher resolution) #############
X_grid = np.arange(
    min(X), max(X), 0.1
)  # Generates the minimum to maximum value of X in small increments (0.1 increments)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Truth or Bluff (Random Forest Regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()
