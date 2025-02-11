############# Question #############
# Consider the "greedy-best-first-search.png" map where each connection between two cities is labelled with the distance by road.
# The following table contains the distance by road between each pair of cities that are connected by a road:

# City 1       City 2       Distance by road
# ------------------------------------------
# Malton       Scarborough   17
# Thirsk       Malton        5
# York         Malton        12
# Pocklington  Malton        10
# Thirsk       York          6
# York         Pocklington   11
# Thirsk       Harrogate     12
# Harrogate    Leeds         10
# York         Leeds         16
# Pocklington  Wakefield     15
# Leeds        Wakefield     8

# In addition to the map and table above, the following table contains the Euclidean (straight line) distances from all other cities to Pocklington:

# City           Euclidean distance to Pocklington
# ----------------------------------------------
# Scarborough     19
# Malton          10
# York            8
# Thirsk          12
# Harrogate       20
# Leeds           17
# Wakefield       12

# This question is about applying the Graph Search version of Greedy Best-First Search (GBFS) to find a path from Harrogate to Pocklington.
# One step of the algorithm consists of selecting a node from the frontier, potentially expanding it and adding any relevant child nodes to the frontier.
# The initial frontier will contain only Harrogate (H). Execute GBFS for 4 steps.
# For each step, specify which node is chosen to be expanded, and give the new frontier as a sequence of states (represented by letters) in alphabetical order.
# For example, W is expanded and the new frontier set is LP.

# <Step 1>
#   Node selected:
#   New frontier in alphabetical order:
# <Step 2>
#   Node selected:
#   New frontier in alphabetical order:
# <Step 3>
#   Node selected:
#   New frontier in alphabetical order:
# <Step 4>
#   Node selected:
#   New frontier in alphabetical order:

############# Answer #############
# <Step 1>
#   Node selected: H
#   New frontier: L, T
# <Step 2>
#   Node selected: T
#   New frontier: L, M, Y
# <Step 3>
#   Node selected: Y
#   New frontier: L, M, P
# <Step 4>
#   Node selected: P
#   New frontier: L, M, W

# Summary:
# 1. At each step, GBFS picks the node with the smallest straight-line distance to the goal (P).
# 2. Harrogate’s neighbors (L, T) enter the frontier first.
# 3. Thirsk (h=12) is chosen before Leeds (h=17), leading to York (h=8), then Pocklington (h=0).
# 4. Once Pocklington is expanded, its unvisited neighbor Wakefield (h=12) joins the frontier.


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
graph = {
    "Malton": {"Scarborough": 17, "Thirsk": 5, "York": 12, "Pocklington": 10},
    "Scarborough": {"Malton": 17},
    "Thirsk": {"Malton": 5, "York": 6, "Harrogate": 12},
    "York": {"Malton": 12, "Thirsk": 6, "Pocklington": 11, "Leeds": 16},
    "Pocklington": {"Malton": 10, "York": 11, "Wakefield": 15},
    "Harrogate": {"Thirsk": 12, "Leeds": 10},
    "Leeds": {"Harrogate": 10, "York": 16, "Wakefield": 8},
    "Wakefield": {"Pocklington": 15, "Leeds": 8},
}

heuristic = {
    "Scarborough": 19,
    "Malton": 10,
    "York": 8,
    "Thirsk": 12,
    "Harrogate": 20,
    "Leeds": 17,
    "Wakefield": 12,
    "Pocklington": 0,
}

city_code_map = {
    "Harrogate": "H",
    "Thirsk": "T",
    "Leeds": "L",
    "York": "Y",
    "Malton": "M",
    "Scarborough": "S",
    "Pocklington": "P",
    "Wakefield": "W",
}


