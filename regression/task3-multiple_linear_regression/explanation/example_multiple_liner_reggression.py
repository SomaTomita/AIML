import numpy as np

# model: y = 5000 + 10 * x1 - 20 * x2 + 30 * x3 + 0.5 * x4 + 0.2 * x5 + 0.3 * x6
intercept = 5000
coefficients = [10, -20, 30, 0.5, 0.2, 0.3]

# input data: [California (1,0,0), R&D Spend, Administration, Marketing Spend]
new_data = [1, 0, 0, 160000, 130000, 300000]

# manual calculation
y_manual = intercept + sum(c * x for c, x in zip(coefficients, new_data))
print(f"Predicted value (manual calculation): {y_manual}")

# Result:
# 1. Calculate the formula:
# y = 5000 + (10 × 1) + (-20 × 0) + (30 × 0) + (0.5 × 160000) + (0.2 × 130000) + (0.3 × 300000)

# 2. Calculate each term:
# - \beta_0 = 5000
# - \beta_1 × x_1 = 10 × 1 = 10
# - \beta_2 × x_2 = -20 × 0 = 0
# - \beta_3 × x_3 = 30 × 0 = 0
# - \beta_4 × x_4 = 0.5 × 160000 = 80000
# - \beta_5 × x_5 = 0.2 × 130000 = 26000
# - \beta_6 × x_6 = 0.3 × 300000 = 90000

# 3. Sum all terms:
# y = 5000 + 10 + 0 + 0 + 80000 + 26000 + 90000 = 201010


# predict
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.intercept_ = intercept
regressor.coef_ = np.array(coefficients)
y_sklearn = regressor.predict([new_data])
print(f"Predicted value (using sklearn): {y_sklearn[0]}")
