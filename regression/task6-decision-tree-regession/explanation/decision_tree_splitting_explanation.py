import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

# dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([100, 200, 300, 400, 500])

regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

predicted_value = regressor.predict([[3.5]])
print(f"predicted value: {predicted_value}")


# Visualising the Decision Tree Regression results
X_grid = np.arange(min(X), max(X) + 1, 0.01).reshape(-1, 1)
plt.scatter(X, y, color="red", label="actual value")
plt.plot(X_grid, regressor.predict(X_grid), color="blue", label="model prediction")
plt.title("decision tree ")
plt.xlabel("input data (X)")
plt.ylabel("target data (y)")
plt.legend()
plt.show()


# Decision Tree Regression: How are the splitting ranges (e.g., X ≤ 1.5 → y = 100) determined?

# 1. Splitting based on the training data:
# DecisionTreeRegressor splits the data by finding the optimal "thresholds" for the input features (X)
# such that the target variable (y) variance within each split is minimized. This process happens
# recursively until a stopping criterion is met (e.g., max_depth, min_samples_split).

# Example:
# Let's assume we have the following training data:
# X = [1, 2, 3, 4, 5]
# y = [100, 200, 300, 400, 500]
#
# Step-by-step splitting:
# - The decision tree will first try to split the data at various points (e.g., X ≤ 1.5, X ≤ 2.5, etc.)
#   and calculate the "Mean Squared Error (MSE)" reduction for each split.
# - For example:
#   - If the split is X ≤ 1.5:
#     - Group 1: X = [1], y = [100] → MSE = 0 (only one value, so no variance)
#     - Group 2: X = [2, 3, 4, 5], y = [200, 300, 400, 500] → Variance exists here
#   - The decision tree evaluates all possible splits and chooses the one with the best reduction in MSE.

# 2. How the ranges (intervals) are created:
# - Once the optimal split is chosen, the decision tree creates two branches (one for each side of the split).
# - This process repeats recursively for each branch, splitting further into smaller intervals until
#   the stopping criterion is reached.
# - In this case, the tree might create intervals like this:
#   - X ≤ 1.5 → Predict y = 100
#   - 1.5 < X ≤ 2.5 → Predict y = 200
#   - 2.5 < X ≤ 3.5 → Predict y = 300
#   - ...

# 3. How regressor.predict works:
# - When you call `regressor.predict([[3.5]])`, the decision tree checks which interval the input (3.5) belongs to.
# - In this case:
#   - 3.5 belongs to the interval 2.5 < X ≤ 3.5.
# - The tree predicts the value for this interval, which is the average of y values in this interval.
# - For example:
#   - If the training data for this interval was y = [300], the prediction is the mean: (300) = 300.
#   - If there were multiple values (e.g., y = [290, 310]), the prediction would be the mean: (290 + 310) / 2 = 300.

# 4. Why the prediction produces a "stair-step" pattern:
# - DecisionTreeRegressor assigns a constant predicted value (mean of y) for each interval (split).
# - When visualizing, this creates a stair-step pattern, as the prediction is the same for all values within
#   each interval, and it abruptly changes at the split points.

# 5. Visualization (in your code):
# - `plt.plot(X_grid, regressor.predict(X_grid), color="blue")` plots these constant predictions for each interval
#   based on the `X_grid` input.
# - The result is a step-like curve showing the predictions for all possible input values.
