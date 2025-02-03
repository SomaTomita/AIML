import numpy as np
import matplotlib.pyplot as plt


# Generalized sigmoid function (logistic function with parameters)
def generalized_sigmoid(x, L=1, alpha=1, x0=0):
    return L / (
        1 + np.exp(-alpha * (x - x0))
    )  # Formula: f(x) = L / (1 + e^(-alpha * (x - x0)))


# Example values for x
x_values = np.linspace(-10, 10, 100)

# Parameters for different sigmoid curves
L = 1  # Maximum value
alpha = 1  # Steepness of the curve
x0 = 0  # Midpoint

# Compute sigmoid values
sigmoid_values = generalized_sigmoid(x_values, L, alpha, x0)

# Plot the generalized sigmoid function
plt.figure(figsize=(8, 6))
plt.plot(
    x_values,
    sigmoid_values,
    label=f"Generalized Sigmoid (L={L}, alpha={alpha}, x0={x0})",
    color="green",
)
plt.xlabel("Input (x)")
plt.ylabel("Output f(x)")
plt.title("Generalized Sigmoid Function")
plt.axhline(L / 2, color="gray", linestyle="--", alpha=0.7, label="Midpoint")
plt.axvline(x0, color="gray", linestyle="--", alpha=0.7, label="x0")
plt.legend()
plt.grid()
plt.show()

# Print some representative values
print("x\tf(x)")
for x in np.array([-5, -2, 0, 2, 5]):
    f_x = generalized_sigmoid(x, L, alpha, x0)
    print(f"{x}\t{f_x:.4f}")
