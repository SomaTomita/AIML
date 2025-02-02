############# Question #############

# Consider the following five sentences in propositional logic.

# 1. A∨B
# 2. A∨¬B∨C
# 3. ¬A∨B
# 4. ¬A∨C
# 5. ¬B∨¬C

# Apply two steps of the DPLL algorithm with the following assumptions:

# - When assigning a proposition symbol, the value true is assigned before false.
# - When performing unit propagation, the clauses are always processed in the order given above.

# For each step of DPLL, you will need to give the assignment made by DPLL followed by the consequences of that assignment, if there are any.
# Write your answer in the same format as this example:
# Step 1: B=true, C=false, A=true, fail

# Use the word fail to indicate that DPLL discovered a clause that is false in the current model, and success to indicate that all clauses are satisfied.


############# Answer #############
# ===============================
# Step 1: Assign A = true
# ===============================

# - We start by assigning A = true.
# - Now, we check for unit propagation.

# Clause (3): ¬A v B
# - Since A = true, ¬A becomes false.
# - This reduces the clause to: B.
# - **Unit Propagation → Assign B = true**

# Clause (5): ¬B v ¬C
# - Since B = true, ¬B becomes false.
# - This reduces the clause to: ¬C.
# - **Unit Propagation → Assign C = false**

# Now, we check if any clause is unsatisfied.

# Clause (4): ¬A v C
# - Since A = true, ¬A is false.
# - Since C = false, this makes the clause **false**.

# --> Step 1 Result:
# Step1: A=true, B=true, C=false, fail

# ===============================
# Step 2: Backtrack and Assign A = false
# ===============================

# - Since A = true failed, we now try A = false.

# Clause (1): A v B
# - Since A = false, the clause reduces to: B.
# - **Unit Propagation → Assign B = true**

# Clause (2): A v ¬B v C
# - Since A = false and B = true, ¬B becomes false.
# - This reduces the clause to: C.
# - **Unit Propagation → Assign C = true**

# Clause (5): ¬B v ¬C
# - Since B = true, ¬B becomes false.
# - Since C = true, ¬C becomes false.
# - This makes the entire clause false (contradiction).

# --> Step 2 Result:
# Step2: A=false, B=true, C=true, fail


############# Question1 #############

# Consider the following five sentences in propositional logic.

# 1. A∨B
# 2. A∨¬B∨C
# 3. ¬A∨B
# 4. ¬A∨¬B∨C
# 5. ¬B∨¬C

# Apply two steps of the DPLL algorithm with the following assumptions:

# When assigning a proposition symbol, the value true is assigned before false.
# When performing unit propagation, the clauses are always processed in the order given above.

# For each step of DPLL, you will need to give the assignment made by DPLL followed by the consequences of that assignment, if there are any.
# Write your answer in the same format as this example:
# Step 1: B=true, C=false, A=true, fail

# Use the word fail to indicate that DPLL discovered a clause that is false in the current model, and success to indicate that all clauses are satisfied.


############# Answer1 #############
# Step1: A=true, B=true, C=true, fail
# Step2: A=false, B=true, C=true, fail


# Step-by-step breakdown :
# DPLL assigns variables in order (A → B → C), always trying True before False.
# Unit Propagation: If a clause has only one remaining variable, that variable must be set to satisfy the clause.
# Backtracking: If a conflict (contradiction) is found, we undo the last assignment and try the next possible value.
# Fail Condition: If a clause becomes completely false (all literals are false), the current assignment is invalid.


# ===============================
# Step 1: Assign A = true
# ===============================

# - Start by assigning A = true (since we always assign True before False).
# - Now, we check which clauses become unit clauses (i.e., clauses where only one literal remains unset).

# Clause (3): ¬A v B
# - Since A = true, ¬A becomes false.
# - This reduces clause (3) to: B.
# - Since it's a unit clause, we must set B = true for Step1 conditon.

