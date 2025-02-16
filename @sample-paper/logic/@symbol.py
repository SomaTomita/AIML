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
#    Symbol: ⇒ or ⊢ (depending on context)
#    Meaning: If one statement is true, another logically follows.
#    Example: If it rains, the ground will be wet (P ⇒ Q).
#    Real-Life Analogy:
#        "If you study, you pass the exam."
#    Usage:
rain = True
if rain:  # P
    ground_wet = True  # Q
print(f"If it rains (P), then the ground is wet (Q): {ground_wet}")  # True

# 2. Negation (Logical NOT)
#    Symbol: ¬ or !
#    Meaning: Negates the truth value of a statement.
#    Example: ¬P means "P is not true."
#    Real-Life Analogy:
#        "If the store is NOT open, you can’t buy groceries."
#    Usage:
rain = False  # ¬P
if not rain:
    print("It's not raining.")

# 3. Entailment (Logical Deduction)
#    Symbol: ⊢
#    Meaning: A statement is provable from premises.
#    Example: P₁, P₂ ⊢ Q means "Q is entailed by premises P₁ and P₂."
#    Real-Life Analogy:
#        "If it’s cloudy and raining, you should take an umbrella."
#    Usage:
rain = True  # P₁
cloudy = True  # P₂
if rain and cloudy:  # Premises entail:
    print("Take an umbrella.")  # Q

# 4. Knowledge Base (Collection of Facts)
#    Symbol: KB
#    Meaning: A collection of known facts and rules.
#    Example: KB = {Fact1, Fact2, Rule1, Rule2, ...}
#    Real-Life Analogy:
#        "A recipe book contains all the knowledge needed to cook a dish."
#    Usage:
knowledge_base = {
    "Fact1": "All humans are mortal",
    "Fact2": "Socrates is a human",
    "Rule1": "If X is human, then X is mortal",
}
print(f"Is Socrates mortal? {'Yes' if 'Fact2' in knowledge_base else 'No'}")  # Yes

# 5. Sentence (Logical Statement or Proposition)
#    Symbol: P, Q, R (representing propositions)
#    Meaning: A declarative statement that is either true or false.
#    Example: "It is sunny today."
#    Real-Life Analogy:
#        "The store is open." (It can only be true or false.)
#    Usage:
sunny = True  # P
print(f"The proposition 'It is sunny today' is {sunny}.")

# 6. Logical OR (Disjunction)
#    Symbol: ∨
#    Meaning: True if at least one condition is true.
#    Example: A ∨ B (A OR B).
#    Real-Life Analogy:
#        "You can have tea OR coffee."
#    Usage:
sunny = True  # A
warm = False  # B
if sunny or warm:  # A ∨ B
    print("It's nice weather!")  # This executes because A is true.
else:
    print("It's neither sunny nor warm.")


# 7. Universal Quantifier (For All)
#    Symbol: ∀
#    Meaning: A property holds for all elements in a given set.
#    Example: ∀x (x + 1 > x) means "For every number x, x + 1 is always greater than x."
#    Real-Life Analogy:
#        "All humans need oxygen to breathe." This applies to every person.
#    Usage:
people = ["Alice", "Bob", "Charlie"]
oxygen_needed = all(person for person in people)
print(f"Does everyone need oxygen? {oxygen_needed}")  # True

# 8. Existential Quantifier (There Exists)
#    Symbol: ∃
#    Meaning: There is at least one element in the set that satisfies a condition.
#    Example: ∃x (x > 5) means "There is at least one x greater than 5."
#    Real-Life Analogy:
#        "At least one person in the class got an A."
#    Usage:
scores = [55, 70, 90, 40]
exists_A = any(score > 85 for score in scores)
print(f"Did anyone score an A? {exists_A}")  # True

# 9. Exclusive OR (XOR)
#    Symbol: ⊕
#    Meaning: True if exactly one of the two conditions is true.
#    Example: (True ⊕ False) = True, but (True ⊕ True) = False.
#    Real-Life Analogy:
#        "You can either take the bus or the train, but not both."
#    Usage:
bus_taken = True
train_taken = False
print(f"Can I use XOR logic? {bus_taken != train_taken}")  # True

