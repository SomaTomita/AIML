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


############# Question 1 #############

# Suppose you are given the following set of five unlabelled examples,
# each with two attributes x and y:

#     x   |   y
#   ----------------
#     2   |   2
#     3   |   1
#     4   |   2
#     6   |   3
#     7   |   2

# Execute the first update step of the k-means clustering algorithm with k=2.
# The initial cluster centres (named A and B) are given in the table below:

#   Cluster Centre |  x  |  y
#  ------------------------
#         A        | 2   | 1
#         B        | 6   | 2

# Enter the updated x and y positions of cluster centres A and B.


############# Answer 1 #############
"Cluster A"
"x: 2.5"
"y: 1.5"

"Cluster B"
"x: 5.67"
"y: 2.33"

# ------------------------------------------------------------------------------
import numpy as np

# Given dataset with two attributes x and y
data = np.array([[2, 2], [3, 1], [4, 2], [6, 3], [7, 2]])

# Initial cluster centers A (2,1) and B (6,2)
cluster_A = np.array([2, 1])
cluster_B = np.array([6, 2])

# Step 1: Compute Euclidean distances to each cluster center
# Euclidean distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# Compute distance from each point to Cluster A (2,1)
distances_A = np.linalg.norm(data - cluster_A, axis=1)

# Calculations:
# d((2,2), (2,1)) = sqrt((2-2)^2 + (2-1)^2) = sqrt(0 + 1) = 1.0
# d((3,1), (2,1)) = sqrt((3-2)^2 + (1-1)^2) = sqrt(1 + 0) = 1.0
# d((4,2), (2,1)) = sqrt((4-2)^2 + (2-1)^2) = sqrt(4 + 1) = sqrt(5) ≈ 2.24
# d((6,3), (2,1)) = sqrt((6-2)^2 + (3-1)^2) = sqrt(16 + 4) = sqrt(20) ≈ 4.47
# d((7,2), (2,1)) = sqrt((7-2)^2 + (2-1)^2) = sqrt(25 + 1) = sqrt(26) ≈ 5.10

# Compute distance from each point to Cluster B (6,2)
distances_B = np.linalg.norm(data - cluster_B, axis=1)

# Calculations:
# d((2,2), (6,2)) = sqrt((2-6)^2 + (2-2)^2) = sqrt(16 + 0) = 4.0
# d((3,1), (6,2)) = sqrt((3-6)^2 + (1-2)^2) = sqrt(9 + 1) = sqrt(10) ≈ 3.16
# d((4,2), (6,2)) = sqrt((4-6)^2 + (2-2)^2) = sqrt(4 + 0) = 2.0
# d((6,3), (6,2)) = sqrt((6-6)^2 + (3-2)^2) = sqrt(0 + 1) = 1.0
# d((7,2), (6,2)) = sqrt((7-6)^2 + (2-2)^2) = sqrt(1 + 0) = 1.0

# Step 2: Assign each point to the closest cluster
# If distance to A is smaller, assign to A; otherwise, assign to B
assignments = np.where(distances_A < distances_B, "A", "B")

# Assignments based on calculated distances:
# (2,2) -> Closest to A (1.0 vs 4.0) -> Assign to A
# (3,1) -> Closest to A (1.0 vs 3.16) -> Assign to A
# (4,2) -> Closest to B (2.24 vs 2.0) -> Assign to B
# (6,3) -> Closest to B (4.47 vs 1.0) -> Assign to B
# (7,2) -> Closest to B (5.10 vs 1.0) -> Assign to B

# Cluster A contains: (2,2), (3,1)
# Cluster B contains: (4,2), (6,3), (7,2)
cluster_A_points = data[assignments == "A"]
cluster_B_points = data[assignments == "B"]

# Step 3: Compute new cluster centers by averaging x and y coordinates of assigned points
if len(cluster_A_points) > 0:
    new_cluster_A = cluster_A_points.mean(axis=0)
else:
    new_cluster_A = cluster_A  # If no points assigned, keep the old center

if len(cluster_B_points) > 0:
    new_cluster_B = cluster_B_points.mean(axis=0)
else:
    new_cluster_B = cluster_B  # If no points assigned, keep the old center

# New Cluster A center:
# x_A = sum(x values in A) / count = (2 + 3) / 2 = 2.5
# y_A = sum(y values in A) / count = (2 + 1) / 2 = 1.5

# New Cluster B center:
# x_B = sum(x values in B) / count = (4 + 6 + 7) / 3 = 17 / 3 ≈ 5.67
# y_B = sum(y values in B) / count = (2 + 3 + 2) / 3 = 7 / 3 ≈ 2.33

# Output the updated cluster centers
print("Updated Cluster A Center:", new_cluster_A)
print("Updated Cluster B Center:", new_cluster_B)

# Expected result:
# Cluster A -> (2.5, 1.5) (average of (2,2) and (3,1))
# Cluster B -> (5.67, 2.33) (average of (4,2), (6,3), (7,2))
# ------------------------------------------------------------------------------

