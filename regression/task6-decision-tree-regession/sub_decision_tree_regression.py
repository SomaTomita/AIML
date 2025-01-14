# Decision Tree Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("regression/task6-decision-tree-regession/batters.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


#############  Training the Decision Tree Regression model on the whole dataset #############
from sklearn.tree import DecisionTreeRegressor

# the decision tree is split up to 3 times.
regressor = DecisionTreeRegressor(random_state=0, max_depth=3)
regressor.fit(X, y)

list = np.empty((10, 9))
for i in range(10):
    for j in range(9):
        list[i][j] = regressor.predict([[0.5 - i * 0.05, j]])
print(list)


############# Visualizing Decision Tree Regression results in a simple 2D colormap #############
from matplotlib.colors import ListedColormap

# Define grid range for visualization
X1 = np.linspace(0.2, 0.4, 100)  # Batting average range
X2 = np.linspace(0, 12, 100)  # Years of enrollment range
X1_grid, X2_grid = np.meshgrid(X1, X2)

# Predicting on the grid
y_pred_grid = regressor.predict(np.c_[X1_grid.ravel(), X2_grid.ravel()])
y_pred_grid = y_pred_grid.reshape(X1_grid.shape)

# Create a colormap visualization
plt.figure(figsize=(8, 6))
contour = plt.contourf(X1_grid, X2_grid, y_pred_grid, alpha=0.8, cmap="coolwarm")
plt.colorbar(contour, label="Predicted Income")

# Scatter plot for actual data points
plt.scatter(
    X[:, 0], X[:, 1], c=y, edgecolor="black", cmap="coolwarm", s=80, label="Actual Data"
)
plt.title("Decision Tree Regression Visualization")
plt.xlabel("Batting Average")
plt.ylabel("Years of Enrollment")
plt.legend()
plt.show()


# interpretation of the decision tree model:
# Since the batting average “3 or higher” was chosen as the first split criterion,
#   this indicates that this is the “most important factor determining annual income” for the model.
#     - Data points with a batting average of 0.30 or higher are placed in the red region.
#   	- Data points with a batting average of less than 0.30 and a short tenure are placed in the blue area.
#   	- Data points with a batting average of less than 0.30 and with a long tenure are placed in the light orange area.