# 10. Set Membership
#     Symbol: ∈
#     Meaning: Denotes that an element belongs to a set.
#     Example: 3 ∈ {1, 2, 3} is True.
#     Real-Life Analogy:
#        "Is your name on the guest list?"
#     Usage:
guest_list = {"Alice", "Bob", "Charlie"}
person = "Bob"
print(f"Is Bob invited? {person in guest_list}")  # True

# 11. Subset
#     Symbol: ⊆
#     Meaning: A set whose elements are entirely contained within another set.
#     Example: {1, 2} ⊆ {1, 2, 3} is True.
#     Real-Life Analogy:
#        "All dogs are animals, but not all animals are dogs."
#     Usage:
dogs = {"Beagle", "Poodle"}
animals = {"Beagle", "Poodle", "Cat", "Elephant"}
print(f"Are all dogs animals? {dogs.issubset(animals)}")  # True

# 12. Union & Intersection
#     Symbols: ∪ (union), ∩ (intersection)
#     Meaning:
#         A ∪ B: Elements in A or B (or both).
#         A ∩ B: Elements in both A and B.
#     Example:
#         If A = {1, 2}, B = {2, 3},
#         A ∪ B = {1, 2, 3}, A ∩ B = {2}.
#     Real-Life Analogy:
#        "The union of two friend circles includes everyone from both groups."
#        "The intersection of two movie lovers includes those who like both genres."
#     Usage:
A = {1, 2}
B = {2, 3}
print(f"Union: {A | B}, Intersection: {A & B}")  # Union: {1, 2, 3}, Intersection: {2}

# 13. Therefore (Logical Conclusion)
#     Symbol: ∴
#     Meaning: Used to conclude a statement based on premises.
#     Example:
#         P → Q, P is true, ∴ Q is true.
#     Real-Life Analogy:
#        "If you study, you pass the test. You studied, ∴ you passed."
#     Usage:
study = True
if study:
    print("∴ You passed the test.")

# 14. Because (Since)
#     Symbol: ∵
#     Meaning: Indicates reasoning or explanation.
#     Example:
#         ∵ P and Q, ∴ P ∧ Q is true.
#     Real-Life Analogy:
#        "We brought an umbrella ∵ it was raining."
#     Usage:
rain = True
if rain:
    print("∵ It was raining, we brought an umbrella.")

# 15. Logical NOR (NOT OR)
#     Symbol: ↓
#     Meaning: The negation of OR; true only if both operands are false.
#     Example:
#         (False ↓ False) = True
#     Real-Life Analogy:
#        "Neither the light is on nor the fan is running."
#     Usage:
light_on = False
fan_running = False
print(f"Is everything off? {not (light_on or fan_running)}")  # True

# 16. Logical NAND (NOT AND)
#     Symbol: ↑
#     Meaning: The negation of AND; false only if both operands are true.
#     Example:
#         (True ↑ True) = False
#     Real-Life Analogy:
#        "You can't have both cake and ice cream."
#     Usage:
cake = True
ice_cream = True
print(f"Can't have both? {not (cake and ice_cream)}")  # False

# 17. Logical Implication (Alternative Form)
#     Symbol: ⟹
#     Meaning: "If P then Q"; similar to →
#     Example: P ⟹ Q.
#     Real-Life Analogy:
#        "If you press the button, the elevator arrives."
#     Usage:
button_pressed = True
if button_pressed:
    print("⟹ The elevator arrives.")

# 18. Modulus (Remainder after Division)
#     Symbol: ≡ (mod)
#     Meaning: A ≡ B (mod n) means A and B leave the same remainder when divided by n.
#     Example:
#         17 ≡ 5 (mod 6) because both 17 and 5 leave remainder 5 when divided by 6.
#     Real-Life Analogy:
#        "Every 7th day is a weekend (mod 7 cycle)."
#     Usage:
A = 17
B = 5
mod = 6
print(f"Are they congruent mod {mod}? {A % mod == B % mod}")  # True
