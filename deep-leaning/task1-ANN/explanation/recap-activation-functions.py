import numpy as np
import matplotlib.pyplot as plt


# Step Function: A binary activation function that outputs 1 if x >= 0, otherwise 0.
# Interpretation: This function is used in early neural networks as an activation function.
# It behaves like a thresholding function, turning the output fully on (1) or off (0).
# However, it is not differentiable at x = 0, making it less useful for deep learning.
def step_function(x):
    return np.where(x >= 0, 1, 0)


# ReLU (Rectified Linear Unit) Function: Outputs x if x > 0, otherwise 0.
# Interpretation: ReLU is widely used in deep learning because it helps prevent vanishing gradients.
# Unlike the step function, ReLU is differentiable for all positive values.
# However, it has a problem where negative values always output zero (dying ReLU problem).
def relu_function(x):
    return np.maximum(0, x)


# Hyperbolic Tangent (Tanh) Function: A smooth activation function that outputs values between -1 and 1.
# Interpretation: Tanh is a scaled version of the sigmoid function, providing output centered around zero.
# It is commonly used in neural networks because it allows both positive and negative activations.
# However, it still suffers from vanishing gradient problems for large values of |x|.
def tanh_function(x):
    return np.tanh(x)


# Generate input values
x_values = np.linspace(-5, 5, 100)

# Compute function values
step_values = step_function(x_values)
relu_values = relu_function(x_values)
tanh_values = tanh_function(x_values)


# Plot Step Function
plt.figure(figsize=(8, 6))
plt.step(x_values, step_values, where="mid", label="Step Function", color="blue")
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.title("Step Function")
plt.axvline(0, color="gray", linestyle="--", alpha=0.7)
plt.legend()
plt.grid()
plt.show()

# Plot ReLU Function
plt.figure(figsize=(8, 6))
plt.plot(x_values, relu_values, label="ReLU Function", color="red")
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.title("ReLU Function")
plt.axvline(0, color="gray", linestyle="--", alpha=0.7)
plt.legend()
plt.grid()
plt.show()

# Plot Tanh Function
plt.figure(figsize=(8, 6))
plt.plot(x_values, tanh_values, label="Tanh Function", color="green")
plt.xlabel("Input (x)")
plt.ylabel("Output")
plt.title("Hyperbolic Tangent (Tanh) Function")
plt.axhline(0, color="gray", linestyle="--", alpha=0.7)
plt.legend()
plt.grid()
plt.show()

# Print some representative values
print("x\tStep(x)\tReLU(x)\tTanh(x)")
for x in np.array([-2, -1, 0, 1, 2]):
    step_x = step_function(x)
    relu_x = relu_function(x)
    tanh_x = tanh_function(x)
    print(f"{x}\t{step_x}\t{relu_x}\t{tanh_x:.4f}")
