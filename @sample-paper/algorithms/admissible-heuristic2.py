############# Question #############
# Suppose you are applying the Tree Search version of Greedy Best-First Search to a search problem. Using an admissible heuristic would guarantee:
# Group of answer choices

# Consistency of the heuristic.
# Optimality of the first solution found.
# Termination whenever the set of states is finite.
# None of the above.

############# Answer #############
"4)  None of the above."


##################################
# Scenario 1: An admissible but NOT consistent heuristic
##################################
#        S
#       / \
#      1   6
#     /     \
#    A ----- G
#       4

# - S → A costs 1
# - A → G costs 4
# - S → G directly costs 6 (not the best path)
# - The best path from S to G is S → A → G with a total cost of 5.

# - We define a heuristic h that is admissible (does not exceed the true cost),
#   but it violates the consistency condition.

#   Admissible means: h(node) <= actual_cost_to_goal(node).
# A heuristic is admissible if it never overestimates the true cost to the goal.
# - h(S) = 5, actual cost to G = 5  (OK)
# - h(A) = 3, actual cost to G = 4  (OK)
# - h(G) = 0, actual cost to G = 0  (OK)
# → heuristic is admissible.

#   Consistency means: h(n) <= cost(n, n') + h(n') for all edges (n -> n').
# 1. For S → A (cost = 1):
#    - h(S) = 5
#    - h(A) = 3
#    - Rule: h(S) ≤ c(S, A) + h(A)
#      → 5 ≤ 1 + 3
#      → 5 ≤ 4  (Wrong! Not consistent)

# 2. For A → G (cost = 4):
#    - h(A) = 3
#    - h(G) = 0
#    - Rule: h(A) ≤ c(A, G) + h(G)
#      → 3 ≤ 4 + 0
#      → 3 ≤ 4  (OK)
# Since S → A fails the consistency check, the heuristic is NOT consistent.


graph_scenario1 = {"S": {"A": 1, "G": 6}, "A": {"G": 4}, "G": {}}  # S->A=1, S->G=6

heuristic_scenario1 = {
    "S": 5,  # Actual best cost to G = 5
    "A": 3,  # Actual best cost to G = 4
    "G": 0,  # Goal node
}


def is_admissible(node, graph, heuristic):
    # We'll do a quick check by comparing heuristic to the actual minimal cost.
    # For this small example, we already know minimal costs by inspection.
    if node == "S":
        return heuristic[node] <= 5  # minimal cost S->A->G
    elif node == "A":
        return heuristic[node] <= 4
    elif node == "G":
        return heuristic[node] == 0
    return True


def check_admissibility(graph, heuristic):
    for node in graph.keys():
        if not is_admissible(node, graph, heuristic):
            return False
    return True


def check_consistency(graph, heuristic):
    for node, edges in graph.items():
        for child, cost in edges.items():
            # Consistency check: h(node) <= cost(node, child) + h(child)
            if heuristic[node] > cost + heuristic[child]:
                return False
    return True


def scenario1_check():
    print("Scenario 1: Check if heuristic is admissible but not consistent.")
    print("Heuristic:", heuristic_scenario1)

    is_adm = check_admissibility(graph_scenario1, heuristic_scenario1)
    is_con = check_consistency(graph_scenario1, heuristic_scenario1)

    print("Admissible?", is_adm)
    print("Consistent?", is_con)
    print("Result: It's admissible but NOT consistent.\n")


scenario1_check()


##################################
# Scenario 2: The first solution found by Greedy Best-First Search is NOT optimal
##################################
#        S
#       / \
#      1   2
#     /     \
#    A       B
#     \     /
#      10  1
#        G

