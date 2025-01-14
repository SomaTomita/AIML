import numpy as np
import pandas as pd

x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 6.9, 6.4, 11.3, 11.8])

# Calculate the mean values
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate (x - x̄), (y - ȳ), (x - x̄)(y - ȳ), and (x - x̄)^2
x_diff = x - x_mean
y_diff = y - y_mean
xy_diff = x_diff * y_diff
x_diff_squared = x_diff**2

# Calculate the sums
sum_xy_diff = np.sum(xy_diff)
sum_x_diff_squared = np.sum(x_diff_squared)

# Calculate the slope (w) and intercept (b)
w = sum_xy_diff / sum_x_diff_squared
b = y_mean - w * x_mean

# Display the results
print(f"Slope (a): {w:.2f}")
print(f"Intercept (b): {b:.2f}")

# Regression line equation
print(f"Regression Line Equation: ŷ = {w:.2f}x + {b:.2f}")

# DataFrame for verification
df = pd.DataFrame(
    {
        "x": x,
        "y": y,
        "(x - x̄)": x_diff,
        "(y - ȳ)": y_diff,
        "(x - x̄)(y - ȳ)": xy_diff,
        "(x - x̄)^2": x_diff_squared,
    }
)
print("\nDataFrame:")
print(df)
