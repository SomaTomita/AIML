############# Question1 #############
# Consider the following description of a search algorithm:
# function XXXXXX-Search(problem) returns a solution, or failure
#     initialize the frontier using the initial state of problem
#     initialize a priority queue based on a heuristic function h(n)
#     loop do
#         if the frontier is empty then return failure
#         choose a node from the frontier with the lowest value of h(n)
#         if the node contains a goal state then return the corresponding solution
#         expand the chosen node, adding the resulting nodes to the frontier, only if not already in the frontier

# Which search algorithm does this describe?

# Depth-First Search
# A* Search
# Greedy Best-First Search
# Graph Search
# Breadth-First Search

############# Answer1 #############
# Algorithm: Greedy Best-First Search
# Why?
# The algorithm uses a priority queue to order nodes in the frontier based on the heuristic function h(n).
# It does not consider the actual path cost g(n) from the start node, focusing only on the heuristic value.
# This behavior matches the definition of Greedy Best-First Search, which prioritizes exploring nodes that "appear" closest to the goal according to the heuristic.


############# Question2 #############
# Consider the following description of a search algorithm:
# function XXXXXX-Search(problem) returns a solution, or failure
#     initialize the frontier using the initial state of problem
#     initialize a priority queue
#     initialize the explored set to be empty
#     set the cost of the initial state to 0
#     loop do
#         if the frontier is empty then return failure
#         choose a node from the frontier with the lowest value of f(n)
#         if the node contains a goal state then return the corresponding solution
#         add the node to the explored set
#         for each neighbor of the chosen node:
#             calculate new_cost
#             if the neighbor is not in the frontier or explored set, or if new_cost is lower than its previously recorded cost:
#                 update the neighbor’s cost and add (or update) it in the frontier with priority f(neighbor) = new_cost + h(neighbor)
#
# Which search algorithm does this describe?
#
# Depth-First Search
# A* Search
# Greedy Best-First Search
# Graph Search
# Breadth-First Search

############# Answer2 #############
# Algorithm: A* Search
# Why?:
# The algorithm maintains a priority queue and updates nodes based on a priority value that combines past cost and an estimated future cost.
# This behavior matches A* Search, which balances exploration and cost efficiency to find an optimal path.


############# Question3 #############
# Consider the following description of a general search algorithm.

# function XXXXXX-Search(problem) returns a solution, or failure
#     initialize the frontier using the initial state of problem
#     initialize the explored set to be empty
#     loop do
#         if the frontier is empty then return failure
#         choose a leaf node and remove it from the frontier
#         if the node contains a goal state then return the corresponding solution
#         add the node to the explored set
#         expand the chosen node, adding the resulting nodes to the frontier, only if not in the frontier or explored set

# Identify this algorithm.

# Depth-First Search
# A* Search
# Greedy Best-First Search
# Graph Search
# Breadth-First Search
# Depth-First Depth-Limited Search
# Tree Search
# Iterative Deepening


############# Answer3 #############
# Algorithm: Graph Search
# Why?: It avoids revisiting nodes (explored set), ensures no duplicate nodes in the frontier,
#         and systematically expands nodes without prioritizing cost or heuristic values.
#       Even though the behavior of the code is similar to BFS, the algorithm itself does not specify “how to manage the frontier”, so this falls under the generic algorithm called "Graph Search


############# Question4 #############
# Consider the following description of a search algorithm:
# function XXXXXX-Search(problem) returns a solution, or failure
#     for increasing values of a parameter:
#         perform a modified version of another search algorithm
#         if a solution is found then return it
#     return failure
#
# Which search algorithm does this describe?
#
# Depth-First Search
# Iterative Deepening Search
# Greedy Best-First Search
# Graph Search
# Breadth-First Search