def greedy_best_first_search(start, goal, graph, heuristic, city_code_map, max_steps=4):
    """
    Performs a Graph Search version of Greedy Best-First Search (GBFS).
    Prints the node selected at each step and the frontier in alphabetical order.
    By default, prints up to 'max_steps' steps.
    """
    import heapq

    visited = set()
    # Frontier will be a min-heap of tuples: (heuristic_value, city_name)
    frontier = []
    # Initialize frontier with the start node
    heapq.heappush(frontier, (heuristic[start], start))

    step = 1
    while frontier and step <= max_steps:
        # Pop the city with the smallest heuristic
        _, current_city = heapq.heappop(frontier)

        # Print Step information
        print(f"<Step {step}>")
        print(f"  Node selected: {city_code_map[current_city]}")

        visited.add(current_city)

        # Expand the current city: add unvisited neighbors to the frontier
        for neighbor in graph[current_city]:
            if neighbor not in visited:
                # If neighbor not already in frontier, add it
                # (For GBFS, duplicates can sometimes exist; for simplicity, we'll skip adding duplicates)
                if not any(n == neighbor for (_, n) in frontier):
                    heapq.heappush(frontier, (heuristic[neighbor], neighbor))

        # Sort frontier alphabetically by the city *codes* (e.g., H, L, M...)
        frontier_codes = sorted(city_code_map[n] for (_, n) in frontier)
        print(f"  New frontier: {', '.join(frontier_codes)}\n")

        step += 1

        # Stop if we've reached the goal (not strictly necessary for a pure demonstration)
        if current_city == goal:
            break


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
############# Question1 #############
# Consider the same map and graph structure as in the previous question, but ignore the road distances (treating each edge equally).
# We apply a simple Breadth-First Search (BFS) starting from Harrogate (H) to find Pocklington (P).

# One step of BFS consists of:
#   1. Removing the front-most node from the queue (frontier).
#   2. Expanding it by adding its unvisited neighbors to the queue in alphabetical order.

# The initial frontier will contain only Harrogate (H).
# Execute BFS for 4 steps.
# For each step, specify which node is chosen (removed from the queue)
# And show the new frontier as a sequence of states in alphabetical order.

# ############# Answer1 #############
# <Step 1>
#   Node selected: H
#   New frontier: L, T
# <Step 2>
#   Node selected: L
#   New frontier: T, W, Y
# <Step 3>
#   Node selected: T
#   New frontier: M, W, Y
# <Step 4>
#   Node selected: M
#   New frontier: P, W, Y

# memo
# 1. both M and W are at depth 2 (directly connected to a node at depth 1, L and T respectively).
#    The frontier is sorted alphabetically, so M comes before W.
# 2. BFS is FIFO.
#    W was inserted into the queue before M (Step 2 vs. Step 3), so W gets expanded first.

# Summary of BFS:
# 1. BFS expands nodes in "layers," so each step removes the left-most node in the queue.
# 2. All unvisited neighbors of the selected node are added to the queue in alphabetical order.
# 3. This process continues until we reach the goal or exhaust the queue.

# Below is a BFS code example (using an unweighted adjacency list) that demonstrates this approach.
# The "queue" replaces the "priority queue" from GBFS.


def bfs_path_steps(graph, start, goal, city_code_map, max_steps=4):
    """
    Simple BFS that prints each step (which node is removed from the queue)
    and the resulting frontier in alphabetical order.
    """
    from collections import deque

    visited = set()
    queue = deque([start])
    visited.add(start)
    step = 1

    while queue and step <= max_steps:
        current_city = queue.popleft()
        print(f"<Step {step}>")
        print(f"  Node selected: {city_code_map[current_city]}")

        # Enqueue unvisited neighbors, in alphabetical order of their codes
        neighbors = list(graph[current_city])
        neighbors_sorted = sorted(neighbors, key=lambda x: city_code_map[x])
        for neighbor in neighbors_sorted:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        # Print the frontier in alphabetical order
        frontier_codes = sorted(city_code_map[city] for city in queue)
        print(f"  New frontier: {', '.join(frontier_codes)}\n")

        # If we've reached the goal, we could stop here, but we continue for demonstration
        step += 1


if __name__ == "__main__":
    # Unweighted adjacency list for BFS (treating each edge equally)
    graph_unweighted = {
        "Malton": ["Scarborough", "Thirsk", "York", "Pocklington"],
        "Scarborough": ["Malton"],
        "Thirsk": ["Malton", "York", "Harrogate"],
        "York": ["Malton", "Thirsk", "Pocklington", "Leeds"],
        "Pocklington": ["Malton", "York", "Wakefield"],
        "Harrogate": ["Thirsk", "Leeds"],
        "Leeds": ["Harrogate", "York", "Wakefield"],
        "Wakefield": ["Pocklington", "Leeds"],
    }

    city_code_map = {
        "Harrogate": "H",
        "Thirsk": "T",
        "Leeds": "L",
        "York": "Y",
        "Malton": "M",
        "Scarborough": "S",
        "Pocklington": "P",
        "Wakefield": "W",
    }

    print("############# BFS Step-by-Step #############")
    bfs_path_steps(
        graph_unweighted, "Harrogate", "Pocklington", city_code_map, max_steps=4
    )


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
############# Question2 #############
# Now let's restate Dijkstra's Algorithm question in the same "step-by-step" style:

