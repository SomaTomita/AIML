import numpy as np
from collections import Counter

# Hypothetical training data points (Age, Estimated Salary) and their labels
# Format: [[Age, Estimated Salary], ...]
X_train = np.array(
    [
        [25, 50000],  # Training Point 1
        [30, 60000],  # Training Point 2
        [35, 70000],  # Training Point 3
        [40, 80000],  # Training Point 4
        [45, 90000],  # Training Point 5
    ]
)

# Labels for the training data
y_train = np.array([0, 0, 1, 1, 1])  # Labels (0: Not Purchased, 1: Purchased)

# New data point to classify
new_point = np.array([34, 72000])  # Age = 34, Estimated Salary = 72,000

# Step 1: Compute Euclidean distance from new_point to all training points
# Euclidean distance formula: sqrt((x1 - x2)^2 + (y1 - y2)^2)
distances = np.sqrt(np.sum((X_train - new_point) ** 2, axis=1))

# Step 2: Find the indices of the k (5) nearest neighbors
k = 5  # Number of neighbors
nearest_indices = np.argsort(distances)[
    :k
]  # Sort distances and get the indices of the nearest points

# Step 3: Retrieve the labels of the nearest neighbors
nearest_labels = y_train[nearest_indices]

# Step 4: Determine the majority class using a vote
# Count the occurrences of each label in the nearest neighbors
label_counts = Counter(nearest_labels)
predicted_class = label_counts.most_common(1)[0][
    0
]  # Most common label is the predicted class

# Displaying results
print("Distances to training points:", distances)
print("Indices of nearest neighbors:", nearest_indices)
print("Labels of nearest neighbors:", nearest_labels)
print("Predicted class for the new data point:", predicted_class)

# Explanation of Outputs:
# 1. Distances: Distance from the new data point to each training data point.
# 2. Nearest Neighbors: Points closest to the new data point, based on distances.
# 3. Nearest Labels: Class labels of these neighbors.
# 4. Predicted Class: Majority label among the nearest neighbors.
