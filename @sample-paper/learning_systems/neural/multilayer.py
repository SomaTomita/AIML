############# Question #############
# When using a multilayer neural network to predict the probability that an example belongs to a class, which activation function would be suitable for the final layer of the neural network?
# Group of answer choices

# - The hard threshold function.
# - The logistic function.
# - The rectifier function.

############# Answer #############
"The logistic function"

# The logistic function (also known as the sigmoid function) is the most suitable activation function for the final layer when predicting the probability that an example belongs to a class in a binary classification problem.


# 1. Logistic Function (Sigmoid)
#    - Formula:
#      σ(x) = 1 / (1 + e^(-x))
#    - Output Range: (0,1), which makes it ideal for probability estimation.
#    - It converts the raw scores (logits) into a probability distribution.
#    - In a binary classification setting, the model typically outputs a single value,
#      which represents the probability of belonging to class 1. The probability of class 0 is simply 1 - P(class1).
#    - Used with the binary cross-entropy loss function.

# 2. Hard Threshold Function
#    - Produces discrete outputs (0 or 1).
#    - Not differentiable, making it unsuitable for backpropagation-based learning in neural networks.

# 3. Rectifier Function (ReLU)
#    - Formula:
#      f(x) = max(0, x)
#    - Commonly used in hidden layers, but not suitable for the output layer in probability estimation.
#    - Outputs range from 0 to +∞, making it unsuitable for probability prediction.


# ------------------------------------------------------------------------------
############# Question 1 #############
# In a deep neural network, which activation function is most commonly used in hidden layers to mitigate the vanishing gradient problem?
# Group of answer choices

# - The sigmoid function.
# - The tanh function.
# - The ReLU function.

############# Answer 1 #############
"The ReLU function"

# ReLU (Rectified Linear Unit) is the most commonly used activation function in hidden layers of deep neural networks because it helps mitigate the vanishing gradient problem.

# 1. ReLU Function
#    - Formula:
#      f(x) = max(0, x)
#    - Output Range: (0, ∞) for positive inputs, 0 for negative inputs.
#    - Helps prevent the vanishing gradient problem by allowing gradients to propagate effectively.
#      (It is a derivative of the error function (loss function) with a parameter, but intuitively it can be thought of as an indicator of “how wrong the neural net is and how much adjustment is needed to correct it.)
#    - Efficient computation, reducing training time in deep networks.
#      (just compare with 0)
#    - However, it suffers from the "dying ReLU" problem, where neurons can get stuck at 0. (If the input is a negative value,)

# 2. Sigmoid Function
#    - Formula:
#      σ(x) = 1 / (1 + e^(-x))
#    - Outputs values in (0,1), but suffers from the vanishing gradient problem.
#      (As the error is propagated to the back (input) layer, the gradient becomes smaller and smaller, until it is almost zero.  This causes the weights to not be updated and learning does not progress.)
#    - Used in output layers for binary classification, but not ideal for deep hidden layers.

# 3. Tanh Function
#    - Formula:
#      tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))
#    - Output Range: (-1,1), centering data around 0, which can help in training.
#    - Still suffers from the vanishing gradient problem, making it less preferable to ReLU in deep networks.


# ------------------------------------------------------------------------------
############# Question 2 #############
# A neural network model trained for a medical diagnosis system provides a probability score for each of five possible diseases (where one and only one disease must be assigned per patient).
# Which of the following activation functions should be used in the output layer for the best probability interpretation?
# Group of answer choices

# - The softmax function.
# - The sigmoid function.
# - The linear function.

############# Answer 2 #############
"The softmax function"

# The softmax function is the best choice because it normalizes the output into a probability distribution
# where the sum of all class probabilities equals 1, making it suitable for mutually exclusive classes.

# 1. Softmax Function
#    - Formula:
#      softmax(x_i) = exp(x_i) / sum(exp(x_j)) for all j
#    - Ensures the sum of outputs across all five diseases is 1, providing a clear probabilistic interpretation.
#    - Allows the model to confidently assign a diagnosis to the most probable disease.
#    - Used with categorical cross-entropy loss.

# 2. Sigmoid Function
#    - Formula:
#      σ(x) = 1 / (1 + e^(-x))
#    - Outputs independent probabilities for each class (not normalized).
#    - Suitable for multi-label classification where multiple diseases could be present at once,
#      but NOT ideal for mutually exclusive cases.

# 3. Linear Function
#    - Outputs unbounded real numbers, which do not represent probabilities.
#    - Used in regression problems, not classification.


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# The Softmax Function
# "Scaling each output with an exponential function and normalizing so that the sum of all class outputs equals 1"

# Why do we use the exponential function (exp)?
# "To emphasize larger values while making smaller values relatively smaller!"

# Before applying Softmax, we have scores for each class (called logits).
# For example, suppose we have three classes: "Cat," "Dog," and "Bird,"
# and their respective scores are as follows:

"Cat: 2.0"
"Dog: 0.5"
"Bird: -1.0"

# It's difficult to directly interpret these as probabilities.
# → By applying the exponential function (exp), the differences in scores become more pronounced.

"exp(2.0) = 7.39"
"exp(0.5) = 1.65"
"exp(-1.0) = 0.37"
# This process highlights the differences in scores, making it easier to determine "winners and losers."

# Why does the sum become 1?
# "To ensure the values can be interpreted as probabilities!"

# If we leave the scores as they are, their sum is arbitrary, meaning they can't be treated as probabilities.
# To fix this, we divide each value by the total sum of all exponentiated values, ensuring the sum equals 1.

# softmax(Cat) = exp(2.0) / (exp(2.0) + exp(0.5) + exp(-1.0))
#              ≈ 7.39 / (7.39 + 1.65 + 0.37)
#              ≈ 7.39 / 9.41
#              ≈ 0.79 (79%)

# softmax(Dog) ≈ 1.65 / 9.41 ≈ 0.18 (18%)

# softmax(Bird) ≈ 0.37 / 9.41 ≈ 0.04 (4%)