############# Answer4 #############
# Algorithm: Iterative Deepening Search
# Why?:
# The algorithm repeatedly executes another search method with a growing constraint, ensuring completeness
# while managing resource usage effectively.


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# **** Problem Class Implementation ****
class Problem:
    def __init__(self, initial_state, goal_state, graph, heuristics=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = graph
        self.heuristics = heuristics

    def is_goal(self, node):
        return node == self.goal_state  # Check if the node is the goal

    def expand(self, node):
        return self.graph.get(node, [])  # Return neighbors of the node


############# Graph Search #############
from collections import deque


def graph_search(problem):
    frontier = deque(
        [problem.initial_state]
    )  # Used as a double-ended queue (can also be a list, stack, or priority queue)
    explored = set()

    while frontier:
        node = (
            frontier.popleft()
        )  # Select the next node to explore from the frontier (FIFO (First In, First Out) for BFS behavior)
        # If this is changed to pop(), it behaves as LIFO (Last In, First Out) for DFS behavior.
        if problem.is_goal(node):  # Check if the node is a goal state
            return node
        explored.add(node)  # Add the node to the explored set
        for neighbor in problem.expand(node):
            if neighbor not in frontier and neighbor not in explored:
                frontier.append(
                    neighbor
                )  # Add to frontier only if not already explored
                # The way nodes are added can vary depending on the structure used for the frontier (e.g., priority queue for A*).
    return "Failure"


# ****Test Code****
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}
problem = Problem(initial_state="A", goal_state="E", graph=graph)
result = graph_search(problem)
print("Result:", result)

# Step-by-Step Execution:
# First Iteration:
#     node = 'A' (popped from frontier)
#   Check if 'A' is the goal → No.
#   Add 'A' to explored: explored = {'A'}.
#   Expand 'A' → Neighbors: ['B', 'C'].
#   Add 'B' and 'C' to frontier: frontier = deque(['B', 'C']).
# Second Iteration:
#     node = 'B' (popped from frontier)
#   Check if 'B' is the goal → No.
#   Add 'B' to explored: explored = {'A', 'B'}.
#   Expand 'B' → Neighbors: ['D', 'E'].
#   Add 'D' and 'E' to frontier: frontier = deque(['C', 'D', 'E']).
# Third Iteration:
#     node = 'C' (popped from frontier)
#   Check if 'C' is the goal → No.
#   Add 'C' to explored: explored = {'A', 'B', 'C'}.
#   Expand 'C' → Neighbors: ['F'].
#   Add 'F' to frontier: frontier = deque(['D', 'E', 'F']).
# Fourth Iteration:
#     node = 'D' (popped from frontier)
#   Check if 'D' is the goal → No.
#   Add 'D' to explored: explored = {'A', 'B', 'C', 'D'}.
#   Expand 'D' → No neighbors.
#   frontier = deque(['E', 'F']).
# Fifth Iteration:
#     node = 'E' (popped from frontier)
#   Check if 'E' is the goal → Yes.
#   Return 'E'.


############# Depth-First Search (DFS) #############
def depth_first_search(problem):
    frontier = [problem.initial_state]  # Use a stack for DFS
    explored = set()

    while frontier:
        node = frontier.pop()  # LIFO(Last In First Out) for DFS behavior
        if problem.is_goal(node):
            return node
        explored.add(node)
        for neighbor in reversed(problem.expand(node)):  # Reversed for DFS order
            if neighbor not in frontier and neighbor not in explored:
                frontier.append(neighbor)
    return "Failure"


# ****Test Code****
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}
problem = Problem(initial_state="A", goal_state="E", graph=graph)
result = depth_first_search(problem)
print("Result:", result)

# Step-by-Step Execution:
# First Iteration:
#   Pop A from the frontier:
#     node = 'A', frontier = [].
#   Check if A is the goal → No.
#   Add A to explored:
#     explored = {'A'}.
#   Expand A: Neighbors = ['B', 'C'] (reversed to ['C', 'B'] for DFS order).
#   Add C and B to the frontier:
#     frontier = ['C', 'B'].
# Second Iteration:
#   Pop B from the frontier:
#     node = 'B', frontier = ['C'].
#   Check if B is the goal → No.
#   Add B to explored:
#     explored = {'A', 'B'}.
#   Expand B: Neighbors = ['D', 'E'] (reversed to ['E', 'D'] for DFS order).
#   Add E and D to the frontier:
#     frontier = ['C', 'E', 'D'].
# Third Iteration:
#   Pop D from the frontier:
#     node = 'D', frontier = ['C', 'E'].
#   Check if D is the goal → No.
#   Add D to explored:
#     explored = {'A', 'B', 'D'}.
#   Expand D: Neighbors = [] (no neighbors to add).
#   Frontier remains:
#     frontier = ['C', 'E'].
# Fourth Iteration:
#   Pop E from the frontier:
#     node = 'E', frontier = ['C'].
#   Check if E is the goal → Yes.
#   Return 'E'.

