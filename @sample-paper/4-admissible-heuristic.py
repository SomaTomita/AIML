############# Question #############

# Suppose you were applying the Graph Search version of A* Search to a search problem.
# Using an admissible heuristic would guarantee that:

# (1) All nodes expanded by the search algorithm will have the same value of f(n).
# (2) The first solution found is an optimal solution.
# (3) The heuristic is also consistent.
# (4) None of the above.


############# Answer #############
# Answer : (4)None of the above.


# (1)
# f(n)=g(n)+h(n)
# In a general A* problem, different paths have different costs g(n), and your heuristic h(n) can also vary.
# So nodes will usually have different values of f(n).

# ex) You have start node S. Two paths lead to different nodes A and B but at different costs (say, (A)=2 and g(B)=4).
#     If the heuristic for each is the same or even 0, you get f(A)=2 and f(B)=4. They differ.


# (2)
# When might it be true?:
#   If you use Tree Search (no revisiting of states) with an admissible heuristic, then the first goal you find is optimal.
#   Or if you use Graph Search (with a closed set) but your heuristic is consistent, that also guarantees the first goal you pop is optimal.

# Why it’s not guaranteed by “admissible alone” in Graph Search:
#   In Graph Search, you may discard or not revisit certain states after you’ve seen them once. If the heuristic is only admissible (but inconsistent), you can still underestimate some costs in a tricky way that leads you to pick a path to the goal that isn’t actually the cheapest, but you find it first anyway.
#   For that reason, admissibility alone doesn’t promise that the first solution is the best in Graph Search.

# (3)
# - Admissible (Does Not Overestimate)
#   A heuristic h(n) is admissible if it does not exceed the true shortest cost h*(n)
#     →　h(n) ≤  h*(n)
#   If A* uses Tree Search, the optimal solution is guaranteed if it is admissible (but not for Graph Search).
# - Consistent (Satisfies the Triangle Inequality)
#   A heuristic is consistent if, when moving from node `n` to `n'`,
#   the difference in heuristic values does not exceed the actual cost of moving:
#   h(n) ≤ c(n, n') + h(n')

# Example: Admissible but NOT Consistent Heuristic
# ---------------------------------------------------
# Scenario:
# Path 1: S -> A -> G (cost: 2 + 4 = 6)
# Path 2: S -> B -> G (cost: 5 + 1 = 6)
#
# Heuristic values:
# h(G) = 0 (Goal has zero cost)
# h(A) = 5 (Does not overestimate)
# h(B) = 2 (Does not overestimate)
# h(S) = 6 (Does not overestimate)
#
# This heuristic is admissible because none of these values exceed the actual shortest cost.
# However, it is NOT consistent because:
# - The heuristic at `A` (h(A) = 5) violates the consistency condition:
#   h(S) = 6, but moving from S to A has cost c(S, A) = 2.
#   Since 6 > 2 + 5, this violates h(n) ≤ c(n, n') + h(n').
#
# Effect of Using This Heuristic:
# In Graph Search, once a node is expanded (closed), it is assumed that we have found the lowest-cost path to it.
# However, with an inconsistent heuristic, a better path may exist, but we may never reprocess that node, leading to suboptimal solutions.


import heapq


class Graph:
    def __init__(self):
        # Edges: a dict mapping each node to a list of (neighbor, cost) pairs
        self.edges = {
            "S": [("A", 2), ("B", 3)],
            "A": [("C", 2)],
            "B": [("C", 2)],
            "C": [("G", 2)],  # G = Goal
            "G": [],
        }

    def neighbors(self, node):
        return self.edges[node]


# ---------------------------------------------------------------------
# Heuristics


def heuristic_admissible_not_consistent(node):
    """
    This heuristic is Admissible but NOT Consistent.
    Admissible: h(G) = 0, h(C) = 2, h(A) = 4, h(B) = 4, h(S) = 6
    It never exceeds the true cost to the goal, so it's "admissible."
    However, it can violate the triangle inequality => not "consistent."
    """
    H = {"S": 6, "A": 4, "B": 4, "C": 2, "G": 0}
    return H[node]


def heuristic_consistent(node):
    """
    This heuristic is Consistent (and also Admissible):
    h(G) = 0, h(C) = 2, h(A) = 4, h(B) = 5, h(S) = 6
    We ensure h(n) <= cost(n->n') + h(n') for all edges => "consistent."
    """
    H = {"S": 6, "A": 4, "B": 5, "C": 2, "G": 0}
    return H[node]


