import numpy as np
import matplotlib.pyplot as plt

# Gradient Descent Explanation:
# Gradient Descent is an optimization algorithm used to minimize functions by iteratively moving in the direction of the negative gradient.
# It is widely used in machine learning to minimize loss functions during training.
# The core idea is that by computing the derivative (gradient) of the function, we determine the direction to update parameters (e.g., weights in neural networks).

# The update rule is:
# theta_new = theta_old - learning_rate * gradient
# where:
# - theta represents the parameter we are optimizing
# - learning_rate controls the step size
# - gradient is the derivative of the function at the current point

# Example: Minimizing a simple quadratic function f(x) = x^2
# The derivative (gradient) is f'(x) = 2x, and the minimum is at x = 0


def function(x):
    return x**2  # Quadratic function f(x) = x^2


def gradient(x):
    return 2 * x  # Derivative f'(x) = 2x


# Gradient Descent Implementation
learning_rate = 0.1  # Step size
x = 4  # Starting point
iterations = 20  # Number of iterations
history = [x]  # Store values for visualization

for _ in range(iterations):
    x -= learning_rate * gradient(x)  # Update x based on the gradient
    history.append(x)

# Visualization of the descent process
x_values = np.linspace(-5, 5, 100)
y_values = function(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Function f(x) = x^2", color="blue")
plt.scatter(
    history, [function(h) for h in history], color="red", label="Gradient Descent Steps"
)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gradient Descent Minimizing f(x) = x^2")
plt.legend()
plt.grid()
plt.show()

# Print step-by-step values
print("Iteration\t x\t f(x)")
for i, x_val in enumerate(history):
    print(f"{i}\t {x_val:.4f}\t {function(x_val):.4f}")