# - The start node is S, and the goal is G.
# - There are two possible paths:
#    - Path 1: S → A → G (Cost: 1 + 10 = 11)
#    - Path 2: S → B → G (Cost: 2 + 1 = 3)    → This is the optimal path
#
# - We define a heuristic h(n) that is admissible (never overestimates)
#   but misguides GBFS by making A seem more attractive than B.
# - h(A) = 1, h(B) = 5, h(G) = 0
# - Since GBFS prioritizes the lowest h(n), it will pick A first.
# - However, this leads to a total cost of 11, while the best path costs only 3.
# → GBFS does NOT guarantee that the first solution found is optimal.

graph_scenario2 = {"S": {"A": 1, "B": 2}, "A": {"G": 10}, "B": {"G": 1}, "G": {}}

# Heuristic that misleadingly suggests A is better (lower h-value):
#  - h(A)=1, h(B)=5, h(S)=some value, h(G)=0
# This will push Greedy BFS to explore A first.
heuristic_scenario2 = {"S": 3, "A": 1, "B": 5, "G": 0}

import heapq


def greedy_best_first_search(graph, heuristic, start, goal):
    # Frontier is a priority queue that sorts by h(node)
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))
    visited = set()  # for demonstration; we won't allow re-expansion in this example

    came_from = {start: None}  # to reconstruct the path
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            # Return path and cost
            return reconstruct_path(came_from, start, goal), path_cost(
                graph, came_from, start, goal
            )

        visited.add(current)
        # Expand neighbors
        for nxt in graph[current]:
            if nxt not in visited:
                came_from[nxt] = current
                heapq.heappush(frontier, (heuristic[nxt], nxt))
    return None, None


def reconstruct_path(came_from, start, goal):
    # Build path from goal back to start
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from.get(node)
    path.reverse()
    return path


def path_cost(graph, came_from, start, goal):
    # Calculate actual cost by traversing the path
    path = reconstruct_path(came_from, start, goal)
    total = 0
    for i in range(len(path) - 1):
        cur_node = path[i]
        nxt_node = path[i + 1]
        total += graph[cur_node][nxt_node]
    return total


def scenario2_demo():
    print(
        "Scenario 2: Greedy Best-First Search might find a suboptimal first solution."
    )
    path, cost_ = greedy_best_first_search(
        graph_scenario2, heuristic_scenario2, "S", "G"
    )
    print("First solution found by Greedy BFS:", path)
    print("Cost of this solution:", cost_)
    print("But there's a cheaper path: S->B->G with cost=3.\n")


scenario2_demo()


##################################
# Scenario 3: A search can fail to terminate in a finite state space (without visited checks)
##################################
#        S <-> A
#          (cycle)
#         (no path to G)

# - Even if the number of states is finite, we can revisit states infinitely
#   if we do not track which states have been visited.
# - We'll build a small cycle: S <-> A, plus a goal G that's not prioritized by the heuristic.
# - The naive search without visited checks could keep cycling between S and A forever.
# - In this code, we'll illustrate what happens if we remove any "visited" set.

graph_scenario3 = {
    "S": {"A": 1},  # S -> A
    "A": {"S": 1},  # A -> S (cycle)
    "G": {},  # G is disconnected in this simple example
}

heuristic_scenario3 = {"S": 5, "A": 5, "G": 0}


def greedy_best_first_search_no_visited(
    graph, heuristic, start, goal, max_iterations=10
):
    # This version has no 'visited' set and can get stuck in cycles.
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))
    came_from = {start: None}

    iteration_count = 0
    while frontier:
        iteration_count += 1
        if iteration_count > max_iterations:
            # We'll break forcibly to avoid infinite loop in this demo
            print("WARNING: No termination within max_iterations (artificial break).")
            return None, None

        _, current = heapq.heappop(frontier)
        if current == goal:
            return reconstruct_path(came_from, start, goal), path_cost(
                graph, came_from, start, goal
            )

        # Expand neighbors without any visited check
        for nxt in graph[current]:
            came_from[nxt] = current
            heapq.heappush(frontier, (heuristic[nxt], nxt))

    return None, None


