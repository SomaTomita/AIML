############# Question #############

# Consider the following four sentences in propositional logic.
# 1. A∨B
# 2. A∨¬B∨C
# 3. ¬A∨B
# 4. ¬A∨¬B∨C
# Suppose you are using the WalkSAT algorithm with the following assumptions:
# * The probability p of making a random walk move is set to 0.5
# * The starting assignment is A=false, B=false, C=false.

# Which of the following assignments can be reached by executing one step of WalkSAT? Select all the assignments that can be reached.

# A = false, B = false, C = false
# A = false, B = false, C = true
# A = false, B = true, C = false
# A = false, B = true, C = true
# A = true, B = false, C = false
# A = true, B = false, C = true
# A = true, B = true, C = false
# A = true, B = true, C = true


############# Answer #############
# A = false, B = false, C = false
# A = true, B = false, C = false
# A = false, B = true, C = false
# A = false, B = false, C = true


# The WalkSAT algorithm works by:
# Selecting an unsatisfied clause at random.
# With probability p, flipping the value of a randomly chosen variable in that clause (random walk move).
# With probability 1−p, flipping the variable that maximizes the number of satisfied clauses.


# Given:
# Initial assignment: A = false, B = false, C = false
# Probability p = 0.5

# Step-by-step Analysis:

# Initial Assignment:
# Evaluate the truth of each clause:
# Clause 1: A ∨ B
#   false ∨ false → false (unsatisfied)
# Clause 2: A ∨ ¬B ∨ C
#   false ∨ true ∨ false → true (satisfied)
# Clause 3: ¬A ∨ B
#   true ∨ false → true (satisfied)
# Clause 4: ¬A ∨ ¬B ∨ C
#   true ∨ true ∨ false → true (satisfied)

# → Clause 1 is the only unsatisfied clause: A ∨ B.

# Possible Actions:
# Since A ∨ B is unsatisfied, WalkSAT will:
# 1. Choose A or B (the variables in the unsatisfied clause) randomly.
# 2. Flip the chosen variable's truth value.
# If A is flipped:
# A = true, B = false, C = false
# If B is flipped:
# A = false, B = true, C = false
# Random Walk Move:
# With probability p = 0.5, any variable in any unsatisfied clause may be flipped randomly.
# This means:
# C could also be flipped to true.


############# Python Code : WalkSAT algorithm #############
import random


def evaluate_clause(clause, assignment):
    """
    Evaluates if a given clause is satisfied under the current variable assignment.
    """
    # any is a function that returns True if any element is True
    return any(literal(assignment) for literal in clause)


def walksat_one_step(A=False, B=False, C=False, p=0.5):
    """
    Performs one step of the WalkSAT algorithm given the initial assignment and probability p.
    """
    # Define clauses as lambda functions for evaluation
    clauses = [
        [lambda x: x["A"], lambda x: x["B"]],  # A ∨ B
        [lambda x: x["A"], lambda x: not x["B"], lambda x: x["C"]],  # A ∨ ¬B ∨ C
        [lambda x: not x["A"], lambda x: x["B"]],  # ¬A ∨ B
        [lambda x: not x["A"], lambda x: not x["B"], lambda x: x["C"]],  # ¬A ∨ ¬B ∨ C
    ]

    # Initial variable assignment
    assignment = {"A": A, "B": B, "C": C}

    # Identify unsatisfied clauses
    unsatisfied_clauses = [
        clause for clause in clauses if not evaluate_clause(clause, assignment)
    ]

    if not unsatisfied_clauses:
        return assignment  # If no clause is unsatisfied, return current assignment

    # Select an unsatisfied clause randomly
    chosen_clause = random.choice(unsatisfied_clauses)

    # Extract the variables involved in the chosen clause
    involved_vars = [
        var
        for var in ["A", "B", "C"]
        if any(
            # Make a copy of the dictionary and change some values → {**dict, key: value}
            l(assignment) != l({**assignment, var: not assignment[var]})
            for l in chosen_clause
        )
    ]

    # Apply WalkSAT rules
    if random.random() < p:
        # Random walk: Flip any random variable (including C)
        var_to_flip = random.choice(["A", "B", "C"])
    else:
        # Greedy move: Flip the variable that maximizes the number of satisfied clauses
        best_var = max(
            involved_vars,
            key=lambda v: sum(
                evaluate_clause(c, {**assignment, v: not assignment[v]})
                for c in clauses
            ),
        )
        var_to_flip = best_var

    # Flip the selected variable
    assignment[var_to_flip] = not assignment[var_to_flip]

    return assignment


# Run the function and print possible new assignments
if __name__ == "__main__":
    reached_assignments = set()
    for _ in range(1000):  # Run multiple times to capture stochastic behavior
        new_assignment = walksat_one_step(A=False, B=False, C=False, p=0.5)
        reached_assignments.add(tuple(sorted(new_assignment.items())))

    print("Possible assignments after one step of WalkSAT:")
    for assignment in sorted(reached_assignments):
        print(dict(assignment))
