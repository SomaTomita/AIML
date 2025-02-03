# ------------------------------------------------------------------------------
# 1. Softmax Function - Mathematical Explanation and Python Implementation
# ------------------------------------------------------------------------------
# - The softmax function is used in the final layer of a neural network for classification.
# - It converts raw scores (logits) into probabilities that sum up to 1.
# - Formula:
#   Softmax(z_i) = exp(z_i) / sum(exp(z_j)) for all j
# - This ensures that the output represents a valid probability distribution.

# - Each raw score is exponentiated to make it positive.
# - Then, the sum of all exponentiated values is computed.
# - Each exponentiated value is divided by the sum, producing probabilities.
# - The highest value gets the largest probability, but all values contribute.
# - The subtraction of np.max(logits) improves numerical stability.


import numpy as np


def softmax(logits):
    exp_values = np.exp(
        logits - np.max(logits)
    )  # Subtracting max for numerical stability
    return exp_values / np.sum(exp_values)


# Example logits (raw scores from a neural network)
logits = np.array([2.0, 1.0, 0.1])

# Compute softmax probabilities
softmax_probs = softmax(logits)

print("Softmax Output:", softmax_probs)
print("Sum of probabilities:", np.sum(softmax_probs))  # Should sum to 1


# ------------------------------------------------------------------------------
# 2. Cross-Entropy Loss - Mathematical Explanation and Python Implementation
# ------------------------------------------------------------------------------
# - Cross-entropy loss measures the difference between predicted and actual distributions.
# - It is commonly used in classification tasks.
# - Formula:
#   CrossEntropyLoss = - sum(y_true * log(y_pred))
# - If y_true is a one-hot vector, only the term corresponding to the correct class contributes.

# - The true class label (y_true) is one-hot encoded (e.g., [1, 0, 0] for class 0).
# - The predicted probabilities (y_pred) are from the softmax function.
# - We take the logarithm of y_pred and multiply by y_true to extract the correct class probability.
# - The sum is taken, and the result is negated to give the loss value.
# - This encourages the model to maximize the probability of the correct class.


def cross_entropy_loss(y_true, y_pred):
    return -np.sum(
        y_true * np.log(y_pred + 1e-9)
    )  # Adding small value for numerical stability


# Example: Assume correct class is index 0 (one-hot encoded)
y_true = np.array([1, 0, 0])  # True class is the first category
y_pred = softmax_probs  # Predicted probabilities from softmax

# Compute cross-entropy loss
loss = cross_entropy_loss(y_true, y_pred)

print("Cross-Entropy Loss:", loss)


# ------------------------------------------------------------------------------
# 3. Softmax and Cross-Entropy Combined (Logits to Loss)
# ------------------------------------------------------------------------------
# - In deep learning frameworks, softmax and cross-entropy are combined for efficiency.
# - Instead of computing softmax first, we directly use raw logits in cross-entropy loss.
# - This avoids numerical instability issues when working with very small probabilities.

# - Instead of applying softmax separately, TensorFlow computes cross-entropy on raw logits.
# - This improves numerical stability by avoiding extremely small values from softmax.
# - The function `softmax_cross_entropy_with_logits` automatically handles both steps.
# - It directly computes the negative log probability for the correct class.

import tensorflow as tf

# Convert logits and labels to tensors
logits_tf = tf.constant([[2.0, 1.0, 0.1]])  # Raw model outputs
y_true_tf = tf.constant([[1.0, 0.0, 0.0]])  # True labels (one-hot encoded)

# Compute softmax cross-entropy loss using TensorFlow
loss_tf = tf.nn.softmax_cross_entropy_with_logits(labels=y_true_tf, logits=logits_tf)

print("Softmax Cross-Entropy Loss (TensorFlow):", loss_tf.numpy())