# Clause (4): ¬A v ¬B v C
# - Since A = true, ¬A becomes false.
# - Since B = true, ¬B becomes false.
# - This reduces clause (4) to: C.
# - Since it's a unit clause, we must set C = true for Step1 conditon.

# Now, we check clause (5): ¬B v ¬C
# - Since B = true, ¬B becomes false.
# - Since C = true, ¬C becomes false.
# - This makes the entire clause false (contradiction).

# The contradiction means that this branch(Assign A = true) **fails**.
# Step1: A=true, B=true, C=true, fail


# ===============================
# Step 2: Backtrack → Assign A = false
# ===============================

# - Since A = true failed, we now try A = false.
# - Again, we check for unit clauses.

# Clause (1): A v B
# - Since A = false, this reduces clause (1) to: B.
# - Since it's a unit clause, we must set B = true.

# Clause (2): A v ¬B v C
# - Since A = false, this reduces clause (2) to: ¬B v C.
# - Since B = true, ¬B becomes false.
# - This reduces the clause to: C.
# - Since it's a unit clause, we must set C = true.

# Now, we check clause (5): ¬B v ¬C
# - Since B = true, ¬B becomes false.
# - Since C = true, ¬C becomes false.
# - This makes the entire clause false (contradiction).

# Again, the contradiction means that this branch **fails**.
# Step2: A=false, B=true, C=true, fail


# Here are all 8 possible assignments:
# A,	B,	C
# True,	 True, True
# True,	 True, False
# True,	 False,	True
# True,	 False,	False
# False,	True,	True
# False,	True,	False
# False,	False,	True
# False,	False,	False


############# Question2 #############
# Consider the following six sentences in propositional logic.

# 1. A∨B
# 2. A∨¬B∨C
# 3. ¬A∨B
# 4. ¬A∨¬B∨C
# 5. ¬B∨¬C
# 6. ¬C∨A

# Apply two steps of the DPLL algorithm with the following assumptions:

# - When assigning a proposition symbol, the value true is assigned before false.
# - When performing unit propagation, the clauses are always processed in the order given above.

# For each step of DPLL, you will need to give the assignment made by DPLL followed by the consequences of that assignment, if there are any.
# Write your answer in the same format as this example:
# Step 1: B=true, C=false, A=true, fail

# Use the word fail to indicate that DPLL discovered a clause that is false in the current model, and success to indicate that all clauses are satisfied.


############# Answer2 #############
# ===============================
# Step 1: Assign A = true
# ===============================

# - We start by assigning A = true.
# - Now, we check for unit propagation.

# Clause (3): ¬A v B
# - Since A = true, ¬A becomes false.
# - This reduces the clause to: B.
# - **Unit Propagation → Assign B = true**

# Clause (5): ¬B v ¬C
# - Since B = true, ¬B becomes false.
# - This reduces the clause to: ¬C.
# - **Unit Propagation → Assign C = false**

# Clause (6): ¬C v A
# - Since C = false, ¬C becomes true.
# - This clause is already satisfied.

# Clause (4): ¬A v ¬B v C
# - Since A = true, ¬A is false.
# - Since B = true, ¬B is false.
# - Since C = false, this makes the clause **false**.

# --> Step 1 Result:
# Step1: A=true, B=true, C=false, fail

# ===============================
# Step 2: Backtrack and Assign A = false
# ===============================

# - Since A = true failed, we now try A = false.

# Clause (1): A v B
# - Since A = false, the clause reduces to: B.
# - **Unit Propagation → Assign B = true**

# Clause (2): A v ¬B v C
# - Since A = false and B = true, ¬B becomes false.
# - This reduces the clause to: C.
# - **Unit Propagation → Assign C = true**

# Clause (5): ¬B v ¬C
# - Since B = true, ¬B becomes false.
# - Since C = true, ¬C becomes false.
# - This makes the entire clause false (contradiction).

# --> Step 2 Result:
# Step2: A=false, B=true, C=true, fail
