############# Question #############
# Consider the following logical statement:
# If the main power fails, and the backup generator does not activate, then the data center shuts down.
# Suppose we have the following three proposition symbols:

# P: The main power is functioning.
# G: The backup generator is activated.
# D: The data center is operational.

# Write the logical statement in propositional logic using the three proposition symbols P, G, and D.
# It should be written as a clause in conjunctive normal form.
# Use a minus sign for negation (for example, -X means the negation of X).
# Write disjunction (‘or’) using the letter ‘v’.
# For example, the clause ¬P∨¬G would be written as -Pv-G.


############# Answer #############
"PvGv-D"

# Step 1: Express the given logical statement
#   "If the main power fails AND the backup generator does NOT activate, then the data center shuts down."
#   - "The main power fails" means NOT P (-P)
#   - "The backup generator does NOT activate" means NOT G (-G)
#   - "The data center shuts down" means NOT D (-D)
#
#   The statement translates to: (-P AND -G) → -D

# Step 2: Convert implication (→) to disjunction (OR)
#   - Recall that P → Q is equivalent to ¬P ∨ Q
#   - Here, P = (-P AND -G), and Q = -D
#   - Applying this: ¬(-P AND -G) ∨ -D

# Step 3: Apply De Morgan’s Law
#   - ¬(-P AND -G) = (P OR G)
#   - So, (P OR G) OR ¬D


############# Question1 #############
# Consider the following logical statement:
# If the motion sensor is defective, or the alarm is not triggered when it should be, then the security system fails.
# Suppose we have the following three proposition symbols:

# M: The motion sensor is working.
# A: The alarm is triggered.
# S: The security system is working.

# Write the logical statement in propositional logic using the three proposition symbols M, A, and S.
# It should be written as a clause in conjunctive normal form.
# Use a minus sign for negation (for example, -X means the negation of X).
# Write disjunction (‘or’) using the letter ‘v’.
# For example, the clause ¬M∨¬A would be written as -Mv-A.


############# Answer1 #############
"Mv-S"
"Av-S"

# Step 1: Express the given logical statement
#   "If the motion sensor is defective OR the alarm is NOT triggered when it should be, then the security system fails."
#   - "The motion sensor is defective" means NOT M (-M)
#   - "The alarm is NOT triggered" means NOT A (-A)
#   - "The security system fails" means NOT S (-S)
#
#   The statement translates to: (-M OR -A) → -S

# Step 2: Convert implication (→) to disjunction (OR)
#   - Recall that P → Q is equivalent to ¬P ∨ Q
#   - Here, P = (-M OR -A), and Q = -S
#   - Applying this: ¬(-M OR -A) ∨ -S

# Step 3: Apply De Morgan’s Law
#   - ¬(-M OR -A) = (M AND A)
#   - So, (M AND A) OR ¬S

# Step 4: Write in required CNF format
#   - Since AND must be expressed in CNF form, we distribute OR:
#   - (M AND A) OR -S  → (M v -S) AND (A v -S)
#   - This results in two clauses: Mv-S and Av-S


############# Question2 #############
# Consider the following logical statement:
# If the network is down, and the server is offline, then users cannot access the website.
# Suppose we have the following three proposition symbols:
# N: The network is up.
# S: The server is online.
# U: Users can access the website.

# Write the logical statement in propositional logic using the three proposition symbols N, S, and U.
# It should be written as a clause in conjunctive normal form.
# Use a minus sign for negation (for example, -X means the negation of X).
# Write disjunction (‘or’) using the letter ‘v’.
# For example, the clause ¬N∨¬S would be written as -Nv-S.


############# Answer2 #############
"NvSv-U"

# Step 1: Express the given logical statement
#   "If the network is down AND the server is offline, then users cannot access the website."
#   - "The network is down" means NOT N (-N)
#   - "The server is offline" means NOT S (-S)
#   - "Users cannot access the website" means NOT U (-U)
#
#   The statement translates to: (-N AND -S) → -U

# Step 2: Convert implication (→) to disjunction (OR)
#   - Recall that P → Q is equivalent to ¬P ∨ Q
#   - Here, P = (-N AND -S), and Q = -U
#   - Applying this: ¬(-N AND -S) ∨ -U

# Step 3: Apply De Morgan’s Law
#   - ¬(-N AND -S) = (N OR S)
#   - So, (N OR S) OR ¬U


############# Question3 #############
# Consider the following logical statement:
# If the battery is bad, and the screen is cracked, then the laptop is broken.
# Suppose we have the following three proposition symbols:
# B: The battery is OK.
# S: The screen is cracked.
# L: The laptop is OK.

# Write the logical statement in propositional logic using the three proposition symbols B, S, and L.
# It should be written as a clause in conjunctive normal form.
# Use a minus sign for negation (for example, -A means the negation of A).
# Write disjunction (‘or’) using the letter ‘v’.
# For example, the clause ¬B∨¬S would be written as -Bv-S.


############# Answer3 #############
"Bv-Sv-L"

