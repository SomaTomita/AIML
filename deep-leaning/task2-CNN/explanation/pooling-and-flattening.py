# ------------------------------------------------------------------------------
# Max Pooling Operation
# ------------------------------------------------------------------------------
# Pooling reduces the spatial size of the feature map while retaining key information.

# - A 2x2 window moves across the feature map and selects the **maximum value** in each region.
# - This reduces the feature map size while keeping the most important values.
# - Helps in making the network more robust to small image shifts.

import numpy as np
import matplotlib.pyplot as plt

# Example 4x4 feature map after convolution
feature_map = np.array([[2, 3, 1, 5], [8, 7, 2, 4], [3, 6, 9, 1], [1, 2, 8, 3]])


# Define a function for max pooling (2x2)
def max_pooling_2x2(matrix):
    pooled = np.zeros((matrix.shape[0] // 2, matrix.shape[1] // 2))
    for i in range(0, matrix.shape[0], 2):
        for j in range(0, matrix.shape[1], 2):
            pooled[i // 2, j // 2] = np.max(matrix[i : i + 2, j : j + 2])
    return pooled


# Apply max pooling
pooled_feature_map = max_pooling_2x2(feature_map)

# Display original and pooled feature maps
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].imshow(feature_map, cmap="gray")
ax[0].set_title("Feature Map Before Pooling")

ax[1].imshow(pooled_feature_map, cmap="gray")
ax[1].set_title("Max Pooled Feature Map")

plt.show()


# ------------------------------------------------------------------------------
# Flattening Operation
# ------------------------------------------------------------------------------
# Flattening converts a 2D feature map into a 1D vector.
# This vector is then fed into a fully connected (dense) neural network for classification.

# Example: Flatten a 2x2 matrix
flattened = pooled_feature_map.flatten()

# Print results
print("Flattened Vector:", flattened)
