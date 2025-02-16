############# Question #############
# Give the time and space complexity of the Tree Search version of Depth-First Search (DFS),
# in terms of the branching factor b and the maximum depth m of the search tree.

# Write your answer using big-O notation, and if you need to use powers then write them in TeX notation.
# For example, n squared would be written as n^2.
# If the algorithm has worst-case complexity n squared, it would be written as O(n^2).

# Time complexity:
# Space complexity:

############# Answer #############
# Time complexity: O(b^m)
# Space complexity: # O(m)

# ----------------------------------------------------------
#     A
#    / \
#   B   C
#  / \   \
# D   E   F

# - Branching factor (b) = 2 (each node has at most 2 children)
# - Maximum depth (m) = 3 (e.g., A → B → D)

# -------------------------------
# TIME COMPLEXITY ANALYSIS
# -------------------------------
# In Tree Search DFS:
# 1. We start from the root (A).
# 2. We explore each node depth-first.
# 3. Each node is visited once.

# Search Flow:
# A
# B
# D → Backtrack (return)
# E → Backtrack (return)
# C
# F → Backtrack (back)

# The total number of nodes in a complete tree of depth m and branching factor b is:
#
#   1 + b + b^2 + ... + b^m = (b^(m+1) - 1) / (b - 1)

# The dominant term in Big-O notation is O(b^m).

# Example calculation:
# If b = 2 and m = 3:
# O(2^3) = O(8)

# -------------------------------
# SPACE COMPLEXITY ANALYSIS
# -------------------------------
# In Tree Search DFS:
# - DFS keeps track of only the current path in the recursion stack.
# - The deepest recursion depth is at most m.
# - Hence, the space complexity depends only on m.

# This results in a space complexity of O(m).

# Example calculation:
# If m = 3:
# O(3)

# ----------------------------------------------------------
# EXAMPLE 2
# Consider a tree with depth m = 4 and branching factor b = 2:

#         A
#        / \
#       B   C
#      / \   \
#     D   E   F
#    /
#   G

# - Time Complexity: O(2^4) = O(16)
# - Space Complexity: O(4) = O(m)
# ----------------------------------------------------------


# ----------------------------------------------------------
# ----------------------------------------------------------
############# Question 1 #############
# Give the time and space complexity of the Tree Search version of Breadth-First Search (BFS),
# in terms of the branching factor b and the maximum depth m of the search tree.

# Write your answer using big-O notation, and if you need to use powers then write them in TeX notation.
# For example, n squared would be written as n^2.
# If the algorithm has worst-case complexity n squared, it would be written as O(n^2).

# Time complexity:
# Space complexity:

############# Answer 1 #############
# Time complexity: O(b^m)
# Space complexity: O(b^m)

# ----------------------------------------------------------
#                A
#               / \
#              B   C
#             / \   \
#            D   E   F

# In BFS, we explore all nodes at depth 0 (the root), then all nodes at depth 1, then depth 2, etc. until we reach the maximum depth m.

# TIME COMPLEXITY:
#  - We visit all nodes level by level.
#  - The total number of nodes in a complete b-ary tree of depth m is about b^m.
#  - Hence, the time complexity is O(b^m).

# SPACE COMPLEXITY:
#  - The largest queue in BFS can hold all nodes in one level,
#    which can be on the order of b^m in the worst case (the bottom level).
#  - Therefore, space complexity is also O(b^m).

# EXAMPLE CALCULATION:
#  - If b = 2, m = 3, the total number of nodes is up to 2^3 = 8.
#  - So time complexity = O(2^3) = O(8), space complexity = O(8).


# ----------------------------------------------------------
# ----------------------------------------------------------
############# Question 2 #############
# Give the time and space complexity of the Tree Search version of Iterative Deepening Depth-First Search (ID-DFS),
# in terms of the branching factor b and the maximum depth m of the search tree.

# Write your answer in big-O notation, and use TeX notation for powers.
# For example, b^m would be written as b^m.

# Time complexity:
# Space complexity:

############# Answer 2 #############
# Time complexity: O(b^m)
# Space complexity: O(m)

# ----------------------------------------------------------
#                A
#               / \
#              B   C
#             / \   \
#            D   E   F

# In ID-DFS, we repeatedly run DFS with increasing depth limits:
#  1) DFS to depth 0
#  2) DFS to depth 1
#  3) DFS to depth 2
#  ...
#  up to depth m

# TIME COMPLEXITY:
#  - Although we do multiple DFS passes, the repeated searches do not exceed O(b^m) in a tree,
#    because each new depth limit re-traverses fewer nodes from previous iterations in a tree setting.
#  - Hence, the time complexity is O(b^m).

# SPACE COMPLEXITY:
#  - Each DFS still only needs space proportional to the maximum depth m of the tree (for the recursion stack or path).
#  - Thus, the space complexity is O(m).

# EXAMPLE CALCULATION:
#  - If b = 2 and m = 3:
#    Time: O(2^3) = O(8)
#    Space: O(3)


############# Question 3 (a Twisted One) #############
# Imagine a Bidirectional Search on a uniform tree where the branching factor is b,
# and the solution is found at depth m (distance from root to the goal is m).
# Give the time and space complexity in big-O notation, using TeX for powers.

# Note: In Bidirectional Search, one search begins from the root and another from the goal,
# meeting in the middle.

# Time complexity:
# Space complexity:


############# Answer 3 #############
# Time complexity: O(b^(m/2))
# Space complexity: O(b^(m/2))

# ----------------------------------------------------------
# Bidirectional Search splits the search into two fronts:
# 1) Forward search from the start (root).
# 2) Backward search from the goal.
#
# Once the two searches meet, the path is found.
#
# TIME COMPLEXITY:
#  - Each search roughly proceeds to half the total depth m, i.e., m/2.
#  - Hence, each search explores on the order of b^(m/2) nodes.
#  - Since we have two simultaneous searches, the total is O(b^(m/2)).
#
# SPACE COMPLEXITY:
#  - Both searches also store on the order of b^(m/2) nodes.
#  - Therefore, the combined space complexity is also O(b^(m/2)).
#
# EXAMPLE CALCULATION:
#  - If b = 2, m = 4:
#    Time: O(2^(4/2)) = O(2^2) = O(4)
#    Space: O(4)


# ----------------------------------------------------------
# ----------------------------------------------------------
############# Question 4 #############
# Give the time and space complexity of performing a Topological Sort using Kahn's Algorithm,
# in terms of the number of vertices V and the number of edges E in a Directed Acyclic Graph (DAG).
#
# Write your answer in Big-O notation.
#
# Time complexity:
#
# Space complexity:

############# Answer 4 #############
# Time complexity: O(V + E)
# Space complexity: O(V)
#
# ----------------------------------------------------------
# EXPLANATION:
# 1) Initialize an in-degree count for each vertex.
# 2) Collect all vertices with in-degree 0 in a queue.
# 3) While the queue is not empty:
#    - Remove a vertex from the queue.
#    - Decrease the in-degree of its neighbors.
#    - If any neighbor's in-degree reaches 0, add it to the queue.
#
# This process visits every vertex and edge exactly once, so the time complexity is O(V + E).
# Since we store in-degree counts for all vertices and keep a queue of at most V vertices,
# the space complexity is O(V).
#
# -------------------------------
# EXAMPLE DAG
# -------------------------------
#     A
#      \
#       B
#      / \
#     C   D
#
# If there are V = 4 vertices and E = 3 edges, the algorithm runs in O(4 + 3) = O(7).
# The overall complexity scales linearly with the size of the graph, not quadratically.
