import numpy as np
import matplotlib.pyplot as plt

# Stochastic Gradient Descent (SGD) Explanation:
# SGD is a variant of gradient descent where updates are performed using a single randomly selected data point at each iteration.
# This makes it computationally efficient and useful for large datasets.
# Unlike standard gradient descent (batch gradient descent), which computes the gradient using the entire dataset,
# SGD introduces more noise, but it often helps escape local minima and speeds up convergence.

# Example: Minimizing a simple quadratic function f(x) = x^2 with stochastic updates
# The derivative (gradient) is f'(x) = 2x, and the minimum is at x = 0


def function(x):
    return x**2  # Quadratic function f(x) = x^2


def gradient(x):
    return 2 * x  # Derivative f'(x) = 2x


# Stochastic Gradient Descent Implementation
learning_rate = 0.1  # Step size
x = 4  # Initial starting point
iterations = 20  # Number of updates
history = [x]  # Store values for visualization

for _ in range(iterations):
    noise = np.random.normal(0, 0.2)  # Adding randomness to simulate SGD
    x -= learning_rate * (gradient(x) + noise)  # Update x based on noisy gradient
    history.append(x)

# Visualization of the stochastic descent process
x_values = np.linspace(-5, 5, 100)
y_values = function(x_values)

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, label="Function f(x) = x^2", color="blue")
plt.scatter(history, [function(h) for h in history], color="red", label="SGD Steps")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Stochastic Gradient Descent (SGD) Minimizing f(x) = x^2")
plt.legend()
plt.grid()
plt.show()

# Print step-by-step values
print("Iteration\t x\t f(x)")
for i, x_val in enumerate(history):
    print(f"{i}\t {x_val:.4f}\t {function(x_val):.4f}")
