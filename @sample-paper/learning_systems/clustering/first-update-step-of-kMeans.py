############# Question #############
# Suppose you are given the following set of five unlabelled examples,
# each with two attributes x and y:

#     x   |   y
#   ----------------
#     3   |   1
#     4   |   3
#     4   |   4
#     5   |   3
#     5   |   4

# Execute the first update step of the k-means clustering algorithm with k=2.
# The initial cluster centres (named A and B) are given in the table below:

#   Cluster Centre |  x  |  y
#  ------------------------
#         A        |  2  |  1
#         B        |  3  |  3

# Enter the updated x and y positions of cluster centres A and B.


############# Answer #############
"Cluster A"
"x: 3.0"
"y: 1.0"

"Cluster B"
"x: 4.5"
"y: 3.5"


# ------------------------------------------------------------------------------
import numpy as np

# Given dataset with two attributes x and y
data = np.array([[3, 1], [4, 3], [4, 4], [5, 3], [5, 4]])

# Initial cluster centers A (2,1) and B (3,3)
cluster_A = np.array([2, 1])
cluster_B = np.array([3, 3])


# Step 1: Compute Euclidean distances to each cluster center
# Euclidean distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# Compute distance from each point to Cluster A (2,1)
distances_A = np.linalg.norm(data - cluster_A, axis=1)
# Calculations:
# d((3,1), (2,1)) = sqrt((3-2)^2 + (1-1)^2) = sqrt(1 + 0) = 1.0
# d((4,3), (2,1)) = sqrt((4-2)^2 + (3-1)^2) = sqrt(4 + 4) = 2.83
# d((4,4), (2,1)) = sqrt((4-2)^2 + (4-1)^2) = sqrt(4 + 9) = 3.61
# d((5,3), (2,1)) = sqrt((5-2)^2 + (3-1)^2) = sqrt(9 + 4) = 3.61
# d((5,4), (2,1)) = sqrt((5-2)^2 + (4-1)^2) = sqrt(9 + 9) = 4.24

# Compute distance from each point to Cluster B (3,3)
distances_B = np.linalg.norm(data - cluster_B, axis=1)
# Calculations:
# d((3,1), (3,3)) = sqrt((3-3)^2 + (1-3)^2) = sqrt(0 + 4) = 2.0
# d((4,3), (3,3)) = sqrt((4-3)^2 + (3-3)^2) = sqrt(1 + 0) = 1.0
# d((4,4), (3,3)) = sqrt((4-3)^2 + (4-3)^2) = sqrt(1 + 1) = 1.41
# d((5,3), (3,3)) = sqrt((5-3)^2 + (3-3)^2) = sqrt(4 + 0) = 2.0
# d((5,4), (3,3)) = sqrt((5-3)^2 + (4-3)^2) = sqrt(4 + 1) = 2.24


# Step 2: Assign each point to the closest cluster
# If distance to A is smaller, assign to A; otherwise, assign to B
assignments = np.where(distances_A < distances_B, "A", "B")


# Step 3: Separate points into clusters based on assignments
# Assignments based on calculated distances:
# (3,1) -> Closest to A (1.0 vs 2.0) -> Assign to A
# (4,3) -> Closest to B (2.83 vs 1.0) -> Assign to B
# (4,4) -> Closest to B (3.61 vs 1.41) -> Assign to B
# (5,3) -> Closest to B (3.61 vs 2.0) -> Assign to B
# (5,4) -> Closest to B (4.24 vs 2.24) -> Assign to B

# Cluster A contains only: (3,1)
# Cluster B contains: (4,3), (4,4), (5,3), (5,4)
cluster_A_points = data[assignments == "A"]
cluster_B_points = data[assignments == "B"]


# Step 4: Compute new cluster centers by averaging x and y coordinates of assigned points
if len(cluster_A_points) > 0:
    new_cluster_A = cluster_A_points.mean(axis=0)
else:
    new_cluster_A = cluster_A  # If no points assigned, keep the old center

if len(cluster_B_points) > 0:
    new_cluster_B = cluster_B_points.mean(axis=0)
else:
    new_cluster_B = cluster_B  # If no points assigned, keep the old center

# New Cluster A center:
# x_A = sum(x values in A) / count = (3) / 1 = 3.0
# y_A = sum(y values in A) / count = (1) / 1 = 1.0

# New Cluster B center:
# x_B = sum(x values in B) / count = (4 + 4 + 5 + 5) / 4 = 18 / 4 = 4.5
# y_B = sum(y values in B) / count = (3 + 4 + 3 + 4) / 4 = 14 / 4 = 3.5


# Output the updated cluster centers
print("Updated Cluster A Center:", new_cluster_A)
print("Updated Cluster B Center:", new_cluster_B)

# Expected result:
# Cluster A -> (3.0, 1.0) (only contains (3,1))
# Cluster B -> (4.5, 3.5) (average of (4,3), (4,4), (5,3), (5,4))

# ------------------------------------------------------------------------------
