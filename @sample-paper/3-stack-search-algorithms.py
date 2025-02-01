############# Question1 #############
# Which search algorithms guarantee finding the optimal solution
#   (shortest path or minimum cost) in an unweighted graph or weighted graph with non-negative edge costs?
# Select two of the following answers:

# Depth-First Search (DFS)
# A* Search
# Greedy Best-First Search
# Breadth-First Search (BFS)
# Tree Search

############# Answer1 #############
# ⚪︎ Breadth-First Search (BFS)
# ⚪︎ A* Search

# Why Not the Others?
# Depth-First Search (DFS): Does not guarantee finding the shortest path as it explores deeply before backtracking.
# Greedy Best-First Search: Focuses only on the heuristic value h(n), which can lead to suboptimal paths.
# Tree Search: A general framework and does not specify how the frontier is managed; thus, it does not guarantee optimality.


############# Question2 #############
# Which search algorithms use a priority queue to determine the next node to expand?
# Select two of the following answers:

# Depth-First Search (DFS)
# A* Search
# Breadth-First Search (BFS)
# Greedy Best-First Search
# Graph Search

############# Answer2 #############
# ⚪︎ A* Search
# ⚪︎ Greedy Best-First Search
# Why Not the Others?
# Depth-First Search (DFS): Uses a LIFO stack to explore the deepest nodes first.
# Breadth-First Search (BFS): Uses a FIFO queue to explore nodes level by level.
# Graph Search: This is a general framework and does not dictate a specific data structure (can use a stack, queue, or priority queue).


############# Question3 #############
# A LIFO (last-in-first-out) stack is used to store the frontier set of which search algorithms?
# Select three of the following answers.

# Depth-First Search
# A* Search
# Greedy Best-First Search
# Graph Search
# Breadth-First Search
# Depth-First Depth-Limited Search
# Tree Search
# Iterative Deepening

############# Answer #############
# ⚪︎ Depth-First Search (DFS)
# ⚪︎ Depth-First Depth-Limited Search
# ⚪︎ Iterative Deepening Search (IDS)
# Why Not the Others?
# A Search*: Uses a priority queue based on the evaluation function f(n) = g(n) + h(n).
# Greedy Best-First Search: Uses a priority queue based on the heuristic value h(n).
# Graph Search: This is a general framework and does not dictate the specific data structure for the frontier
#   (This can use a stack, queue, or priority queue depending on the algorithm).
# Breadth-First Search (BFS): Uses a FIFO (first-in-first-out) queue to explore all nodes at one level before moving to the next.
# Tree Search: This is a general concept for searching trees and does not specify the use of a stack, queue, or other structure.
#   It depends on the specific search strategy.


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}


class Problem:
    def __init__(self, initial_state, goal_state, graph):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.graph = graph

    def is_goal(self, node):
        return node == self.goal_state

    def expand(self, node):
        return self.graph.get(node, [])


problem = Problem("A", "G", graph)


############# depth_limited_search #############
def depth_limited_search(problem, limit):
    def recursive_dls(node, depth):
        if problem.is_goal(node):
            return node
        elif depth == 0:
            return "cutoff"
        else:
            cutoff_occurred = False
            # The recursive call below behaves like pushing onto a stack (LIFO behavior).
            for neighbor in problem.expand(node):
                # Recursive call adds to the call stack (LIFO).
                result = recursive_dls(neighbor, depth - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result != "failure":
                    return result
                # When recursion backtracks, it pops from the call stack (LIFO).
            return "cutoff" if cutoff_occurred else "failure"

    # Recursive depth-limited search starts here
    return recursive_dls(problem.initial_state, limit)


result = depth_limited_search(problem, limit=2)
print("Depth-Limited Search Result:", result)

# Depth-Limited Search (DLS):
# Parameters:  Limit: 2,  Start: A,  Goal: G
# Execution Steps:
# Call 1: recursive_dls(A, depth=2)
#   A is not the goal. Expand neighbors: B and C.
#   Move to neighbor B with depth=1.
# Call 2: recursive_dls(B, depth=1)
#   B is not the goal. Expand neighbors: D and E.
#   Move to neighbor D with depth=0.
# Call 3: recursive_dls(D, depth=0)
#   Depth limit reached. Return "cutoff".
#   Back to Call 2: Explore E (next neighbor of B) with depth=0.
# Call 4: recursive_dls(E, depth=0)
#   Depth limit reached. Return "cutoff".
#   Back to Call 1: Explore C (next neighbor of A) with depth=1.
# Call 5: recursive_dls(C, depth=1)
#   C is not the goal. Expand neighbors: F and G.
#   Move to neighbor F with depth=0.
# Call 6: recursive_dls(F, depth=0)
#   Depth limit reached. Return "cutoff".
#   Back to Call 5: Explore G (next neighbor of C) with depth=0.
# Call 7: recursive_dls(G, depth=0)
#   G is the goal! Return G.


############# iterative_deepening_search #############
def iterative_deepening_search(problem):
    depth = 0
    while True:
        # Each call to depth_limited_search uses recursion, which utilizes a LIFO stack.
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
        # As depth increases, new stack frames are created with deeper levels of recursion.
        depth += 1


result = iterative_deepening_search(problem)
print("Iterative Deepening Search Result:", result)

# Iterative Deepening Search (IDS):
# Parameters: Start: A.  Goal: G
# Execution Steps:
# IDS repeatedly calls DLS with increasing depth limits until the goal is found.

# Iteration 1 (Depth = 0):
#   Call 1: recursive_dls(A, depth=0)
#     Depth limit reached immediately. Return "cutoff".
# Iteration 2 (Depth = 1):
#   Call 1: recursive_dls(A, depth=1)
#     Expand neighbors: B and C.
#   Call 2: recursive_dls(B, depth=0)
#     Depth limit reached. Return "cutoff".
#   Call 3: recursive_dls(C, depth=0)
#     Depth limit reached. Return "cutoff".
# Iteration 3 (Depth = 2):
#   Call 1: recursive_dls(A, depth=2)
#     Expand neighbors: B and C.
#   Call 2: recursive_dls(B, depth=1)
#     Expand neighbors: D and E.
#   Call 3: recursive_dls(D, depth=0)
#     Depth limit reached. Return "cutoff".
#   Call 4: recursive_dls(E, depth=0)
#     Depth limit reached. Return "cutoff".
#   Call 5: recursive_dls(C, depth=1)
#     Expand neighbors: F and G.
#   Call 6: recursive_dls(F, depth=0)
#     Depth limit reached. Return "cutoff".
#   Call 7: recursive_dls(G, depth=0)
#     G is the goal! Return G.


# Key Differences
# [Aspect]        [Depth-Limited Search (DLS)]                                        [Iterative Deepening Search (IDS)]
# Purpose	        Explores nodes up to a fixed depth limit.	                          Repeatedly calls DLS with increasing depth limits.
# Depth Limit	    Requires a pre-defined depth limit.	                                Dynamically adjusts the depth limit, starting from 0.
# Completeness	  Not complete if the goal is deeper than the limit.	                Complete for finite search spaces (eventually finds the goal).
# Optimality	    Not optimal— it stops at the fixed depth and may miss better paths.	Optimal for unweighted graphs (mimics BFS when fully explored).
# Performance	    Single run with a fixed depth.	                                    Runs multiple iterations, each increasing the depth limit.
# Redundant Work  Does not revisit previously expanded depths.                        Revisits the same nodes in shallower levels in each iteration.
# Practical Use	  Useful when the depth of the goal is known.	                        Useful when the depth of the goal is unknown.
