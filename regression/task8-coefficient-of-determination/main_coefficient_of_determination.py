# The coefficient of determination indicates how small the difference (error) between the observed and predicted data is relative to the variability (variance) of the overall data.
# → Simply put, it is an indicator that measures “how well the predictions made by the model fit the original data.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# from sklearn.metrics import r2_score

# # Generate synthetic data
# np.random.seed(42)
# x = np.linspace(0, 10, 100).reshape(-1, 1)  # Independent variable
# y_good_fit = 3 * x + 5 + np.random.normal(scale=1, size=x.shape)  # Well-fitted data
# y_poor_fit = 3 * x + 5 + np.random.normal(scale=5, size=x.shape)  # Poorly-fitted data

# # Fit linear regression models
# model_good = LinearRegression()
# model_poor = LinearRegression()
# model_good.fit(x, y_good_fit)
# model_poor.fit(x, y_poor_fit)

# # Predictions
# y_good_pred = model_good.predict(x)
# y_poor_pred = model_poor.predict(x)

# # Calculate R^2
# r2_good = r2_score(y_good_fit, y_good_pred)
# r2_poor = r2_score(y_poor_fit, y_poor_pred)

# # Create a summary table
# data = {
#     "Dataset": ["Well-fitted data", "Poorly-fitted data"],
#     "R^2 Value": [r2_good, r2_poor],
#     "Model Slope": [model_good.coef_[0][0], model_poor.coef_[0][0]],
#     "Model Intercept": [model_good.intercept_[0], model_poor.intercept_[0]],
# }
# summary_table = pd.DataFrame(data)

# # Display
# print(summary_table)

# plt.figure(figsize=(12, 6))

# plt.subplot(1, 2, 1)
# plt.scatter(x, y_good_fit, label="Data (Good Fit)", alpha=0.7)
# plt.plot(x, y_good_pred, color="red", label="Model (Good Fit)")
# plt.title("Well-Fitted Data")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()

# plt.subplot(1, 2, 2)
# plt.scatter(x, y_poor_fit, label="Data (Poor Fit)", alpha=0.7)
# plt.plot(x, y_poor_pred, color="red", label="Model (Poor Fit)")
# plt.title("Poorly-Fitted Data")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()

# plt.tight_layout()
# plt.show()


############# R^2 Calculation #############
# Fixed seed value (Using the same seed value will ensure that the random number sequence generated will always be the same.)
np.random.seed(42)
# Generate 100 independent variables evenly ranging from 0 to 10
x = np.linspace(0, 10, 100).reshape(-1, 1)
# Generate dependent variables with a linear relationship (y = 3x + 5) and add noise
y = 3 * x + 5 + np.random.normal(scale=3, size=x.shape)


# Calculate mean of observed data
y_mean = np.mean(y)

# Fit a linear regression model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)


# Calculate components of variation
SST = np.sum((y - y_mean) ** 2)  # Total variation (SST)
SSR = np.sum((y_pred - y_mean) ** 2)  # Regression variation (SSR)
SSE = np.sum((y - y_pred) ** 2)  # Residual variation (SSE)


# Calculate R^2
R2 = SSR / SST
# or
R2_alternative = 1 - (SSE / SST)

# Explanation: R^2 as a ratio of explained variation
assert np.isclose(SST, SSR + SSE), "The relationship SST = SSR + SSE must hold."


# Visualization
plt.figure(figsize=(12, 6))
# Scatter plot of observed data
plt.scatter(x, y, label="Observed Data", alpha=0.7)
# Plot regression line
plt.plot(x, y_pred, color="red", label="Regression Line")
# Plot mean line
plt.axhline(y_mean, color="green", linestyle="--", label="Mean Line")
plt.title("Decomposition of Variations (SST, SSR, SSE)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


# Print the breakdown
print(f"Total Variation (SST): {SST:.2f}")
print(f"Regression Variation (SSR): {SSR:.2f}")
print(f"Residual Variation (SSE): {SSE:.2f}")
print(f"R^2 Value: {R2:.2f}")
# Proof: R^2 is between 0 and 1
if 0 <= R2 <= 1:
    print(
        "Proof: R^2 is between 0 and 1 because SSR and SST are non-negative, and SSR <= SST."
    )
else:
    print("R^2 is outside the range [0, 1], which indicates an issue with the model.")