############# Question 2 #############
# Suppose you are given the following set of five unlabelled examples,
# each with two attributes x and y:

#     x   |   y
#   ----------------
#     0   |   0
#     1   |   1
#     2   |   2
#     3   |   3
#     4   |   4

# Execute the first update step of the k-means clustering algorithm with k=2.
# The initial cluster centres (named A and B) are given in the table below:

#   Cluster Centre |  x    |  y
#  ----------------------------
#         A        |  2    |  2
#         B        | 100   | 100

# Enter the updated x and y positions of cluster centres A and B.

############# Answer 2 #############
"Cluster A"
"x: 2.0"
"y: 2.0"

"Cluster B"
"x: 100.00"
"y: 100.00"

# ------------------------------------------------------------------------------
import numpy as np

# Given dataset with two attributes x and y
data = np.array([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]])

# Initial cluster centers A (2,2) and B (100,100)
cluster_A = np.array([2, 2])
cluster_B = np.array([100, 100])

# Step 1: Compute Euclidean distances to each cluster center
# Euclidean distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# Compute distance from each point to Cluster A (2,2)
distances_A = np.linalg.norm(data - cluster_A, axis=1)

# Calculations:
# d((0,0), (2,2)) = sqrt((0-2)^2 + (0-2)^2) = sqrt(4 + 4) = sqrt(8) ≈ 2.83
# d((1,1), (2,2)) = sqrt((1-2)^2 + (1-2)^2) = sqrt(1 + 1) = sqrt(2) ≈ 1.41
# d((2,2), (2,2)) = sqrt((2-2)^2 + (2-2)^2) = 0
# d((3,3), (2,2)) = sqrt((3-2)^2 + (3-2)^2) = sqrt(1 + 1) = sqrt(2) ≈ 1.41
# d((4,4), (2,2)) = sqrt((4-2)^2 + (4-2)^2) = sqrt(4 + 4) = sqrt(8) ≈ 2.83

# Compute distance from each point to Cluster B (100,100)
distances_B = np.linalg.norm(data - cluster_B, axis=1)

# Calculations:
# d((0,0), (100,100)) = sqrt((0-100)^2 + (0-100)^2) = sqrt(10000 + 10000) = sqrt(20000) ≈ 141.42
# d((1,1), (100,100)) = sqrt((1-100)^2 + (1-100)^2) = sqrt(9801 + 9801) ≈ 140.01
# d((2,2), (100,100)) = sqrt((2-100)^2 + (2-100)^2) = sqrt(9604 + 9604) ≈ 138.59
# d((3,3), (100,100)) = sqrt((3-100)^2 + (3-100)^2) = sqrt(9409 + 9409) ≈ 137.18
# d((4,4), (100,100)) = sqrt((4-100)^2 + (4-100)^2) = sqrt(9216 + 9216) ≈ 135.76

# Step 2: Assign each point to the closest cluster
# If distance to A is smaller, assign to A; otherwise, assign to B
assignments = np.where(distances_A < distances_B, "A", "B")

# Assignments based on calculated distances:
# (0,0) -> Closest to A (2.83 vs 141.42) -> Assign to A
# (1,1) -> Closest to A (1.41 vs 140.01) -> Assign to A
# (2,2) -> Closest to A (0 vs 138.59) -> Assign to A
# (3,3) -> Closest to A (1.41 vs 137.18) -> Assign to A
# (4,4) -> Closest to A (2.83 vs 135.76) -> Assign to A

# Cluster A contains all points: (0,0), (1,1), (2,2), (3,3), (4,4)
# Cluster B contains no points.
cluster_A_points = data[assignments == "A"]
cluster_B_points = data[assignments == "B"]

# Step 3: Compute new cluster centers by averaging x and y coordinates of assigned points
if len(cluster_A_points) > 0:
    new_cluster_A = cluster_A_points.mean(axis=0)
else:
    new_cluster_A = cluster_A  # If no points assigned, keep the old center

if len(cluster_B_points) > 0:
    new_cluster_B = cluster_B_points.mean(axis=0)
else:
    new_cluster_B = cluster_B  # If no points assigned, keep the old center

# New Cluster A center:
# x_A = sum(x values in A) / count = (0 + 1 + 2 + 3 + 4) / 5 = 10 / 5 = 2.0
# y_A = sum(y values in A) / count = (0 + 1 + 2 + 3 + 4) / 5 = 10 / 5 = 2.0

# New Cluster B center remains the same:
# Since no points were assigned to B, its center does not change.

# Output the updated cluster centers
print("Updated Cluster A Center:", new_cluster_A)
print("Updated Cluster B Center:", new_cluster_B)

# Expected result:
# Cluster A -> (2.0, 2.0) (all points were assigned to A, so its mean is the same)
# Cluster B -> (100.0, 100.0) (no points assigned, so it remains unchanged)
# ------------------------------------------------------------------------------
