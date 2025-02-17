############# Question1 #############
# In propositional logic, if there are n proposition symbols, and one of the symbols is constrained to always be true, how many models are there?

############# Answer1 #############
# 2**(n-1)
# If one symbol is fixed as true, the remaining (n-1)symbols can take either true or false.
# For example, if n=5 and one symbol is always true, the number of models is: 16.


# ----------------------------------------------------------
############# Question2 #############
# In propositional logic, suppose there are four proposition symbols A, B, C, D.
# How many models are there?

############# Answer2 #############
# 16 models.
# In propositional logic, each proposition symbol can take one of two truth values: true or false.
# If there are n  proposition symbols, the total number of models is 2**n


# ----------------------------------------------------------
############# Question3 #############
# In propositional logic, using four proposition symbols A, B, C, D,
# how many models are there of the formula B ∧ ¬D?
# In other words, how many truth assignments satisfy B ∧ ¬D?

############# Answer3 #############
# 4 models satisfy "B ∧ ¬D".

# A model (or satisfying assignment) is a truth assignment to all propositional variables that makes the given formula true.
# - B must be true.
# - D must be false.
# - The values of A and C are not restricted by the formula, meaning they can be either true or false independently.

# Since A and C are free variables, they each have 2 possible truth values:
# - A can be true or false (2 choices).
# - C can be true or false (2 choices).s

# Total models = 2 (choices for A) × 2 (choices for C) = 4


# ----------------------------------------------------------
# ############# Question 4 #############
# In propositional logic, using four proposition symbols A, B, C, D,
# how many models satisfy the formula (A ∨ C) ∧ ¬B?

# ############# Answer 4 #############
# Step 0:
# ∨ = OR
# ∧ = AND

# Step 1: Understand the constraints imposed by the formula (A ∨ C) ∧ ¬B.
# - ¬B means B must be false.
# - A ∨ C means at least one of A or C must be true.

# Step 2: Determine the possible values for A and C that satisfy A ∨ C.
# - (A = True, C = Ture, False) → Valid
# - (A = False, C = True) → Valid
# - (A = False, C = False) → Invalid (violates A ∨ C)

# Step 3: Calculate the number of models.
# - B is fixed as False (1 choice).
# - A and C can be (True, Any) or (False, True), leading to 3 valid combinations.
# - D is unrestricted (2 choices: True or False).

# Total models = 3 (valid A, C assignments) × 2 (choices for D) = 6 models.


# ----------------------------------------------------------
# ############# Question 5 #############
# Suppose we have five propositional symbols: A, B, C, D, E.
# A new constraint is introduced: If A is true, then B must be false.
# Additionally, D must be true in all models.
# How many models satisfy these constraints?

# ############# Answer 5 #############
# Step 1: Interpret the constraints.
# - If A = True, then B must be False (A → ¬B).
# - D is fixed as True.
# - C and E remain unrestricted and can take any value (True or False).

# Step 2: Count the valid assignments.
# - A can be True or False (2 choices).
# - If A = True → B must be False (1 forced choice).
# - If A = False → B can be either True or False (2 choices).
# - C and E are unrestricted (2 choices each).

# Case 1: A = True → B = False, C and E unrestricted.
# Models: 1 (forced B) × 2 (C) × 2 (E) = 4 models.

# Case 2: A = False → B unrestricted, C and E unrestricted.
# Models: 2 (B) × 2 (C) × 2 (E) = 8 models.

# Step 3: Compute the total number of valid models.
# Total models = 4 (Case 1) + 8 (Case 2) = 12 models.


# ----------------------------------------------------------
# ############# Question 6 #############
# In propositional logic, using four proposition symbols A, B, C, D,
# how many models are there of the formula C ∨ A ∨ ¬C?
# Or, to put it another way, how many models satisfy C ∨ A ∨ ¬C?

# ############# Answer 6 #############
# 16 models.

# Step 1: Simplify the formula C ∨ A ∨ ¬C.
# - The expression C ∨ ¬C is always true (tautology).
# - The formula then simplifies to (True) ∨ A, which is still always true.

# Step 2: Determine the number of satisfying models.
# - Since the formula does not impose any restrictions, all possible truth assignments
#   for A, B, C, and D satisfy it.
# - Each of the four propositional symbols (A, B, C, D) can be either true or false.
# - The total number of possible models is 2^4 = 16.


# ----------------------------------------------------------
# ############# Question 7 #############
# In propositional logic, using four proposition symbols A, B, C, D,
# how many models are there of the formula A ∧ B ∧ ¬A?
# Or, to put it another way, how many models satisfy A ∧ B ∧ ¬A?

# ############# Answer 7 #############
# 0 models.

# Step 1: Analyze the formula A ∧ B ∧ ¬A.
# - The expression A ∧ ¬A is always false because A cannot be both true and false simultaneously.
# - Since A ∧ ¬A is a contradiction, the entire formula A ∧ B ∧ ¬A is unsatisfiable.

# Step 2: Determine the number of satisfying models.
# - A contradiction means that there are no possible truth assignments that satisfy the formula.
# - Therefore, the number of satisfying models is 0.
