############# Question #############

# What is the meaning of this symbol:  ⊢
# Group of answer choices (select one):

# Inference
# Negation
# Entailment
# Knowledge base
# Sentence


############# Answer #############
# The correct answer is: Entailment


# 1. Inference (Logical Reasoning)
# Symbol: ⇒ or ⊢ (depending on context)
# Example: If it rains, the ground will be wet (P ⇒ Q).
# Representation:
# P ⇒ Q means "If P is true, then Q logically follows."
# Example:
rain = True
if rain:  # P
    ground_wet = True  # Q
# Logical reasoning: If "rain" is true, we infer "ground_wet" is true.


# 2. Negation (Logical NOT)
# Symbol: ¬ or !
# Example: It's not raining.
# Representation:
# ¬P means "P is not true."
# Example:
rain = False  # ¬P
if not rain:
    print("It's not raining.")


# 3. Entailment (Logical Deduction)
# Symbol: ⊢
# Example: From the axioms, we can deduce the theorem.
# Representation:
# P₁, P₂ ⊢ Q means "Q is entailed by premises P₁ and P₂."
# Example:
rain = True  # P₁
cloudy = True  # P₂
if rain and cloudy:  # Premises entail:
    print("Take an umbrella.")  # Q


# 4. Knowledge Base (Collection of Facts)
# Symbol: KB
# Example: A database of known facts or rules.
# Representation:
# KB = {Fact1, Fact2, Rule1, Rule2, ...}
# Example:
knowledge_base = {
    "Fact1": "All humans are mortal",
    "Fact2": "Socrates is a human",
    "Rule1": "If X is human, then X is mortal",
}
# Using this knowledge base, we infer:
# Socrates is mortal.


# 5. Sentence (Logical Statement or Proposition)
# Symbol: P, Q, R (representing propositions)
# Example: "It is sunny today."
# Representation: A logical statement is a declarative sentence that is either true or false.
# Example:
sunny = True  # P
print(f"The proposition 'It is sunny today' is {sunny}.")


# 6. Logical OR:
### Table ###
# A,      B,      A ∨ B
# True,   True,   True
# True,   False,  True
# False,  True,   True
# False,  False,  False

# example:
sunny = True  # A
warm = False  # B
# A ∨ B means either sunny OR warm is true (or both).
if sunny or warm:  # A ∨ B
    print("It's nice weather!")  # This executes because A is true.
else:
    print("It's neither sunny nor warm.")
