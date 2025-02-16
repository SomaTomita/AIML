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