# Considering actual road distances in the graph, we apply Dijkstra's Algorithm to find
# the shortest path from Harrogate (H) to Pocklington (P).

# One step of Dijkstra's Algorithm consists of:
#   1. Selecting the node with the smallest current distance from the start (in the frontier).
#   2. Expanding it by relaxing edges to its neighbors (i.e., checking if we can improve the distance to neighbor nodes).

# The initial frontier will contain only Harrogate (H) with distance 0.
# Execute Dijkstra for 4 expansions (steps). For each step, specify which node is chosen
# (the one with the smallest distance found so far) and show the new frontier (unsettled nodes)
# in an order sorted by their city codes (for demonstration purposes).

############# Answer2 #############
# <Step 1>
#   Node selected: H (distance so far: 0)
#   New frontier: L (10), T (12)
# <Step 2>
#   Node selected: L (distance so far: 10)
#   New frontier: T (12), W (18), Y (26)
# <Step 3>
#   Node selected: T (distance so far: 12)
#   New frontier: M (17), W (18), Y (18), Y (26)
# <Step 4>
#   Node selected: M (distance so far: 17)
#   New frontier: P (27), S (34), W (18), Y (18), Y (26)

# Dijkstra’s Algorithm will eventually produce the shortest total distance to P from H.
# Below is an illustrative code snippet that shows how we might track these expansions.


import heapq


def dijkstra_steps(graph, start, goal, city_code_map, max_steps=4):
    """
    Performs Dijkstra's Algorithm in a step-by-step fashion.
    Prints the node chosen at each step and the frontier afterward.
    This is for demonstration purposes: we break after 'max_steps' expansions.
    """
    # distances will keep track of the best known distance to each node
    distances = {city: float("inf") for city in graph}
    distances[start] = 0

    # Each entry in the frontier: (distance_from_start, city, path_to_city)
    frontier = [(0, start, [start])]
    visited = set()
    step = 1

    while frontier and step <= max_steps:
        cur_dist, current_city, path_so_far = heapq.heappop(frontier)

        # If we've already visited this node in a better way, skip
        if current_city in visited:
            continue
        visited.add(current_city)

        print(f"<Step {step}>")
        print(
            f"  Node selected: {city_code_map[current_city]} (distance so far: {cur_dist})"
        )

        # Relax edges from the current city
        for neighbor, dist in graph[current_city].items():
            new_dist = cur_dist + dist
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                new_path = path_so_far + [neighbor]
                heapq.heappush(frontier, (new_dist, neighbor, new_path))

        # After expansion, show what's in the frontier in alphabetical order by code
        # but we won't reorder the actual heap (just for printing)
        frontier_cities = [city_code_map[node] for (_, node, _) in frontier]
        frontier_cities_sorted = sorted(frontier_cities)
        print(f"  New frontier: {', '.join(frontier_cities_sorted)}\n")

        # If we've reached the goal, we could break here, but we'll continue for demonstration
        step += 1


if __name__ == "__main__":
    graph_weighted = {
        "Malton": {"Scarborough": 17, "Thirsk": 5, "York": 12, "Pocklington": 10},
        "Scarborough": {"Malton": 17},
        "Thirsk": {"Malton": 5, "York": 6, "Harrogate": 12},
        "York": {"Malton": 12, "Thirsk": 6, "Pocklington": 11, "Leeds": 16},
        "Pocklington": {"Malton": 10, "York": 11, "Wakefield": 15},
        "Harrogate": {"Thirsk": 12, "Leeds": 10},
        "Leeds": {"Harrogate": 10, "York": 16, "Wakefield": 8},
        "Wakefield": {"Pocklington": 15, "Leeds": 8},
    }

    city_code_map = {
        "Harrogate": "H",
        "Thirsk": "T",
        "Leeds": "L",
        "York": "Y",
        "Malton": "M",
        "Scarborough": "S",
        "Pocklington": "P",
        "Wakefield": "W",
    }

    print("############# Dijkstra Step-by-Step #############")
    dijkstra_steps(
        graph_weighted, "Harrogate", "Pocklington", city_code_map, max_steps=4
    )
