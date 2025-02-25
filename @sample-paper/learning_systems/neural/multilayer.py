############# Question #############
# When using a multilayer neural network to predict the probability that an example belongs to a class, which activation function would be suitable for the final layer of the neural network?
# Group of answer choices

# - The hard threshold function.
# - The logistic function.
# - The rectifier function.

############# Answer #############
"The logistic function"

# The logistic function (also known as the sigmoid function) is the most suitable activation function
# for the final layer when predicting the probability that an example belongs to a class in a binary classification problem.

# Explanation:

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
