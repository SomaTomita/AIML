############# Question #############
# The Port of Southampton is upgrading its infrastructure with the latest autonomous crane.
# The crane can be positioned over land or over a ship.
# Also, the crane can be hoding the container or not holding thle container.
# The set of states is shown in the table below, and the value of the heuristic function is given for each state.

# State Table:
# State, Crane Position, Holding Container?, Container Position, Heuristic Value h(n)
# A,         Land,            	No,	                 Land, 	            0
# B,         Land,            	No,	                 Ship, 	            20
# C,         Land,            	Yes,                 Land, 	            3
# D,         Ship,            	No,	                 Land, 	            5
# E,         Ship,            	No,	                 Ship, 	            16
# F,         Ship,            	Yes,	               Ship, 	            9

# The task is to offload a container from a ship while minimising the amount of energy that is used.

# The actions are:
#   - Pick up the container, with a cost of 10.
#   - Put down the container, with a cost of 3.
#   - Move the crane from land to ship or from ship to land.
#      → Moving the crane while not holding anything has a cost of 3.
#      → Moving the crane while holding the container has a cost of 7.

#   The task is to move the container from the ship onto land.
#   The starting state is B, and the goal state is A.

# Apply the Tree Search version of A* Search to solve this problem.
# One step of the algorithm consists of selecting a node from the frontier, potentially expanding it and adding any relevant child nodes to the frontier.

# The initial frontier set will contain only B.
# Execute A* Search for 3 steps.
# For each step, specify which node is chosen to be expanded, and give the new frontier set as a sequence of states in alphabetical order.
#   For example, C is expanded and the new frontier set is AEF.


############# Answer #############
# Step 1
#   Node selected: B
#   New frontier set in alphabetical order: E
# Step 2
#   Node selected: E
#   New frontier set in alphabetical order: B, F
# Step 3
#   Node selected: F
#   New frontier set in alphabetical order: B, C, E


import heapq


# Conditions for Valid Actions in CraneProblem
#   Pick up container (F):
#     The crane must be at the same position as the container (Ship in this case).
#     The crane must not already be holding a container.

#   Put down container (C, F):
#     The crane must be holding a container before performing this action.
#     The container can only be placed in a valid location (e.g., Land or Ship, depending on the state).

#   Move crane (B ↔ E, F ↔ C):
#     Moving without holding a container has a lower cost (3).
#     Moving while holding a container has a higher cost (7).
#     The move is only valid if it stays within the defined states of the problem.


#   Reversibility of Actions:
#     Moving between Land and Ship can be undone (e.g., B ↔ E).
#     Picking up a container can be undone by putting it down in the same location (e.g., F ↔ E).
#     However, once the container reaches Land (C → A), it cannot be moved back to the Ship.
class CraneProblem:
    def __init__(self):
        self.edges = {
            "B": [("E", 3)],  # Move Land -> Ship (cost=3)
            "E": [
                ("B", 3),  # Move Ship -> Land (cost=3) -> Return to B
                ("F", 10),  # Pick up container (cost=10)
            ],
            "F": [
                ("C", 7),  # Move Ship -> Land while holding container (cost=7)
                ("E", 3),  # Put down container (cost=3) -> Return to E
            ],
            "C": [
                ("A", 3),  # Put down container (cost=3)
                ("F", 10),  # Pick up container again (cost=10) -> Return to F if needed
            ],
        }

    def neighbors(self, node):
        return self.edges.get(node, [])


def heuristic(node):
    H = {
        "A": 0,
        "B": 20,
        "C": 3,
        "D": 5,
        "E": 16,
        "F": 9,
    }
    return H[node]


def astar_tree_search(start, goal, problem):
    frontier = []  # priority queue (f, g, node, path)
    g_costs = {start: 0}
    start_f = g_costs[start] + heuristic(start)
    heapq.heappush(frontier, (start_f, g_costs[start], start, [start]))

    step = 1
    while frontier and step <= 3:
        f, g, current, path = heapq.heappop(frontier)

        print(f"Step {step}")
        print(f"Node selected: {current}")

        if current == goal:
            print(f"Goal reached at Step {step}")
            break

        new_frontier = []

        for nbr, cost in problem.neighbors(current):
            new_g = g + cost
            new_f = new_g + heuristic(nbr)
            heapq.heappush(frontier, (new_f, new_g, nbr, path + [nbr]))
            new_frontier.append((nbr, new_f))

        new_frontier.sort()

        frontier_states = [state for state, _ in new_frontier]
        print(f"New frontier set in alphabetical order: {', '.join(frontier_states)}\n")

        step += 1


