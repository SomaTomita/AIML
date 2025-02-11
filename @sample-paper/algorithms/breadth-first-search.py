############# Question #############
# A FIFO (first-in-first-out) queue is used to store the frontier set of which search algorithm?
# Group of answer choices

# Breadth-First Search
# Graph Search
# Tree Search
# Depth-First Search
# A* Search
# Depth-First Depth-Limited Search
# Iterative Deepening
# Greedy Best-First Search

############# Answer #############
"Breadth-First Search"

# Breadth-First Search (BFS) uses a FIFO queue to store the frontier set.
# BFS explores all nodes at the present depth prior to moving on to the nodes at the next depth level.
# It systematically searches the nodes at the present depth level before moving on to the nodes at the next depth level.
# BFS is a complete search algorithm, meaning it will find a solution if one exists.

# Graph Search / Tree Search: These terms refer to generic search strategies rather than a specific algorithm with a FIFO queue. (any frontier set is allowed)
# Depth-First Search (DFS): Uses a LIFO (Last-In-First-Out) stack instead of a FIFO queue.
# Depth-First Depth-Limited Search: Uses a stack like DFS but with a depth limit.
# Iterative Deepening: Uses DFS (LIFO) at each depth level.
# A* Search: Uses a priority queue (min-heap) based on the evaluation function f(n)=g(n)+h(n).
# Greedy Best-First Search: Uses a priority queue based on the heuristic function h(n)


# ---------------------------------------------------------------------
############# Question 1 #############
# Which search algorithm uses a LIFO (last-in-first-out) stack to store the frontier set?
# Group of answer choices

# Breadth-First Search
# Graph Search
# Tree Search
# Depth-First Search
# A* Search
# Depth-First Depth-Limited Search
# Iterative Deepening
# Greedy Best-First Search

############# Answer #############
"Depth-First Search (DFS)"
"Depth-First Depth-Limited Search"
"Iterative Deepening Search (IDS)"

# - Depth-First Search (DFS) uses a LIFO stack to store the frontier.
#   This means the most recently discovered node is expanded first, allowing DFS to quickly explore deep paths before backtracking.
# - DFS is not guaranteed to be optimal and may not always be complete in infinite search spaces if no depth limit or cycle detection is implemented.

# Other Options Explanation:
# - Breadth-First Search (BFS): Uses a FIFO queue.
# - Graph Search / Tree Search: General search paradigms, not tied to a specific data structure.
# - A* Search: Uses a priority queue with f(n) = g(n) + h(n).
# - Greedy Best-First Search: Uses a priority queue based only on h(n).


# ---------------------------------------------------------------------
############# Question 2 #############
# Which search algorithm uses a priority queue that prioritizes nodes according to the heuristic function h(n) alone?
# Group of answer choices

# Breadth-First Search
# Graph Search
# Tree Search
# Depth-First Search
# A* Search
# Depth-First Depth-Limited Search
# Iterative Deepening
# Greedy Best-First Search

############# Answer #############
"Greedy Best-First Search"

# - Greedy Best-First Search selects the next node to explore based only on the heuristic function h(n), meaning it always chooses the node that appears to be closest to the goal.
# - It does not consider the cost to reach the node (g(n)), which can lead to suboptimal paths.

# Other Options Explanation:
# - Breadth-First Search (BFS): Uses a FIFO queue.
# - Depth-First Search (DFS): Uses a LIFO stack.
# - A* Search: Uses a priority queue with f(n) = g(n) + h(n), which balances cost and heuristic.
# - Graph Search / Tree Search: General search methodologies, not specific data structures.
# - Depth-First Depth-Limited Search: DFS with a maximum depth constraint.
# - Iterative Deepening: Repeated applications of DFS with increasing depth limits.
