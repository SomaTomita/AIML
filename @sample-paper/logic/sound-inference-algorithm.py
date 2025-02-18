############# Question1 #############
# Suppose we have two sentences S₁, S₂ in propositional logic, and suppose S₁ ⊨ S₂ and S₂ ⊨ S₁.
# Which of the following statements are true?

# 1. A sound inference algorithm will infer S₁ from S₂.
# 2. A sound inference algorithm may infer S₁ from S₂.
# 3. A sound inference algorithm will not infer S₁ from S₂.
# 4. A sound inference algorithm will infer S₂ from S₁.
# 5. A sound inference algorithm may infer S₂ from S₁.
# 6. A sound inference algorithm will not infer S₂ from S₁.

# Select the correct answer from the given options.
# - 2 and 5
# - Only 6
# - 3 and 5
# - 2 and 4
# - 3 and 4
# - Only 4
# - 1 and 6
# - 2 and 6
# - 1 and 5
# - Only 2
# - 1 and 4
# - 3 and 6
# - Only 3
# - Only 1
# - Only 5

############# Answer1 #############
"2 and 5"

# - Given that S₁ ⊨ S₂ and S₂ ⊨ S₁, it means S₁ and S₂ are logically equivalent.
# - A sound inference algorithm guarantees correctness but does not necessarily guarantee that it will always derive every correct inference.
# - "Will infer" (statements 1 and 4) is too strong since soundness does not imply completeness.
# - "May infer" (statements 2 and 5) is correct because a sound algorithm is allowed to make these inferences, but it is not required.
# - "Will not infer" (statements 3 and 6) is incorrect because inference is logically possible.

# Example:
# - Let S₁ represent "It is raining heavily."
# - Let S₂ represent "The ground is wet due to rain."
#
# Logical relationships:
# - S₁ ⊨ S₂ (If it is raining heavily, then the ground is wet due to rain.)
# - S₂ ⊨ S₁ (If the ground is wet due to rain, then it is raining heavily.)
# - These statements imply that S₁ and S₂ are logically equivalent (S₁ ⇔ S₂).
#
# Why "may infer" instead of "will infer"?
# - A sound inference algorithm "may infer" because it only guarantees that if it makes an inference, it will be correct.
# - However, it does NOT guarantee that it will always find and make every possible correct inference.
# - This is different from a complete inference system, which ensures all valid conclusions are always drawn.
# - Example: The system might know "It is raining heavily" but fail to explicitly conclude "The ground is wet."
# - Since inference is possible but not guaranteed, we say "may infer" instead of "will infer."


############# Question2 #############
# Suppose we have three sentences A, B, and C in propositional logic, and suppose A ⊨ B and B ⊨ C.
# Which of the following statements are true?

# 1. A sound inference algorithm will infer C from A.
# 2. A sound inference algorithm may infer C from A.
# 3. A sound inference algorithm will not infer C from A.
# 4. A sound inference algorithm will infer B from C.
# 5. A sound inference algorithm may infer B from C.
# 6. A sound inference algorithm will not infer B from C.

# Select the correct answer from the given options.
# - 1 and 5
# - Only 6
# - 2 and 4
# - 2 and 5
# - 3 and 4
# - Only 4
# - 1 and 6
# - 2 and 6
# - 1 and 5
# - Only 2
# - 1 and 4
# - 3 and 6
# - Only 3
# - Only 1
# - Only 5

############# Answer2 #############
"1 and 5"

# - Given that A ⊨ B and B ⊨ C, by transitivity of entailment, A ⊨ C.
# - A sound inference algorithm should be able to infer C from A (Statement 1 is true).
# - A sound inference algorithm may infer B from C, but it is not required (Statement 5 is true).
# - Statement 3 and 6 are incorrect because C is logically entailed by A and B is not necessarily entailed by C.
# Therefore, the correct statements are 1 and 5.


# ex 1 - transitivity)
# Traffic Light System:
# - Let A represent "The traffic light is red."
# - Let B represent "Cars must stop."
# - Let C represent "Pedestrians can cross."