problem = CraneProblem()
astar_tree_search("B", "A", problem)


# Step 1
# Select the node with the smallest f value from the frontier.

# Current frontier = {B} → Expand B
# Selected node: B
# Expanding B (State: Crane=Land, Holding=No, Container=Ship)
# Possible actions:
#   - Pick up is not possible
#     → The container is on the ship, but the crane is on land.
#   - Put down is not possible
#     → The crane is not holding anything.
#   - Move (Land → Ship, cost = 3)
#     → Generate node E (State: Ship, No, Ship)

#   g(E) = g(B) + 3 = 0 + 3 = 3
#   h(E) = 16
#   f(E) = 3 + 16 = 19

# Update frontier:
# - Remove B from the frontier and add E.
# - New frontier = {E}

# Step 1 result:
# Node selected: B
# New frontier: E (Only E remains, so alphabetical order is trivial)


# Step 2
# Current frontier = {E}

# Selected node: E (State: Ship, No, Ship)
# g(E) = 3, h(E) = 16, f(E) = 19

# Expanding E
# Possible actions for E (Ship, No, Ship):
# - Move (Ship → Land, cost = 3)
#   → Generate B (Land, No, Ship) as a new child (Tree Search allows duplicates).
#     g(B_new) = 3 + 3 = 6
#     h(B) = 20 (unchanged)
#     f(B_new) = 6 + 20 = 26
# - Pick up (cost = 10)
#   → Generate F (Ship, Yes, Ship)
#     g(F) = 3 + 10 = 13
#     h(F) = 9
#     f(F) = 13 + 9 = 22
# - Put down is not possible
#   → The crane is not holding anything.

# Update frontier:
# - Remove E from the frontier and add the child nodes B(new) and F.
# - New frontier = {B(new), F}
# - In alphabetical order: {B, F}

# Step 2 result:
# Node selected: E
# New frontier (alphabetical): B, F


# Step 3
# Current frontier = {B(new), F}

# B(new): f = 26
# F: f = 22
# → Since F has the smaller f value (22 < 26), select F for expansion.

# Expanding F (State: Ship, Yes, Ship)
# Possible actions:
# - Move (Ship → Land, cost = 7) (while holding the container)
#   → Generate C (Land, Yes, Land)
#     g(C) = g(F) + 7 = 13 + 7 = 20
#     h(C) = 3
#     f(C) = 20 + 3 = 23
# - Put down (cost = 3)
#   → Place the container on the ship, resulting in state E (Ship, No, Ship).
#   - In Tree Search, even if E has appeared before, it is treated as a new child node.
#     g(E_new) = 13 + 3 = 16
#     h(E) = 16 (same as before)
#     f(E_new) = 16 + 16 = 32
# - Pick up is not possible (already holding the container).

# Update frontier:
# - Retain B(new) in the frontier.
# - Add C and E(new).
# - New frontier = {B(new), C, E(new)}
# - B(new): f = 26
# - C: f = 23
# - E(new): f = 32
# - Alphabetical order: B, C, E

# Step 3 result:
# Node selected: F
# New frontier (alphabetical): B, C, E


############# Breadth-First Search (BFS) version #############
from collections import deque


class CraneProblemBFS:
    def __init__(self):
        # Define valid state transitions and their costs
        self.edges = {
            "B": [("E", 3)],  # Move Land → Ship (cost = 3)
            "E": [
                ("B", 3),  # Move Ship → Land (cost = 3)
                ("F", 10),  # Pick up container (cost = 10)
            ],
            "F": [
                ("C", 7),  # Move Ship → Land while holding container (cost = 7)
                ("E", 3),  # Put down container (cost = 3) → Return to E
            ],
            "C": [
                ("A", 3),  # Put down container (cost = 3)
                ("F", 10),  # Pick up container again (cost = 10)
            ],
        }

    def neighbors(self, node):
        """Returns valid next states and their corresponding costs."""
        return self.edges.get(node, [])


