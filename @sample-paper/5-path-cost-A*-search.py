############# Question1 #############
# What condition must a heuristic function h(n) satisfy for A* Search to guarantee finding the shortest path?

############# Answer1 #############
# The heuristic h(n) must be:
# Admissible: h(n) =< h*(n), where h*(n) is the true cost to reach the goal from node n.
# Consistent (Monotonicity): For every node n and its successor n', the following must hold: h(n) =< c(n,n')+h(n'), where c(n,n') is the cost of the edge from n to n'.


############# Question2 #############
# Write the evaluation function of Greedy Best-First Search in terms of the heuristic h(n).

############# Answer2 #############
# f(n)=h(n)


############# Question3 #############
# Write the evaluation function of A* Search in terms of the path cost g(n) and the heuristic h(n).

############# Answer3 #############
# f(n) = g(n) + h(n)
# g(n): The cost of the path from the start node to the current node n.
# h(n): The heuristic estimate of the cost to reach the goal from node n.