# Logical relationships:
# - A ⊨ B (If the light is red, then cars must stop.)
# - B ⊨ C (If cars must stop, then pedestrians can cross.)
# By transitivity:
# - A ⊨ C (If the light is red, then pedestrians can cross.)

# ex 2 - sound inference)
# B ⊨ C (B may entail C)
#    - The phrase "cars must stop" (B) does not always mean "pedestrians can cross" (C) in a general sense.
#    - There could be other conditions affecting C:
#      - For example, there might be a separate pedestrian signal that also needs to be green.
#      - There could be an emergency vehicle overriding normal traffic rules.
#    - While B ⊨ C is generally true in typical cases, it is not universally true in all circumstances.


############# Question3 #############
# Suppose we have two sentences X, Y in propositional logic, and suppose X ⊨ Y but Y ⊭ X.
# Which of the following statements are true?

# 1. A sound inference algorithm will infer X from Y.
# 2. A sound inference algorithm may infer X from Y.
# 3. A sound inference algorithm will not infer X from Y.
# 4. A sound inference algorithm will infer Y from X.
# 5. A sound inference algorithm may infer Y from X.
# 6. A sound inference algorithm will not infer Y from X.

# Select the correct answer from the given options.
# - 2 and 5
# - Only 6
# - 3 and 5
# - 2 and 4
# - 3 and 4
# - Only 4
# - 1 and 6
# - 2 and 6
# - 1 and 5
# - Only 2
# - 1 and 4
# - 3 and 6
# - Only 3
# - Only 1
# - Only 5

############# Answer3 #############
"3 and 4"

# - Since X ⊨ Y but Y ⊭ X, Y follows from X, but X does not necessarily follow from Y.
# - A sound inference algorithm will not infer X from Y because Y does not entail X (Statement 3 is true).
# - A sound inference algorithm will infer Y from X because X ⊨ Y (Statement 4 is true).
# - Statements 1 and 2 are incorrect because X is not always guaranteed by Y.
# - Statements 5 and 6 are incorrect because Y is already entailed by X.

# Example:
# - Let X represent "It is snowing."
# - Let Y represent "The temperature is below freezing."

# Logical relationships:
# - X ⊨ Y (If it is snowing, then the temperature must be below freezing.)
# - Y ⊭ X (If the temperature is below freezing, it does not necessarily mean that it is snowing.)


############# Question4 #############
# Suppose we have two sentences P, Q in propositional logic, and suppose P ⊨ Q but Q ⊭ P.
# Which of the following statements are true?

# 1. A sound inference algorithm will infer Q from P.
# 2. A sound inference algorithm may infer Q from P.
# 3. A sound inference algorithm will not infer Q from P.
# 4. A sound inference algorithm will infer P from Q.
# 5. A sound inference algorithm may infer P from Q.
# 6. A sound inference algorithm will not infer P from Q.

# Select the correct answer from the given options.
# - 1 and 5
# - Only 6
# - 2 and 4
# - 1 and 6
# - 3 and 5
# - Only 4
# - 1 and 6
# - 2 and 6
# - 1 and 5
# - Only 2
# - 1 and 4
# - 3 and 6
# - Only 3
# - Only 1
# - Only 5

############# Answer4 #############
"1 and 6"

# - Given P ⊨ Q but Q ⊭ P, we know that Q is a logical consequence of P, but not the other way around.
# - A sound inference algorithm will infer Q from P (Statement 1 is true).
# - A sound inference algorithm will not infer P from Q since Q does not entail P (Statement 6 is true).
# - Statement 3 is false because Q is always guaranteed from P.
# - Statement 5 is incorrect because "may infer" is misleading when entailment does not exist.

# Example:
# - Let P represent "A person is running."
# - Let Q represent "The person is moving."

# Logical relationships:
# - P ⊨ Q (If a person is running, then they are definitely moving.)
# - Q ⊭ P (If a person is moving, they might be walking, not necessarily running.)