def bfs_tree_search(start, goal, problem):
    """
    Breadth-First Search (Tree Search Version)
    - Expands the shallowest nodes first.
    - Does not use a heuristic function (h(n)).
    - Since it does not track visited nodes, the same state may appear multiple times.
    """
    queue = deque([(start, 0, [start])])  # (node, cost, path)

    step = 1
    while queue and step <= 3:
        current, g, path = queue.popleft()  # Expand the first node in the queue

        print(f"Step {step}")
        print(f"Node selected: {current}")

        if current == goal:
            print(f"Goal reached at Step {step}")
            break

        new_frontier = []

        for neighbor, cost in problem.neighbors(current):
            new_g = g + cost
            queue.append((neighbor, new_g, path + [neighbor]))
            new_frontier.append((neighbor, new_g))

        new_frontier.sort()
        frontier_states = [state for state, _ in new_frontier]

        print(f"New frontier set in alphabetical order: {', '.join(frontier_states)}\n")

        step += 1


# Run the BFS-based search
problem_bfs = CraneProblemBFS()
bfs_tree_search("B", "A", problem_bfs)


############# Answer #############
# Step 1
#   Node selected: B
#   New frontier set in alphabetical order: E
# Step 2
#   Node selected: E
#   New frontier set in alphabetical order: B, F
# Step 3
#   Node selected: B
#   New frontier set in alphabetical order: E


# Step 1
# Select the shallowest node from the queue (FIFO order).

# Current frontier = {B} → Expand B
# Selected node: B
# Expanding B (State: Crane=Land, Holding=No, Container=Ship)

# Possible actions:
#   - Move (Land → Ship, cost = 3)
#     → Generate node E (State: Ship, No, Ship)
#     g(E) = g(B) + 3 = 0 + 3 = 3

# Update frontier:
# - Remove B from the queue and add E.
# - New frontier = {E}

# Step 1 result:
# Node selected: B
# New frontier: E (Only E remains, so alphabetical order is trivial)


# Step 2
# Current frontier = {E}

# Selected node: E (State: Ship, No, Ship)
# g(E) = 3

# Expanding E
# Possible actions:
# - Move (Ship → Land, cost = 3)
#   → Generate B (Land, No, Ship)
#     g(B_new) = 3 + 3 = 6
# - Pick up (cost = 10)
#   → Generate F (Ship, Yes, Ship)
#     g(F) = 3 + 10 = 13

# Update frontier:
# - Remove E from the queue and add B(new) and F.
# - New frontier = {B(new), F}
# - In alphabetical order: {B, F}

# Step 2 result:
# Node selected: E
# New frontier (alphabetical): B, F


# Step 3
# Current frontier = {B(new), F}

# B(new): g = 6
# F: g = 13
# → Since B has the lower g value (6 < 13), select B for expansion.

# Expanding B (State: Land, No, Ship)
# Possible actions:
# - Move (Land → Ship, cost = 3)
#   → Generate E again (Tree Search allows duplicates).
#     g(E_new) = 6 + 3 = 9

# Update frontier:
# - Retain F in the queue.
# - Add E(new) to the queue.
# - New frontier = {E(new), F}
# - Alphabetical order: {E, F}

# Step 3 result:
# Node selected: B
# New frontier (alphabetical): E, F


# Key Differences Between BFS and A*:
# 1. No Heuristic (h(n)) Used in BFS
#   BFS expands nodes level by level, ignoring the potential future cost.
#   A* considers both current cost (g(n)) and estimated future cost (h(n)).
# 2.BFS Always Selects the Shallowest Node First
#   This can lead to inefficient paths if the shortest path in terms of steps is not the optimal cost path.
#   A* is more efficient when a good heuristic is available.
# 3. Repeated States in BFS
#   Since Tree Search does not track visited nodes, BFS may generate the same state multiple times.
#   Graph Search (BFS with visited state tracking) would be more efficient.