# Tree @DFS: DFS: Depth-First Search.gif


############# Breadth-First Search (BFS) #############
# From shallow level to deep level
def breadth_first_search(problem):
    frontier = deque([problem.initial_state])  # Use a queue for BFS
    explored = set()

    while frontier:
        node = frontier.popleft()  # FIFO (First In, First Out) for BFS behavior
        if problem.is_goal(node):
            return node
        explored.add(node)
        for neighbor in problem.expand(node):
            if neighbor not in frontier and neighbor not in explored:
                frontier.append(neighbor)
    return "Failure"


# ****Test Code****
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": [], "F": []}
problem = Problem(initial_state="A", goal_state="E", graph=graph)
result = breadth_first_search(problem)
print("Result:", result)

# Step-by-Step Execution:
# First Iteration:
#   Pop A from the frontier:
#   node = 'A', frontier = deque([]).
#   Check if A is the goal → No.
#   Add A to explored:
#   explored = {'A'}.
#   Expand A: Neighbors = ['B', 'C'].
#   Add B and C to the frontier:
#   frontier = deque(['B', 'C']).
# Second Iteration:
#   Pop B from the frontier:
#   node = 'B', frontier = deque(['C']).
#   Check if B is the goal → No.
#   Add B to explored:
#   explored = {'A', 'B'}.
#   Expand B: Neighbors = ['D', 'E'].
#   Add D and E to the frontier:
#   frontier = deque(['C', 'D', 'E']).
# Third Iteration:
#   Pop C from the frontier:
#   node = 'C', frontier = deque(['D', 'E']).
#   Check if C is the goal → No.
#   Add C to explored:
#   explored = {'A', 'B', 'C'}.
#   Expand C: Neighbors = ['F'].
#   Add F to the frontier:
#   frontier = deque(['D', 'E', 'F']).
# Fourth Iteration:
#   Pop D from the frontier:
#   node = 'D', frontier = deque(['E', 'F']).
#   Check if D is the goal → No.
#   Add D to explored:
#   explored = {'A', 'B', 'C', 'D'}.
#   Expand D: Neighbors = [] (no neighbors to add).
#   Frontier remains:
#   frontier = deque(['E', 'F']).
# Fifth Iteration:
#   Pop E from the frontier:
#   node = 'E', frontier = deque(['F']).
#   Check if E is the goal → Yes.
#   Return 'E'.

# Tree @BFS: Breadth-First Search.gif


############# A* Search #############
import heapq


def a_star_search(problem):
    frontier = [(0, problem.initial_state)]  # (f(n), node)
    costs = {problem.initial_state: 0}  # g(n) = 0 for the start node

    while frontier:
        _, currentNode = heapq.heappop(frontier)  # priority queue
        if problem.is_goal(currentNode):
            return currentNode

        for neighbor, cost in problem.expand(currentNode):
            new_cost = costs[currentNode] + cost  # g(n) = g(currentNode) + step cost
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                priority = new_cost + problem.heuristics[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(frontier, (priority, neighbor))
    return "Failure"


# ****Test Code****
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 1), ("E", 5)],
    "C": [("F", 2)],
    "D": [("G", 2)],
    "E": [("G", 1)],
    "F": [("G", 3)],
    "G": [],
}
heuristics = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 2,
    "E": 1,
    "F": 3,
    "G": 0,
}
problem = Problem("A", "G", graph, heuristics)
result = a_star_search(problem)
print("Result:", result)

