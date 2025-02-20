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
# Possible Assignments After One Step
# (Starting from A = false, B = false, C = false)

# 1) A = true, B = false, C = false
# 2) A = false, B = true, C = false

# Explanation of WalkSAT Steps

# 1. Identify Unsatisfied Clauses
#    Initial Assignment: A = false, B = false, C = false
#    Evaluate each clause:
#      Clause 1: A ∨ B
#        false ∨ false → false   (unsatisfied)
#      Clause 2: A ∨ ¬B ∨ C
#        false ∨ true ∨ false → true  (satisfied)
#      Clause 3: ¬A ∨ B
#        true ∨ false → true          (satisfied)
#      Clause 4: ¬A ∨ ¬B ∨ C
#        true ∨ true ∨ false → true   (satisfied)
#    => Only Clause 1 (A ∨ B) is unsatisfied.

# 2. Random Walk vs. Greedy Flip
#    - With probability p = 0.5, pick a random variable from the unsatisfied clause (A ∨ B) and flip it.
#    - With probability 1 − p = 0.5, pick the variable in the clause whose flip satisfies the most clauses.
#      (In this case, flipping either A or B leads to Clause 1 becoming satisfied, so either is valid.)

# 3. Possible Outcomes
#    - Flip A: A becomes true, so new assignment is (A = true, B = false, C = false).
#    - Flip B: B becomes true, so new assignment is (A = false, B = true, C = false).

# Note:
# Flipping C is NOT an option in the first step because C is not part of the unsatisfied clause.
# Therefore, (A = false, B = false, C = true) cannot be reached in this single step.


# ---------------------------------------------------------
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


# Pros and Cons
# 	Pros:
# 	•	The algorithm efficiently focuses on unsatisfied clauses, ensuring progress toward satisfying more clauses.
# 	•	The random-walk component helps avoid getting stuck in local maxima.
# 	Cons:
# 	•	There is still a chance of repeatedly flipping variables in unsatisfied clauses without reaching a globally optimal solution.
# 	•	Probability tuning (value of p) can be tricky and heavily influences the performance.
# ---------------------------------------------------------


############# Question2 #############
# Given the same four clauses:
# 1. A ∨ B
# 2. A ∨ ¬B ∨ C
# 3. ¬A ∨ B
# 4. ¬A ∨ ¬B ∨ C

# Which assignments of (A, B, C) satisfy all four clauses?
# Select all that apply from the eight possible assignments:

# 1) A = false, B = false, C = false
# 2) A = false, B = false, C = true
# 3) A = false, B = true, C = false
# 4) A = false, B = true, C = true
# 5) A = true, B = false, C = false
# 6) A = true, B = false, C = true
# 7) A = true, B = true, C = false
# 8) A = true, B = true, C = true


############# Answer2 #############
#   (A=false, B=true, C=true)  --> #4
#   (A=true, B=true, C=true)   --> #8

# ---------------------------------------------------------
# 1) A = false, B = false, C = false
#    Clause 1: A ∨ B = false ∨ false = false (fails here)
#    => Not all satisfied

# 2) A = false, B = false, C = true
#    Clause 1: A ∨ B = false ∨ false = false (fails here)
#    => Not all satisfied

# 3) A = false, B = true, C = false
#    Clause 1: false ∨ true = true
#    Clause 2: false ∨ ¬(true) ∨ false = false ∨ false ∨ false = false (fails)
#    => Not all satisfied

# 4) A = false, B = true, C = true
#    Clause 1: false ∨ true = true
#    Clause 2: false ∨ ¬(true) ∨ true = false ∨ false ∨ true = true
#    Clause 3: ¬(false) ∨ true = true ∨ true = true
#    Clause 4: ¬(false) ∨ ¬(true) ∨ true = true ∨ false ∨ true = true
#    => All four clauses satisfied

# 5) A = true, B = false, C = false
#    Clause 1: true ∨ false = true
#    Clause 2: true ∨ ¬(false) ∨ false = true ∨ true ∨ false = true
#    Clause 3: ¬(true) ∨ false = false ∨ false = false (fails)
#    => Not all satisfied

# 6) A = true, B = false, C = true
#    Clause 1: true ∨ false = true
#    Clause 2: true ∨ ¬(false) ∨ true = true ∨ true ∨ true = true
#    Clause 3: ¬(true) ∨ false = false ∨ false = false (fails)
#    => Not all satisfied

# 7) A = true, B = true, C = false
#    Clause 1: true ∨ true = true
#    Clause 2: true ∨ ¬(true) ∨ false = true ∨ false ∨ false = true
#    Clause 3: ¬(true) ∨ true = false ∨ true = true
#    Clause 4: ¬(true) ∨ ¬(true) ∨ false = false ∨ false ∨ false = false (fails)
#    => Not all satisfied

# 8) A = true, B = true, C = true
#    Clause 1: true ∨ true = true
#    Clause 2: true ∨ ¬(true) ∨ true = true ∨ false ∨ true = true
#    Clause 3: ¬(true) ∨ true = false ∨ true = true
#    Clause 4: ¬(true) ∨ ¬(true) ∨ true = false ∨ false ∨ true = true
#    => All four clauses satisfied

# ---------------------------------------------------------