# ---------------------------------------------------------------------
# 1. A* Tree Search (no closed_set)
def astar_tree_search(start, goal, graph, heuristic):
    """
    A* Tree Search:
    - Does NOT keep a closed set.
    - Will revisit states if encountered via different paths.
    - If the heuristic is Admissible, the first goal found is guaranteed optimal
      (because we never discard any path).
    """
    frontier = []  # Min-heap of (f, g, node, path)
    g_costs = {start: 0}
    start_f = g_costs[start] + heuristic(start)
    heapq.heappush(frontier, (start_f, g_costs[start], start, [start]))

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current == goal:
            # As soon as we pop the goal, it's guaranteed optimal
            # in Tree Search if the heuristic is Admissible.
            return path, g

        # Expand neighbors without marking "visited"
        for nbr, cost in graph.neighbors(current):
            new_g = g + cost
            new_f = new_g + heuristic(nbr)

            # If this path is cheaper than any previously recorded path to `nbr`, update
            if (nbr not in g_costs) or (new_g < g_costs[nbr]):
                g_costs[nbr] = new_g
                new_path = path + [nbr]
                heapq.heappush(frontier, (new_f, new_g, nbr, new_path))

    return None, float("inf")  # No path found


# 2. A* Graph Search (with closed_set) - standard approach
def astar_graph_search(start, goal, graph, heuristic):
    """
    A* Graph Search:
    - Keeps a closed_set (expanded nodes).
    - If the heuristic is Consistent, the first goal found is guaranteed optimal.
    - If the heuristic is only Admissible but NOT Consistent, the first goal found
      might not be optimal, because we prune some states after visiting them once.
    """
    frontier = []  # priority queue of (f, g, node, path)
    g_costs = {start: 0}
    start_f = g_costs[start] + heuristic(start)
    heapq.heappush(frontier, (start_f, g_costs[start], start, [start]))

    closed_set = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current == goal:
            # In Graph Search, if the heuristic is consistent, this is the optimal path.
            return path, g

        closed_set.add(current)

        for nbr, cost in graph.neighbors(current):
            new_g = g + cost
            new_f = new_g + heuristic(nbr)

            # Skip neighbors that are in closed_set (standard Graph Search behavior)
            if nbr in closed_set:
                continue

            # If we've never seen `nbr` or found a cheaper cost, push to frontier
            if (nbr not in g_costs) or (new_g < g_costs[nbr]):
                g_costs[nbr] = new_g
                heapq.heappush(frontier, (new_f, new_g, nbr, path + [nbr]))

    return None, float("inf")  # No path found


# ---------------------------------------------------------------------
if __name__ == "__main__":
    graph = Graph()

    # **1 Tree Search with an Admissible Heuristic
    print(
        "[1] Tree Search A* with an Admissible (not necessarily consistent) heuristic"
    )
    path_ts, cost_ts = astar_tree_search(
        "S", "G", graph, heuristic_admissible_not_consistent
    )
    print("Solution path:", path_ts)
    print("Solution cost:", cost_ts, "\n")

    # **2 Graph Search with a Consistent Heuristic
    print("[2] Graph Search A* with a Consistent Heuristic")
    path_gc, cost_gc = astar_graph_search("S", "G", graph, heuristic_consistent)
    print("Solution path:", path_gc)
    print("Solution cost:", cost_gc, "\n")

    # **3 Graph Search with an Admissible but NOT Consistent Heuristic
    print("[3] Graph Search A* with Admissible but NOT Consistent Heuristic")
    path_gi, cost_gi = astar_graph_search(
        "S", "G", graph, heuristic_admissible_not_consistent
    )
    print("Solution path:", path_gi)
    print("Solution cost:", cost_gi)


# **1  Tree Search + Admissible Heuristic ⇒ First found goal is optimal.
# We do not keep a closed_set. We may revisit nodes many times, but we never miss a cheaper path if it appears.
# In Tree Search, admissibility alone guarantees that the first time we pop the goal from the frontier, it must be the optimal solution.

# **2 Graph Search + Consistent Heuristic ⇒ First found goal is optimal.
# We do keep a closed_set. Once a node is expanded, we do not revisit it.
# In Graph Search, for the first goal found to be optimal, we need the heuristic to be consistent.

# **3 Graph Search + Admissible (but Not Consistent) Heuristic ⇒ First found goal is not guaranteed optimal.
# Again, we keep a closed_set. However, if the heuristic is only admissible and not consistent, the first goal found by A* can fail to be optimal because some shorter paths might never get revisited once we close them early.
