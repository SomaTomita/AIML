# Convolution is the core operation in CNNs that applies a filter (kernel) to an image.
# It extracts important features like edges, textures, and patterns.

# - The kernel slides over the input matrix, computing the sum of element-wise multiplications.
# - This operation captures **features like edges** in the image.
# - The kernel used is a simple **edge detection filter**.
# - The result is a feature map (convolved image), which is smaller than the original.


import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Example 5x5 grayscale image (input)
image = np.array(
    [
        [1, 2, 1, 0, 0],
        [4, 5, 3, 1, 1],
        [2, 3, 1, 0, 0],
        [0, 1, 2, 3, 4],
        [1, 0, 0, 1, 2],
    ]
)

# Example 3x3 filter (kernel)
kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

# Apply 2D convolution (valid mode ensures no padding)
convolved_image = convolve2d(image, kernel, mode="valid")

# Display original and convolved images
fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].imshow(image, cmap="gray")
ax[0].set_title("Original Image")

ax[1].imshow(convolved_image, cmap="gray")
ax[1].set_title("Convolved Image")

plt.show()