############# Question3 #############
# Consider the following four clauses in propositional logic, each involving the three variables A, B, and C:

# 1. A ∨ B
# 2. ¬A ∨ C
# 3. B ∨ ¬C
# 4. ¬A ∨ ¬B ∨ C

# Out of the eight possible assignments for (A, B, C), which ones satisfy all four clauses?

# Please check each of the following assignments:

# 1) A = false, B = false, C = false
# 2) A = false, B = false, C = true
# 3) A = false, B = true,  C = false
# 4) A = false, B = true,  C = true
# 5) A = true,  B = false, C = false
# 6) A = true,  B = false, C = true
# 7) A = true,  B = true,  C = false
# 8) A = true,  B = true,  C = true

############# Answer3 #############
#   (A = false, B = true, C = false)   -- #3
#   (A = false, B = true, C = true)    -- #4
#   (A = true,  B = true, C = true)    -- #8

# ---------------------------------------------------------
# 1) A = false, B = false, C = false
#    Clause 1: A ∨ B = false ∨ false = false   (fails)
#    => Not all satisfied

# 2) A = false, B = false, C = true
#    Clause 1: false ∨ false = false           (fails)
#    => Not all satisfied

# 3) A = false, B = true, C = false
#    Clause 1: false ∨ true = true
#    Clause 2: ¬(false) ∨ false = true ∨ false = true
#    Clause 3: true ∨ ¬(false) = true ∨ true = true
#    Clause 4: ¬(false) ∨ ¬(true) ∨ false = true ∨ false ∨ false = true
#    => All clauses satisfied

# 4) A = false, B = true, C = true
#    Clause 1: false ∨ true = true
#    Clause 2: true ∨ true = true
#    Clause 3: true ∨ ¬(true) = true ∨ false = true
#    Clause 4: true ∨ false ∨ true = true
#    => All clauses satisfied

# 5) A = true, B = false, C = false
#    Clause 1: true ∨ false = true
#    Clause 2: ¬(true) ∨ false = false ∨ false = false   (fails)
#    => Not all satisfied

# 6) A = true, B = false, C = true
#    Clause 1: true ∨ false = true
#    Clause 2: false ∨ true = true
#    Clause 3: false ∨ ¬(true) = false ∨ false = false   (fails)
#    => Not all satisfied

# 7) A = true, B = true, C = false
#    Clause 1: true ∨ true = true
#    Clause 2: false ∨ false = false                      (fails)
#    => Not all satisfied

# 8) A = true, B = true, C = true
#    Clause 1: true ∨ true = true
#    Clause 2: false ∨ true = true
#    Clause 3: true ∨ ¬(true) = true ∨ false = true
#    Clause 4: false ∨ ¬(true) ∨ true = false ∨ false ∨ true = true
#    => All clauses satisfied

# ---------------------------------------------------------


############# Question4 #############
# Consider the following three sentences in propositional logic:

# 1. A ∨ B
# 2. A ∨ ¬B
# 3. A ∨ B ∨ ¬C

# Apply one step of the WalkSAT algorithm with the following assumptions:
# - The probability p of making a random walk move is set to 0.
# - The starting assignment is:
A = False
B = False
C = True
# - The algorithm chooses clause 3.

# For each proposition symbol in clause 3, how many clauses would be satisfied in total if the symbol were flipped?
# A: ??
# B: ??
# C: ??

############# Answer4 #############
# A: 3
# B: 2
# C: 2

# ---------------------------------------------------------

# Step 1: Evaluate clause 3 under the current assignment
# Clause 3: A ∨ B ∨ ¬C
# Substituting the values: False ∨ False ∨ ¬True
#                         False ∨ False ∨ False
#                         = False (Not satisfied)

# Step 2: Consider flipping each symbol in clause 3 and count satisfied clauses
# (1) Flip A (A becomes True)
A = True
# Clause 1: A ∨ B = True ∨ False = True (Satisfied)
# Clause 2: A ∨ ¬B = True ∨ True = True (Satisfied)
# Clause 3: A ∨ B ∨ ¬C = True ∨ False ∨ False = True (Satisfied)
# Total satisfied clauses = 3

# (2) Flip B (B becomes True)
A = False  # Reset A to its original value
B = True
# Clause 1: A ∨ B = False ∨ True = True (Satisfied)
# Clause 2: A ∨ ¬B = False ∨ False = False (Not satisfied)
# Clause 3: A ∨ B ∨ ¬C = False ∨ True ∨ False = True (Satisfied)
# Total satisfied clauses = 2

# (3) Flip C (C becomes False)
B = False  # Reset B to its original value
C = False
# Clause 1: A ∨ B = False ∨ False = False (Not satisfied)
# Clause 2: A ∨ ¬B = False ∨ True = True (Satisfied)
# Clause 3: A ∨ B ∨ ¬C = False ∨ False ∨ True = True (Satisfied)
# Total satisfied clauses = 2

# Step 3: Choose the best variable to flip
# - Flipping A results in 3 satisfied clauses
# - Flipping B results in 2 satisfied clauses
# - Flipping C results in 2 satisfied clauses

# Since flipping A satisfies the most clauses, it is the best choice.
# ---------------------------------------------------------
