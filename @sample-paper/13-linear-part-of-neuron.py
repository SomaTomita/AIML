############# Question #############

# Suppose the linear part of a neuron produces the value -3.
# For each of three activation functions (hard threshold, logistic, rectifier), what is the output of the neuron?
# The answers are for the three activation functions (hard threshold, logistic, rectifier) in that order, and are rounded to the nearest integer.
# Group of answer choices

# 0, 0, 0.
# 1, 1, 1.
# 0, 1, 0.
# 1, 0, 1.
# 0, 0, 1.
# 1, 1, 0.
# 1, 0, 0.

############# Answer #############
"0, 0, 0"

# ------------------------------------------------------------------------------
# 1. Hard Threshold Function:
#    - If the input is greater than 0, output is 1; otherwise 0.
#    - Since -3 < 0, output = 0.

# 2. Logistic (Sigmoid) Function:
#    - σ(x) = 1 / (1 + e^(-x))
#    - σ(-3) = 1 / (1 + e^3)
#    - e^3 ≈ 20.0855, so:
#      σ(-3) = 1 / (1 + 20.0855) ≈ 0.0474
#    - Rounded to the nearest integer → 0.

# 3. Rectifier (ReLU) Function:
#    - ReLU(x) = max(0, x)
#    - ReLU(-3) = max(0, -3) = 0.

# Correct Answer: **0, 0, 0.**
# ------------------------------------------------------------------------------


############# Question1 #############

# Suppose the linear part of a neuron produces the value 6.
# For each of three activation functions (hard threshold, logistic, rectifier), what is the output of the neuron?
# The answers are for the three activation functions (hard threshold, logistic, rectifier) in that order, and are rounded to the nearest integer.
# Group of answer choices

# 6, 6, 1.
# 1, 6, 1.
# 0, 1, 1.
# 1, 0, 1.
# 1, 1, 6.
# 0, 1, 6.
# 1, 1, 1.


############# Answer1 #############
"1, 1, 6"


# ------------------------------------------------------------------------------
# Detailed Explanation (commented)
# ------------------------------------------------------------------------------
# We are given a neuron with a linear output of 6 and need to apply three

# 1. Hard Threshold (Step) Function:
#    - Definition:
#        f(x) =
#        { 1, if x ≥ 0
#        { 0, if x < 0
#    - If the input is greater than 0, output 1; otherwise, output 0.
#    - Since our input is 6 (which is greater than 0), the output is:
hard_threshold_output = 1

# 2. Logistic (Sigmoid) Function:
#    - Definition:
#        σ(x) = 1 / (1 + e^(-x))
#    - Applying x = 6:
#        σ(6) = 1 / (1 + e^(-6))
#    - Calculating step-by-step:
#        e^(-6) ≈ 0.00247875
#        1 + e^(-6) ≈ 1.00247875
#        1 / 1.00247875 ≈ 0.9975
#    - Rounding to the nearest integer:
sigmoid_output = round(0.9975)  # Result is 1

# 3. Rectifier Function (ReLU):
#    - Definition:
#        ReLU(x) = max(0, x)
#    - Applying x = 6:
#        ReLU(6) = max(0, 6) = 6
relu_output = 6

# The outputs for Hard Threshold, Logistic (Sigmoid), and ReLU are:
# 1, 1, 6