# Step-by-Step Execution:
# Initialization:
#   Frontier (priority queue): [(0, 'A')]
#   Start with node A with f(A) = g(A) + h(A) = 0 + 7 = 7.
#   Costs (g-values): {'A': 0}
#   The cost to reach the start node A is 0.
# Iteration 1:
#   Pop node from frontier: current = 'A', f(A) = 7.
#   Expand 'A':
#   Neighbors: B (cost = 1) and C (cost = 4).
#   Compute costs:
#   g(B) = g(A) + cost(A → B) = 0 + 1 = 1
#   f(B) = g(B) + h(B) = 1 + 6 = 7
#   g(C) = g(A) + cost(A → C) = 0 + 4 = 4
#   f(C) = g(C) + h(C) = 4 + 4 = 8
#   - frontier: [(7, 'B'), (8, 'C')]
#   - costs: {'A': 0, 'B': 1, 'C': 4}
# Iteration 2:
#   Pop node from frontier: current = 'B', f(B) = 7.
#   Expand 'B':
#   Neighbors: D (cost = 1) and E (cost = 5).
#   Compute costs:
#   g(D) = g(B) + cost(B → D) = 1 + 1 = 2
#   f(D) = g(D) + h(D) = 2 + 2 = 4
#   g(E) = g(B) + cost(B → E) = 1 + 5 = 6
#   f(E) = g(E) + h(E) = 6 + 1 = 7
#   - frontier: [(4, 'D'), (8, 'C'), (7, 'E')]
#   - costs: {'A': 0, 'B': 1, 'C': 4, 'D': 2, 'E': 6}
# Iteration 3:
#   Pop node from frontier: current = 'D', f(D) = 4.
#   Expand 'D':
#   Neighbor: G (cost = 2).
#   Compute costs:
#   g(G) = g(D) + cost(D → G) = 2 + 2 = 4
#   f(G) = g(G) + h(G) = 4 + 0 = 4
#   - frontier: [(4, 'G'), (8, 'C'), (7, 'E')]
#   - costs: {'A': 0, 'B': 1, 'C': 4, 'D': 2, 'E': 6, 'G': 4}
# Iteration 4:
#   Pop node from frontier: current = 'G', f(G) = 4.
#   Goal check: G is the goal node. Return G.


############# Greedy Best-First Search #############
import heapq


def greedy_best_first_search(problem):
    frontier = []
    heapq.heappush(
        frontier, (problem.heuristics[problem.initial_state], problem.initial_state)
    )  # h(n) for initial state
    explored = set()

    while frontier:
        _, node = heapq.heappop(frontier)
        if problem.is_goal(node):
            return node
        explored.add(node)
        for neighbor, _ in problem.expand(
            node
        ):  # Expand returns (neighbor, cost), but cost is ignored
            if neighbor not in frontier and neighbor not in explored:
                heuristic = problem.heuristics[neighbor]  # Use heuristic value h(n)
                heapq.heappush(frontier, (heuristic, neighbor))
    return "Failure"


# ****Test Code****
graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 1), ("E", 5)],
    "C": [("F", 2)],
    "D": [("G", 2)],
    "E": [("G", 1)],
    "F": [("G", 3)],
    "G": [],
}
heuristics = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 2,
    "E": 1,
    "F": 3,
    "G": 0,
}
problem = Problem("A", "G", graph, heuristics)
result = greedy_best_first_search(problem)
print("Result:", result)

