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

# - We have a simple directed graph with three nodes: S -> A -> G
# - Actual costs:
#     S -> A = 1
#     A -> G = 4
#     (Assume direct S -> G exists but costs 6; not used here for the best path.)
# - The best path from S to G is S->A->G with total cost = 5.
# - We define a heuristic h that is admissible (does not exceed the true cost),
#   but it violates the consistency condition.
#   Admissible means: h(node) <= actual_cost_to_goal(node).
#   Consistency means: h(n) <= cost(n, n') + h(n') for all edges (n -> n').
# - We'll show that h(S)=5, h(A)=3, h(G)=0 is admissible but not consistent,
#   because for edge S->A: h(S)=5, cost(S,A)=1, h(A)=3 => 5 <= 1+3=4 is FALSE.

# We'll programmatically check consistency and show it fails,
# while still satisfying admissibility.

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

# - We define a small graph with a start node S, two paths to the goal G:
#       S -> A -> G
#       S -> B -> G
# - Actual costs:
#       S->A = 1, A->G = 10  => total 11
#       S->B = 2, B->G = 1   => total 3 (this is the optimal path)
# - We'll define a heuristic that favors going to A first (making us pick A),
#   even though that leads to a total cost of 11.
#   Greedy Best-First only looks at the heuristic, so it might jump to A first.
# - We'll see that the first solution found is cost=11, not the best possible (3).

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
# Suppose you are running the Graph Search version of A*
# on a pathfinding problem. You have an admissible heuristic
# (it never overestimates the true cost to reach the goal).

# Which of the following statements is guaranteed by using
# an admissible heuristic in the Graph Search version of A*?

# Group of answer choices:
# 1) Consistency of the heuristic.
# 2) Optimality of the first solution found.
# 3) Termination whenever the set of states is finite.
# 4) None of the above.

############# Answer1 #############
"2) Optimality of the first solution found."

# 1) The Key Points:
#    - We have a Graph Search version of A*.
#    - The heuristic is admissible (never overestimates the true cost).
#    - In Graph Search, we maintain a "closed set" to avoid re-expanding
#      the same node endlessly.
#
# 2) Admissible Heuristic:
#    - Admissibility means the heuristic value h(n) for any node n is
#      never greater than the true minimal cost from n to the goal.
#
# 3) A* (Graph Search) Guarantees:
#    - When using a properly implemented Graph Search A* with an admissible
#      (and typically consistent) heuristic, the first time we pop the goal
#      from the priority queue (based on f(n) = g(n) + h(n)), that solution
#      is guaranteed to be optimal.
#    - Specifically, if we do not reopen nodes in the closed set unless
#      a strictly better g-value is found, the algorithm will find the
#      optimal solution upon the first arrival at the goal.
#
# 4) Evaluating the Choices:
#    - (1) Consistency is not automatically guaranteed by mere admissibility,
#      so "1) Consistency of the heuristic" might not hold.
#    - (2) Optimality of the first solution found: This is indeed guaranteed
#      by A* (Graph Search) with an admissible heuristic (and correct management
#      of closed/open sets). So this is true.
#    - (3) Termination on finite states is typically true for Graph Search,
#      but it's not the core property singled out by using an admissible
#      heuristic. The question specifically focuses on the guaranteed outcome
#      of the search's solution quality.
#    - (4) None of the above would be incorrect, because (2) is indeed guaranteed.
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
