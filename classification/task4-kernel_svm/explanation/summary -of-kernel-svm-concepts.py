# Kernel SVM (Support Vector Machine) is a method for classifying data that is difficult
# to linearly separate by mapping it to a higher-dimensional space.

# Import necessary libraries
import numpy as np

# Example data points
x = np.array([30, 50000])  # A data point (Age: 30, Salary: 50,000)
l = np.array([40, 60000])  # Another data point (Age: 40, Salary: 60,000)

# Step 1: Calculate the Euclidean distance between x and l
# Euclidean distance formula: ||x - l|| = sqrt((x1 - l1)^2 + (x2 - l2)^2)
# The Euclidean distance measures how "far" two points are in space.
euclidean_distance = np.sqrt(np.sum((x - l) ** 2))
print(f"Euclidean Distance: {euclidean_distance}")

# Step 2: Compute the squared Euclidean distance (||x - l||^2)
# Squared distance simplifies the computation by removing the square root.
# - If ||x - l||^2 = 100 (close points):
#     exp(-100 / (2 * sigma^2)) results in a similarity close to 1.
# - If ||x - l||^2 = 10,000 (distant points):
#     exp(-10,000 / (2 * sigma^2)) results in a similarity close to 0.
squared_distance = np.sum((x - l) ** 2)
print(f"Squared Euclidean Distance: {squared_distance}")


# Step 3: Define the kernel function using the exponential formula
# The RBF Kernel formula: K(x, l) = exp(-||x - l||^2 / (2 * sigma^2))
# - ||x - l||^2: Measures the distance between data points.
# - Exponential term normalizes this distance into a similarity score in [0, 1].
# - σ (sigma): Determines the scale of influence (how far points can affect each other).
#   - Large σ: Distant points still contribute to the similarity score.
#   - Small σ: Focuses only on nearby points, distant points contribute almost 0.
def rbf_kernel(x, l, sigma):
    squared_distance = np.sum((x - l) ** 2)  # Calculate ||x - l||^2
    return np.exp(-squared_distance / (2 * sigma**2))


# Example: Choosing a sigma value
sigma = 10000  # Kernel parameter that controls sensitivity to distance

# Step 4: Compute the kernel similarity between x and l
# The kernel similarity K(x, l) measures how "similar" x is to l based on distance.
kernel_similarity = rbf_kernel(x, l, sigma)
print(f"Kernel Similarity (K(x, l)): {kernel_similarity}")


# Summary of Kernel SVM concepts
"""
Key Concepts:
1. x and l:
   - x: Represents an input data point (e.g., age, salary).
   - l: Represents another data point, often a support vector in SVM.

2. ||x - l||^2 (Squared Euclidean Distance):
   - Large distance -> Data points are less similar.
   - Small distance -> Data points are more similar.

3. Exponential Term (e^(-||x - l||^2 / (2 * sigma^2))):
   - Converts distance into a similarity score in the range [0, 1].

4. σ (sigma):
   - Determines whether the model focuses on nearby points or considers distant points.

Advantages:
1. Allows linear separability of nonlinear data in higher-dimensional space.
2. With the right kernel, it can model complex patterns effectively.
3. Regularization parameter (C) helps prevent overfitting.

Disadvantages:
1. Computationally expensive, making it less suitable for large datasets.
2. Requires careful tuning of kernel and hyperparameters (e.g., σ for RBF kernel).
"""