def scenario3_infinite_loop_demo():
    print("Scenario 3: Demonstrating potential infinite loop without visited checks.")
    print("Graph has a cycle: S <-> A. G is never reached.")
    path, cost_ = greedy_best_first_search_no_visited(
        graph_scenario3, heuristic_scenario3, "S", "G", max_iterations=10
    )
    if path is None:
        print("No solution found. Likely stuck in a cycle (stopped artificially).")
    else:
        print("Solution found (unexpected in this setup):", path)
    print()


scenario3_infinite_loop_demo()


# ----------------------------------------------------------
# ----------------------------------------------------------
############# Question1 #############
# Suppose you are applying the *Tree Search* version of A* Search to a search problem.
# The heuristic you are using is *admissible*, meaning it never overestimates
# the true cost to reach the goal.
#
# Which of the following statements is guaranteed by using an admissible
# heuristic in *Tree Search A*?
#
# Group of answer choices:
# (1) All nodes expanded by the search algorithm will have the same value of f(n).
# (2) The first solution found is guaranteed to be the optimal solution.
# (3) The heuristic is also consistent.
# (4) None of the above.

############# Answer #############
"(2) The first solution found is guaranteed"

# < Difference between Tree Search and Graph Search >
# Tree Search:
#   - A state that has been visited once may be visited again on a “different path” (without a closed set). (It does not have a closed set.)
#   - Even a route that is not the shortest path can be re-searched, so a better solution may be found later.
#   - If there is an admissibility heuristic, the first solution found will be the optimal solution.
# Graph Search:
#   - Adds the visited node to the closed set so that the same node is not expanded twice.
#   - However, it is possible that a closed node is actually revisited with a better route. (In this case, the optimal solution may not be obtained.)
#   - Non-consistent heuristics may not yield an optimal solution.


# < Explanation >
# 1) Admissible Heuristic in Tree Search A*:
#    - In Tree Search, we do NOT maintain a "closed set" that would prevent
#      re-expanding a node. Instead, every time we discover a path to a node,
#      we add that path to the frontier.
#    - Because we never discard potential paths, we will always explore
#      the path that truly leads to the cheapest cost, provided our
#      heuristic never overestimates (i.e., is admissible).
#
# 2) Evaluating the Choices:
#    (1) "All nodes expanded have the same f(n)":
#        - The function f(n) = g(n) + h(n) will differ as soon as you have
#          different path costs g(n). Since there are typically multiple
#          ways to reach the same node at different costs, f(n) values
#          can vary. This is not guaranteed.
#
#    (2) "The first solution found is guaranteed to be optimal":
#        - In Tree Search A*, an admissible heuristic ensures that the first
#          time you pop the goal from the priority queue, it will be the
#          lowest-cost path. Because you do not discard alternative paths
#          prematurely, you won't miss any better route. Thus, this
#          statement is *true* under these conditions.
#
#    (3) "The heuristic is also consistent":
#        - Admissibility alone does not imply consistency. Consistency
#          (monotonicity) is a stronger condition. Hence, you cannot
#          conclude the heuristic is consistent just from it being admissible.


##################################
# < Example 1 >
#    S
#   / \
#  A   B
#  |   |
#  G   G
##################################
import heapq

# Graph definition (Tree structure)
graph = {"S": [("A", 1), ("B", 4)], "A": [("G", 5)], "B": [("G", 1)], "G": []}

# Admissible heuristic
heuristic = {"S": 4, "A": 5, "B": 1, "G": 0}


def astar_tree_search(start, goal):
    """Tree Search version of A* algorithm"""
    frontier = []  # Priority queue
    heapq.heappush(
        frontier, (heuristic[start], 0, start, [start])
    )  # (f, g, node, path)

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current == goal:
            return path, g  # The first route to reach the goal is the optimal solution

        # Expand children (Tree Search, no visited management)
        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")  # No solution found


