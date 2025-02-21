############# Question #############

# A logistic regression function is equivalent to which type of neuron?
# Group of answer choices

# - A neuron that combines a rectifier function with a logistic function.
# - A neuron with the logistic function as its activation function.
# - A neuron with the rectifier function as its activation function.
# - A neuron with the hard threshold function as its activation function.
# - A neuron with the softplus function as its activation function.


############# Answer #############
"a neuron with the logistic function as its activation function."


# -  Logistic regression is a mechanism that adds inputs (data) together, adjusts the slope (weighting), and outputs the sum of the inputs in the range of 0 to 1
# - The sigmoid function (logistic function) is an S-shaped curved function that approaches 1 as the value increases and approaches 0 as the value decreases.
# - When a neuron (artificial nerve) is using a sigmoid function, the output of that neuron has the same formula as logistic regression.
# - In other words, we can understand that "logistic regression is a single neuron with sigmoid activation itself.

# ############# Detailed Explanation #############
# 1. Logistic Regression Recap:
#    Logistic regression takes inputs (x), computes a weighted sum (wᵀx + b),
#    and then applies the logistic (sigmoid) function:
#       σ(z) = 1 / (1 + e^(-z)).
#
# 2. Neuron with Logistic Activation:
#    In neural networks, a neuron often does:
#       a = φ(wᵀx + b).
#    If φ is the logistic (sigmoid) function, it matches exactly how logistic
#    regression computes its output.
#
# 3. Other Activations (Comparison):
#    - ReLU (Rectifier): max(0,z) -> Not equivalent to logistic.
#    - Hard Threshold: Step at z=0 -> Not equivalent to logistic.
#    - Softplus: log(1 + e^z) -> Different from logistic.
#
# 4. Analogy:
#    Logistic activation acts like a "smooth switch," gradually changing
#    the output from 0 to 1 rather than snapping it at a particular threshold.


############# Question #############

# The mathematical model of a neuron has two parts. Name the two parts.
# Group of answer choices

# An arbitrary non-linear function and an activation function.
# A rectifier function and a hard threshold function.
# An arbitrary non-linear function and a logistic function.
# A linear function and an activation function.
# A linear function and a logistic function.
# An arbitrary non-linear function and a hard threshold function.

############# Answer #############
"A linear function and an activation functions"

# Correct Answer: "A Linear Function and an Activation Function"

# (a) Linear Function (Weighted Sum)
# - This is the first step in the neuron model.
# - It calculates a weighted sum of input features plus a bias.
# - Mathematically, it is represented as:
#   z = sum(w_i * x_i) + b
#   where:
#     - x_i are the input values (features),
#     - w_i are the corresponding weights,
#     - b is the bias term.
# - This operation is linear and does not introduce non-linearity.

# (b) Activation Function
# - After computing the linear function, the neuron applies an activation function
#   to introduce non-linearity.
# - Activation functions help the network learn complex patterns beyond simple linear relationships.
# - Common activation functions include:
#   - ReLU (Rectified Linear Unit): f(z) = max(0, z)
#   - Sigmoid (Logistic Function): f(z) = 1 / (1 + exp(-z))
#   - Tanh (Hyperbolic Tangent): f(z) = (exp(z) - exp(-z)) / (exp(z) + exp(-z))
#   - Softmax (for multi-class classification): f(z_i) = exp(z_i) / sum(exp(z_j))
# - This combination of a linear function followed by a non-linear activation function
#   allows neural networks to model complex functions.


# Incorrect Options and Explanations:
# 1. "An Arbitrary Non-Linear Function and an Activation Function" ❌
# - The first step in a neuron is always a linear function, not an arbitrary non-linear function.
# - The activation function introduces non-linearity, but the weighted sum (first step) is always linear.

# 2. "A Rectifier Function and a Hard Threshold Function" ❌
# - A rectifier function (like ReLU) is an activation function, not a part of the first step (linear function).
# - A hard threshold function is a step activation function (e.g., Heaviside step function).
# - The neuron model needs a linear function first, not just two activation functions.
# - Example of a hard threshold function:
#   f(z) =
#     1, if z > 0
#     0, if z ≤ 0
# - This function was used in early perceptrons but is too rigid for modern neural networks.

# 3. "An Arbitrary Non-Linear Function and a Logistic Function" ❌
# - Again, the first part should be a linear function (not an arbitrary non-linear function).
# - The logistic function (sigmoid) is a type of activation function, but not all neurons use it.
# - Example of a sigmoid function:
#   f(z) = 1 / (1 + exp(-z))
# - While the logistic function is useful (especially in binary classification),
#   it is just one type of activation function.

# 4. "A Linear Function and a Logistic Function" ❌
# - The logistic function (sigmoid) is an activation function, but neurons can use other activation functions too.
# - The correct answer should refer to activation functions in general, not just a single function.

# 5. "An Arbitrary Non-Linear Function and a Hard Threshold Function" ❌
# - The first step in a neuron should be a linear function, not an arbitrary non-linear function.
# - The hard threshold function is just one type of activation function, and modern neural networks use more flexible activations.