# Step-by-Step Execution
#   Initialization:
#   Frontier: [(7, 'A')] (heuristic h(A) = 7)
#   Explored set: set()
# Iteration 1:
#   Pop node 'A' from the frontier:
#   Frontier: []
#   Current node: 'A' (h(A) = 7)
#   Goal check: False
#   Expand 'A':
#   Neighbors: B (h(B) = 6) and C (h(C) = 4)
#   frontier: [(6, 'B'), (4, 'C')]
#   explored set: {'A'}
# Iteration 2:
#   Pop node 'C' from the frontier (lowest heuristic):
#   Frontier: [(6, 'B')]
#   Current node: 'C' (h(C) = 4)
#   Goal check: False
#   Expand 'C':
#   Neighbor: F (h(F) = 3)
#   frontier: [(3, 'F'), (6, 'B')]
#   explored set: {'A', 'C'}
# Iteration 3:
#   Pop node 'F' from the frontier:
#   Frontier: [(6, 'B')]
#   Current node: 'F' (h(F) = 3)
#   Goal check: False
#   Expand 'F':
#   Neighbor: G (h(G) = 0)
#   frontier: [(0, 'G'), (6, 'B')]
#   explored set: {'A', 'C', 'F'}
# Iteration 4:
#   Pop node 'G' from the frontier:
#   Frontier: [(6, 'B')]
#   Current node: 'G' (h(G) = 0)
#   Goal check: True
#   Return 'G'
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# | Algorithm                  | Frontier Data Structure    | Heuristic Usage         | Cost Usage | Explored Set               | Features / Search Order
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# | Graph Search               | Queue (deque)              | None                    | None       | Yes                        | A general graph search using an explored set to avoid revisiting nodes.
# | Depth-First Search (DFS)   | Stack (list)               | None                    | None       | Yes                        | LIFO order; dives deep first, which can be efficient but may miss shallower solutions.
# | Breadth-First Search (BFS) | Queue (deque)              | None                    | None       | Yes                        | FIFO order; explores level by level. Guarantees the shortest path (in terms of edges), but may use high memory.
# | A* Search                  | Priority Queue (heapq)     | Yes (f(n)=g(n)+h(n))    | Yes        | Implicit via cost tracking | Combines actual path cost (g(n)) and heuristic (h(n)) to efficiently find an optimal solution, if the heuristic is admissible.
# | Greedy Best-First Search   | Priority Queue (heapq)     | Yes (only h(n))         | None       | Yes                        | Chooses nodes based solely on the heuristic value. It is fast but does not guarantee the optimal solution.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# - Graph Search: Uses an explored set to prevent revisiting nodes.
#   This is a generic method for exploring graphs.
#
# - Depth-First Search (DFS): Uses a "stack" to explore as deep as possible before backtracking.
#   Pros: Lower memory usage; may quickly find deep solutions. (DFS only stores nodes along the current path, plus at most one adjacent node per level.)
#   Cons: Risk of infinite loops; does not guarantee the shortest path. (e.g., in an infinite graph, it can overflow the stack.)
#
# - Breadth-First Search (BFS): Uses a "queue" to explore nodes level by level.
#   Pros: Guarantees the shortest path (in terms of the number of edges).
#   Cons: Can require significant memory. (It stores all nodes at the current depth level, so the number of stored nodes grows exponentially with depth.)
#
# - A* Search: Uses a "priority queue" combining actual cost (g(n)) and heuristic (h(n)) into f(n) = g(n) + h(n).
#   Pros: Finds optimal solutions efficiently if the heuristic is well-designed.
#   Cons: Requires a good heuristic; improper heuristic design can degrade performance.
#
# - Greedy Best-First Search: Uses a "priority queue" ordered solely by the heuristic value h(n).
#   Pros: Often fast in reaching a goal.
#   Cons: Does not guarantee the optimal solution; may be misled by local minima.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
############# DFS Memory Transition (Stack-Based, LIFO) #############
# Step 1 (Start at Root):
#    A
#    |
#    v
#    B

# Stack: [A, B]

# Step 2 (Go deeper):
#    A
#    |
#    v
#    B
#    |
#    v
#    D

# Stack: [A, B, D]  # Only the current path is stored

# Step 3 (Backtrack and explore new branch):
#    A
#    |
#    v
#    B
#    |
#    v
#    E

# Stack: [A, B, E]  # D is removed, E is added

# Step 4 (Go deeper again):
#    A
#    |
#    v
#    B
#    |
#    v
#    E
#    |
#    v
#    G

# Stack: [A, B, E, G]  # Only this deep path is in memory

# Final Memory Usage: **O(d) (depth of tree)**.


############# BFS Memory Transition (Queue-Based, FIFO) #############
# Step 1 (Start at Root):
#    A

# Queue: [A]  # Stores root

# Step 2 (Expand Level 1):
#      A
#     / \
#    B   C

# Queue: [B, C]  # Stores all children of A

# Step 3 (Expand Level 2):
#      A
#     / \
#    B   C
#   / \   \
#  D   E   F

# Queue: [D, E, F]  # Stores all children of B and C

# Step 4 (Expand Level 3):
#      A
#     / \
#    B   C
#   / \   \
#  D   E   F
#         / \
#        G   H

# Queue: [G, H]  # Stores all children of F

# Final Memory Usage: **O(b^d) (branching factor ^ depth)**.
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
