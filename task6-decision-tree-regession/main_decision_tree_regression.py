# Decision Tree Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("task6-decision-tree-regession/Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Why feature scaling is not required in Decision Tree Regression :
# Decision trees split data based on thresholds in the feature space
# They focus on reducing the variance within splits by grouping similar target values together, independent of feature scales.


#############  Training the Decision Tree Regression model on the whole dataset #############
from sklearn.tree import DecisionTreeRegressor

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

# Predicting a new result
regressor.predict([[6.5]])

#############  Visualising the Decision Tree Regression results (higher resolution) #############
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("Truth or Bluff (Decision Tree Regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()