solution_path, solution_cost = astar_tree_search("S", "G")
print("The first solution found:", solution_path)
print("Optimal cost:", solution_cost)


##################################
# < Example 2 >
#       S
#      / \
#     A   B
#    /     \
#   C       D
#  /
# G
##################################
import heapq

# New graph (G is only at the end of A->C)
graph = {
    "S": [("A", 1), ("B", 3)],
    "A": [("C", 4)],
    "B": [("D", 2)],  # B side has no G
    "C": [("G", 2)],  # G is after C
    "D": [],  # D has no goal
    "G": [],
}

# Admissible heuristic
heuristic = {"S": 5, "A": 4, "B": 2, "C": 2, "D": 1, "G": 0}


def astar_tree_search(start, goal):
    """Tree Search version of A* algorithm"""
    frontier = []
    heapq.heappush(
        frontier, (heuristic[start], 0, start, [start])
    )  # (f, g, node, path)

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current == goal:
            return path, g  # The first goal found is the optimal solution

        for neighbor, cost in graph[current]:
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")  # No solution found (if goal is not found)


solution_path, solution_cost = astar_tree_search("S", "G")
print("The first solution found:", solution_path)
print("Optimal cost:", solution_cost)

# Tree Search A* correctly recognized that “there is no goal on the B side” and searched the route on the A side to find the optimal solution.
# Graph Search A* adds a node once visited to the closed set and does not expand it again.
# Thus, if it first goes B → D, the search will fail and may end before trying the correct route A → C → G.
# ----------------------------------------------------------


# ----------------------------------------------------------
# ----------------------------------------------------------
############# Question2 #############
# Suppose you are running the Tree Search version of Greedy Best-First Search
# (GBFS) on a planning problem. The heuristic is admissible (never overestimates)
# but might not be consistent. Also, there is no mechanism to avoid revisiting
# states (no "visited" check).

# Which of the following statements is guaranteed by using
# this admissible heuristic in the Tree Search version of GBFS?

# Group of answer choices:
# 1) Consistency of the heuristic.
# 2) Optimality of the first solution found.
# 3) Termination whenever the set of states is finite.
# 4) None of the above.

############# Answer2 #############
"4) None of the above."

# 1) Situation:
#    - We use Tree Search with Greedy Best-First Search (GBFS).
#    - The heuristic is admissible but may not be consistent.
#    - No mechanism to avoid revisiting states (no visited set).
#
# 2) Analyzing Each Choice:
#    - (1) Consistency of the heuristic:
#      Admissibility alone does not imply consistency.
#      Consistency requires h(n) <= cost(n, n') + h(n') for all edges (n -> n').
#      Hence, we cannot claim consistency just because it's admissible.
#
#    - (2) Optimality of the first solution found:
#      Greedy Best-First Search prioritizes nodes with the smallest heuristic value h(n).
#      However, it ignores the actual cost so far, g(n). As a result, it might lead
#      to a path that seems promising by the heuristic but is not truly optimal.
#      Therefore, the first solution it finds is not guaranteed to be optimal.
#
#    - (3) Termination whenever the set of states is finite:
#      Because we're using Tree Search and have no visited check, the same states
#      can be re-generated infinitely (through different paths), potentially
#      causing an infinite loop, even in a finite state space. Hence, we cannot
#      guarantee termination.
# ----------------------------------------------------------
##################################
#       S
#      / \
#     A   B
#    /     \
#   C       D
#  /         \
# G           G
##################################
# Route 1 (optimal route): S → A → C → G (cost 1 + 1 + 1 = 3)
# Route 2 (route chosen by GBFS): S → B → D → G (cost 1 + 10 + 1 = 12)

# < Flow of search >
# Expand S → A (h=4), B (h=3) are candidates
# Select B because h(B) < h(A)
# Expand B → D (h=1)
# Expand D → G (Goal!)
# Goal is reached! However, the cost is 12, which is not the optimal route.