# 1) Translate "battery is bad" using B:
#    Since B means "the battery is OK," "the battery is bad" means "NOT B" (written as -B).
#
# 2) Translate "the screen is cracked" using S:
#    S already means "the screen is cracked," so we just use S.
#
# 3) Translate "the laptop is broken" using L:
#    Since L means "the laptop is OK," "the laptop is broken" means "NOT L" (written as -L).
#
# So the full logical statement is:
#   "If (NOT B) AND S, then NOT L."
#   which we can write as:  =====  (-B AND S) → -L  =====
#   That is: “If (battery is bad AND screen is cracked), then (laptop is broken).”
#
# 4) Recall that an implication P → Q is logically equivalent to:
#       NOT(P) OR Q
#    Here, P is ( -B AND S ) and Q is ( -L ).
#
# 5) "NOT( -B AND S )" can be expanded using De Morgan's law:
#       NOT( -B AND S ) = ( NOT(-B) ) OR ( NOT(S) )
#       but NOT(-B) means just B (since -B was "battery is bad").
#       and NOT(S) means -S (since S was "screen is cracked").
#
#    So, NOT( -B AND S ) = B OR -S
#
# 6) That gives us:
#       ( B OR -S ) OR -L
#    which we can write more simply as:
#       B v -S v -L
#
# 7) This final expression "Bv-Sv-L" is a single clause in Conjunctive Normal Form (CNF).


# ############# Question4 #############
# Consider the following logical statement:
# If the battery is OK, and the screen is not cracked, then the phone works.
# Suppose we have the following three proposition symbols:

# B: The battery is OK.
# S: The screen is cracked.
# W: The phone works.

# Write the logical statement in propositional logic using the three proposition symbols B, S, and W.
# It should be written as a clause in conjunctive normal form.
# Use a minus sign for negation (for example, -X means the negation of X).
# Write disjunction (‘or’) using the letter ‘v’.
# For example, the clause ¬B∨¬S would be written as -Bv-S.


# ############# Answer4 #############
"-BvSvW"

# Explanation:
# Step 1: Translate the given statement into logical form:
#   "If the battery is OK AND the screen is NOT cracked, then the phone works."
#   - "The battery is OK" -> B
#   - "The screen is NOT cracked" -> NOT S (-S)
#   - "The phone works" -> W
#   So the statement is: (B AND -S) -> W
#
# Step 2: Recall that an implication P -> Q can be rewritten as ¬P ∨ Q.
#   Here, P is (B AND -S), and Q is (W).
#   So we get: ¬(B AND -S) ∨ W
#
# Step 3: Apply De Morgan’s Law to ¬(B AND -S):
#   ¬(B AND -S) = (¬B OR S)
#   Therefore, the whole expression becomes: (¬B OR S) OR W
#   Which simplifies to: -BvSvW


""
############# De Morgan's Laws #############
# De Morgan's Laws state:
#   NOT (A AND B)  is equivalent to  (NOT A) OR (NOT B)
#   NOT (A OR B)   is equivalent to  (NOT A) AND (NOT B)

# Example 1: Applying De Morgan’s Law to an AND operation
A = True
B = False
# Original expression: NOT (A AND B)
original = not (A and B)
# Equivalent using De Morgan's Law: (NOT A) OR (NOT B)
demorgan_version = (not A) or (not B)
print(original == demorgan_version)  # True → Both expressions are equivalent
# -----------------------------------------------

# Example 2: Applying De Morgan’s Law to an OR operation
A = False
B = True
# Original expression: NOT (A OR B)
original = not (A or B)
# Equivalent using De Morgan's Law: (NOT A) AND (NOT B)
demorgan_version = (not A) and (not B)
print(original == demorgan_version)  # True → Both expressions are equivalent
# -----------------------------------------------

# Example 3: Using variables to demonstrate De Morgan's Laws in logic
A = True
B = True
C = False
# De Morgan's Law applied to a complex expression
# NOT (A AND (B OR C)) is equivalent to (NOT A) OR ( (NOT B) AND (NOT C) )
original = not (A and (B or C))
demorgan_version = (not A) or ((not B) and (not C))
print(original == demorgan_version)  # True → Equivalent by De Morgan’s Law
# -----------------------------------------------

# Example 4: De Morgan's Laws in conditional statements
A = False
B = False
# Instead of using NOT (A AND B), you can rewrite it using De Morgan’s Law
if not (A and B):  # Standard form
    print("Condition met using original expression.")
if (not A) or (not B):  # Equivalent using De Morgan's Law
    print("Condition met using De Morgan’s transformation.")
# -----------------------------------------------

# Example 5: Demonstrating De Morgan’s Law with lists
items = ["apple", "banana", "grape"]
# Original: Check if neither "orange" nor "melon" is in the list
original = not ("orange" in items or "melon" in items)
# Equivalent using De Morgan’s Law
demorgan_version = ("orange" not in items) and ("melon" not in items)
print(original == demorgan_version)  # True → They give the same result
# -----------------------------------------------


############# Logical Equivalence #############
# <Example>
# Original Statement (Implication)
# "If you study, then you will pass the exam."

# Logical Representation
# S: You study.
# P: You pass the exam.
# S→P

# After Conversion to Disjunction (OR)
# ¬S∨P

# Explanation:
# "Either you don’t study, or you pass the exam."


# <Example>
# Statement:
# "If it rains, then the ground is wet."

# Logical Representation:
# R: It is raining.
# W: The ground is wet.

# Conversion:
# R → W   →   ¬R v W

# Explanation:
# "If it doesn't rain (¬R), or the ground is wet (W), the statement holds."


# <Example>
# Original
# ¬X → Y

# After Conversion
# X v Y

# Explanation:
# "If NOT X implies Y, then either X is true or Y is true."
