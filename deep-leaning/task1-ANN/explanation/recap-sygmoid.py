import numpy as np
import matplotlib.pyplot as plt

# In this example, let's assume we are predicting whether a student passes a test.
# The dependent variable (outcome) is Pass (1) or Fail (0).
# The independent variable (explanatory) is the student's score y.


# Define the sigmoid function, which represents the probability of passing the test
def sigmoid(y):
    return 1 / (1 + np.exp(-y))  # Formula: P(Pass) = 1 / (1 + e^(-y))


# Compute the derivative of the sigmoid function.
# This represents the gradient used in backpropagation.
def sigmoid_derivative(y):
    return sigmoid(y) * (
        1 - sigmoid(y)
    )  # d/dy(sigmoid(y)) = sigmoid(y) * (1 - sigmoid(y))


# Compute the probability of failing the test
def probability_fail(y):
    return 1 - sigmoid(y)  # P(Fail) = 1 - P(Pass)


# Compute the odds ratio, which is the ratio of P(Pass) to P(Fail)
def odds_ratio(y):
    p_pass = sigmoid(y)  # Compute P(Pass)
    p_fail = probability_fail(y)  # Compute P(Fail)
    return p_pass / p_fail  # Odds ratio formula: (P(Pass) / P(Fail)) = e^y


# Compute the log-odds, which is the natural logarithm of the odds ratio
def log_odds(y):
    return np.log(odds_ratio(y))  # Log-odds formula: log(odds ratio) = log(e^y) = y


# Generate values from -10 to 10 to better illustrate the gradient vanishing issue
y_values = np.linspace(-10, 10, 100)

# Compute function values
sigmoid_values = sigmoid(y_values)
odds_values = odds_ratio(y_values)
log_odds_values = log_odds(y_values)

sigmoid_derivative_values = sigmoid_derivative(y_values)


# Print results in a table format with headers
print("Score (y)\tP(Pass)\tP(Fail)\tOdds Ratio\tLog Odds")
for y in np.array([-2, -1, 0, 1, 2]):  # Discrete values for reference
    p_pass = sigmoid(y)  # Compute P(Pass)
    p_fail = probability_fail(y)  # Compute P(Fail)
    odds = odds_ratio(y)  # Compute odds ratio e^y
    log_odds_value = log_odds(y)  # Compute log-odds, which should equal y

    # Display values with four decimal places for clarity
    print(f"{y}\t{p_pass:.4f}\t{p_fail:.4f}\t{odds:.4f}\t{log_odds_value:.4f}")


# Plot the sigmoid function
plt.figure(figsize=(8, 6))
plt.plot(y_values, sigmoid_values, label="Sigmoid Function", color="red")
plt.xlabel("Input (y)")
plt.ylabel("Output (Probability)")
plt.title("Sigmoid Function")
plt.axhline(0.5, color="gray", linestyle="--", alpha=0.7)
plt.axvline(0, color="gray", linestyle="--", alpha=0.7)
plt.legend()
plt.grid()
plt.show()

# Plot the derivative of the sigmoid function to show the vanishing gradient problem
plt.figure(figsize=(8, 6))
plt.plot(y_values, sigmoid_derivative_values, label="Sigmoid Derivative", color="blue")
plt.xlabel("Input (y)")
plt.ylabel("Gradient")
plt.title("Sigmoid Derivative (Vanishing Gradient Issue)")
plt.axhline(0, color="gray", linestyle="--", alpha=0.7)
plt.axvline(0, color="gray", linestyle="--", alpha=0.7)
plt.legend()
plt.grid()
plt.show()


# Explanation:
# The derivative of the sigmoid function is very small when y is too large or too small (close to 0).
# This leads to a problem during backpropagation in deep networks: gradients become extremely small, preventing proper weight updates (this is the "vanishing gradient problem").
