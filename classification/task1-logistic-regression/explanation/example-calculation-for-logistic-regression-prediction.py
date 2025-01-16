# Assumed coefficients and intercept (hypothetical values for explanation):
w1 = 0.3  # Coefficient for Age
w2 = 0.0001  # Coefficient for Estimated Salary
b = -2.5  # Intercept term

# Input values (scaled version will be used internally):
age = 30
estimated_salary = 87000


# Step 1: Feature Scaling
# Let's assume the scaled values for Age and Estimated Salary are:
scaled_age = -0.5  # Hypothetical scaled value for Age
scaled_salary = 1.2  # Hypothetical scaled value for Estimated Salary


# Step 2: Calculate the weighted sum (logit function, z):
z = w1 * scaled_age + w2 * scaled_salary + b
# Substitute values:
z = 0.3 * (-0.5) + 0.0001 * (1.2) - 2.5
# Calculation:
z = -0.15 + 0.00012 - 2.5
z = -2.64988  # Final logit value


# Step 3: Apply the sigmoid function:
# Sigmoid function formula:
# sigmoid(z) = 1 / (1 + exp(-z))
import math

probability = 1 / (1 + math.exp(-z))
# Substitute z:
probability = 1 / (1 + math.exp(2.64988))
# Calculation:
probability = 1 / (1 + 14.1567)
probability = 1 / 15.1567
probability = 0.0659  # Final probability (6.59%)


# Step 4: Thresholding:
# Logistic regression uses a threshold (default is 0.5):
# If probability >= 0.5, predict class 1 (Purchased).
# If probability < 0.5, predict class 0 (Not Purchased).

# In this case:
if probability >= 0.5:
    prediction = 1  # Purchased
else:
    prediction = 0  # Not Purchased


# Final Prediction:
# With a probability of 6.59%, the model predicts class 0 (Not Purchased).

# Summary of calculations:
# z = -2.64988
# probability = 0.0659 (6.59%)
# prediction = 0 (Not Purchased)
