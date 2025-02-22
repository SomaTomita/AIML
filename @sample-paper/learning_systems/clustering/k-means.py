############# Question #############

# Given a set of unlabelled examples, the k-means clustering algorithm:
# Group of answer choices

# Finds the best possible cluster centres: minimising the total Euclidean distance from each example to its nearest cluster centre.
# Finds the best possible cluster centres: minimising the total Manhattan distance from each example to its nearest cluster centre.
# Finds a set of cluster centres that may not be the best possible, but cannot be improved by the k-means update step.
# Finds a set of cluster centres that are located where the examples are most dense.
# Finds the best possible cluster centres: dividing the set of examples into clusters of equal size (or as close to equal as possible).

############# Answer #############
"Finds a set of cluster centres that may not be the best possible, but cannot be improved by the k-means update step."

# k-means: Sum the distance between each data (x) and the center of the cluster to which it belongs (μ), and create clusters so that the value is minimized.
# - The k-means algorithm follows an iterative improvement process where it moves towards a local minimum, but it does not guarantee finding the global optimal clustering
"May not be the best possible"  # → Because k-means can get stuck in local minima depending on initialization.
"Cannot be improved by the k-means update step"  # → Because once centroids stabilize, k-means stops even if a better solution exists.

# ❌ Finds the best possible cluster centres: minimising the total Euclidean distance from each example to its nearest cluster centre.
# - The update step only minimizes the sum of squared distances from points to centroids.
# - It never reassigns all points from scratch or tries entirely new centroid placements.
#   It often converges to a local minimum, meaning that there might be a better clustering solution that k-means does not find.
#   The outcome depends heavily on the initial placement of cluster centers.

# ❌  Finds the best possible cluster centres: minimising the total Manhattan distance from each example to its nearest cluster centre.
# - The k-means algorithm is specifically designed to use Euclidean distance (L2 norm), which measures the straight-line distance between points.
# - If you want clustering that minimizes Manhattan distance (L1 norm), you would use k-medoids or k-medians clustering, not k-means.

# ❌ Finds a set of cluster centres that are located where the examples are most dense.
# - K-means minimizes variance (sum of squared Euclidean distances), but it does not explicitly aim to find high-density regions.

# ❌ Finds the best possible cluster centres: dividing the set of examples into clusters of equal size (or as close to equal as possible).
# K-means does not enforce equal cluster sizes; some clusters may have many more points than others.


# ------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# K-means Algorithm Steps:
# 1. Initialization: Randomly choose k points as initial cluster centers (centroids).
# 2. Assignment: Assign each data point to the nearest centroid.
# 3. Update: Compute new centroids as the mean of the assigned points.
# 4. Convergence: Repeat steps 2 and 3 until cluster assignments no longer change.


def initialize_centroids(X, k):
    """
    Step 1: Randomly initialize k centroids.
    - X: Dataset (numpy array of shape (num_samples, num_features))
    - k: Number of clusters
    """
    np.random.seed(42)  # For reproducibility
    indices = np.random.choice(X.shape[0], k, replace=False)  # Pick k random indices
    return X[indices]  # Return the selected data points as initial centroids


def assign_clusters(X, centroids):
    """
    Step 2: Assign each data point to the nearest centroid.
    - Compute the Euclidean distance between each point and each centroid.
    - Assign the point to the cluster with the closest centroid.
    """
    distances = np.linalg.norm(
        X[:, np.newaxis] - centroids, axis=2
    )  # Compute distances
    return np.argmin(distances, axis=1)  # Assign each point to the nearest centroid


def update_centroids(X, labels, k):
    """
    Step 3: Update centroids as the mean of all points in each cluster.
    - Compute the mean of all data points assigned to each cluster.
    """
    return np.array([X[labels == i].mean(axis=0) for i in range(k)])


def kmeans(X, k, max_iters=100, tol=1e-4):
    """
    Full K-means algorithm:
    - Step 1: Initialize centroids randomly.
    - Step 2: Assign points to clusters.
    - Step 3: Compute new centroids.
    - Step 4: Repeat until convergence or max_iters is reached.
    """
    centroids = initialize_centroids(X, k)  # Step 1: Initialize centroids
    for _ in range(max_iters):
        labels = assign_clusters(X, centroids)  # Step 2: Assign clusters
        new_centroids = update_centroids(X, labels, k)  # Step 3: Update centroids

        # Step 4: Check for convergence: If centroids do not change significantly, stop.
        if np.linalg.norm(new_centroids - centroids) < tol:
            break
        centroids = new_centroids  # Update centroids

    return labels, centroids  # Return final cluster assignments and centroids


# Generate sample data (2D points for visualization)
np.random.seed(42)
X1 = np.random.randn(50, 2) + np.array([2, 2])  # Cluster 1
X2 = np.random.randn(50, 2) + np.array([-2, -2])  # Cluster 2
X3 = np.random.randn(50, 2) + np.array([2, -2])  # Cluster 3
X = np.vstack((X1, X2, X3))  # Combine clusters

# Run K-means with k=3
k = 3
labels, centroids = kmeans(X, k)

# Visualization of results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", alpha=0.6, edgecolors="k")
plt.scatter(
    centroids[:, 0], centroids[:, 1], c="red", marker="X", s=200, label="Centroids"
)
plt.legend()
plt.title("K-means Clustering Results")
plt.show()
# ------------------------------------------------------------------------------


# K-means Algorithm Steps:
# 1. Initialization: Randomly choose k points as initial cluster centers (centroids).
# 2. Assignment: Assign each data point to the nearest centroid.
# 3. Update: Compute new centroids as the mean of the assigned points.
# 4. Convergence: Repeat steps 2 and 3 until cluster assignments no longer change.

# Why does K-means work well?
# - K-means gradually moves cluster centers to better positions.
# - It does this by repeating two steps: assignment and update.
#
# Example:
# Imagine we have three groups of people standing in different spots.
# 1. We pick three random leaders (centroids) to represent each group.
# 2. Each person walks toward the closest leader.
# 3. Each leader moves to the average position of their group.
# 4. Repeat steps 2 and 3 until leaders stop moving.
# - This process naturally groups people into sensible clusters!
#
# - The goal of K-means is to minimize the total distance between points and their cluster centers.
# - This is called the "cost function," and K-means automatically lowers it over time.

# Limitations of K-means:
# 1. K-means does not always find the best solution (local minimum problem).
#    - Because centroids are chosen randomly, K-means may settle for a "good enough" solution rather than the best one.
#    - Example: If we start with bad initial centroids, we might get stuck in a suboptimal grouping.
#    - Solution: Use "K-means++" to pick better starting centroids.

# 2. K-means assumes clusters are round and evenly sized.
#    - If clusters have irregular shapes or different sizes, K-means may not work well.
#    - Example: If we try K-means on a dataset with moon-shaped clusters, it will fail to separate them correctly.

# 3. K-means is sensitive to outliers.
#    - Since it calculates centroids based on the mean, an outlier (a point far away) can shift the centroid too much.
#    - Solution: Consider using K-medoids, which are less sensitive to outliers.
