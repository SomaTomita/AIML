############# Question #############

# In the data set below there are four examples with two attributes (x and y), and each example is labelled 0 or 1.
# Dataset:
# x,	y,	Label
# 1,	1,	0
# 1,	2,	0
# 2,	1,	0
# 2,	2,	1

# Professor Fuzzbrain wants to predict the label from x and y using a single neuron with a hard threshold activation function.
# He has made four attempts at this task, and they are shown in hypotheses A to D below.
# In each case, threshold represents the hard threshold function that returns 0 for negative inputs and 1 for positive inputs.
# For each hypothesis, work out whether it correctly predicts the label for all four of the examples.
# If it does, enter ‘y’ into the box, otherwise enter ‘n’.


############# Answer #############
# A. f(x,y) = threshold(x + y – 4.5):
"n"
# B. f(x,y) = threshold(x + y – 3.5):
"y"
# C. f(x,y) = threshold(-x -y + 3.5):
"n"
# D. f(x,y) = threshold(x + y – 2.5):
"n"


# ------------------------------------------------------------------------------
# Detailed Explanation (commented)
# ------------------------------------------------------------------------------
# The hard threshold function returns 0 for negative inputs and 1 for positive inputs.
# (Note: We assume the threshold function outputs 1 for inputs > 0 and 0 for inputs < 0.
#  Since none of the computed values are exactly 0, this ambiguity does not affect our results.)


# We will evaluate each hypothesis:
# Hypothesis A: f(x,y) = threshold(x + y – 4.5)
# ------------------------------------------------
# For each example:
#   Example 1: (1, 1) -> 1 + 1 - 4.5 = -2.5, threshold(-2.5) = 0, expected label = 0. (Correct)
#   Example 2: (1, 2) -> 1 + 2 - 4.5 = -1.5, threshold(-1.5) = 0, expected label = 0. (Correct)
#   Example 3: (2, 1) -> 2 + 1 - 4.5 = -1.5, threshold(-1.5) = 0, expected label = 0. (Correct)
#   Example 4: (2, 2) -> 2 + 2 - 4.5 = -0.5, threshold(-0.5) = 0, expected label = 1. (Incorrect)
#
# Conclusion for A: Does NOT correctly predict all examples.
# Answer = 'n'


# Hypothesis B: f(x,y) = threshold(x + y – 3.5)
# ------------------------------------------------
# For each example:
#   Example 1: (1, 1) -> 1 + 1 - 3.5 = -1.5, threshold(-1.5) = 0, expected label = 0. (Correct)
#   Example 2: (1, 2) -> 1 + 2 - 3.5 = -0.5, threshold(-0.5) = 0, expected label = 0. (Correct)
#   Example 3: (2, 1) -> 2 + 1 - 3.5 = -0.5, threshold(-0.5) = 0, expected label = 0. (Correct)
#   Example 4: (2, 2) -> 2 + 2 - 3.5 = 0.5, threshold(0.5) = 1, expected label = 1. (Correct)
#
# Conclusion for B: Correctly predicts all examples.
# Answer = 'y'


# Hypothesis C: f(x,y) = threshold(-x - y + 3.5)
# ------------------------------------------------
# For each example:
#   Example 1: (1, 1) -> -1 - 1 + 3.5 = 1.5, threshold(1.5) = 1, expected label = 0. (Incorrect)
#
# Since Example 1 is already incorrect, we do not need to evaluate further.
#
# Conclusion for C: Does NOT correctly predict all examples.
# Answer = 'n'


# Hypothesis D: f(x,y) = threshold(x + y – 2.5)
# ------------------------------------------------
# For each example:
#   Example 1: (1, 1) -> 1 + 1 - 2.5 = -0.5, threshold(-0.5) = 0, expected label = 0. (Correct)
#   Example 2: (1, 2) -> 1 + 2 - 2.5 = 0.5, threshold(0.5) = 1, expected label = 0. (Incorrect)
#
# Conclusion for D: Does NOT correctly predict all examples.
# Answer = 'n'
