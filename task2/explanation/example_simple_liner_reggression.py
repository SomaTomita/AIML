############# Manual Linear Regression Calculation #############
import numpy as np

# sample data (age, salary)
X = np.array([1, 2, 3])  # Input data
y = np.array([30000, 40000, 50000])  # Output data

# calculate the slope (w)
mean_x = np.mean(X)
mean_y = np.mean(y)
# @calculation_for_slope_simple.png
# Calculate the “impact of outputs based on input variability” by dividing the numerator (co-variation of inputs and outputs) by the denominator (input variance)
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x) ** 2)
w = numerator / denominator

# calculate the intercept (b)
b = mean_y - w * mean_x

# predict() the salary for a new value of X
x_new = 4
y_pred = w * x_new + b
print(f"Predicted salary for {x_new} years of experience (manual): {y_pred}")


############# Using sklearn for Linear Regression #############
from sklearn.linear_model import LinearRegression

X = X.reshape(-1, 1)  # Now X is a 2D array

model = LinearRegression()
model.fit(X, y)
predicted_salary = model.predict([[4]])
print(f"Predicted salary for 4 years of experience: {predicted_salary[0]}")
