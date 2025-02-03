import numpy as np
import matplotlib.pyplot as plt

# Loss Function Explanation:
# A loss function measures how well a machine learning model's predictions match the actual target values.
# The goal of training is to minimize this loss function, making the model as accurate as possible.
# Different types of loss functions are used based on the type of problem (classification, regression, etc.).

# Binary Cross-Entropy Loss (Log Loss):
# When using the sigmoid function, binary cross-entropy is commonly used as the loss function.
# The formula is:
# Loss = - (y * log(y^) + (1 - y) * log(1 - y^))
# where:
# - y is the actual target (0 or 1)
# - y^ is the predicted probability (output of sigmoid function)


def binary_cross_entropy(y_true, y_pred):
    return -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


# Example scenario:
# Let's assume we have a sigmoid output of 0.7, and the true label is 1.
y_pred = 0.7  # Predicted probability
y_true = 1  # Actual label
loss = binary_cross_entropy(y_true, y_pred)
# It indicates the penalty (loss) associated with predicting 0.7 instead of 1.
print(f"Binary Cross-Entropy Loss: {loss:.4f}")


# Explanation of Weight Impact:
# When the same input is passed to different neurons, adjusting one weight (w) too much can create an imbalance.
# If one neuron’s weight becomes very large, it can dominate the output and negatively impact other neurons.
# This makes training difficult because gradient updates affect the entire network.

# Generate a range of predicted values (y_pred) to visualize the loss function
y_pred_values = np.linspace(
    0.01, 0.99, 100
)  # Avoiding 0 and 1 to prevent log(0) issues
loss_values = [binary_cross_entropy(1, y) for y in y_pred_values]


# Plot the loss function
plt.figure(figsize=(8, 6))
plt.plot(y_pred_values, loss_values, label="Binary Cross-Entropy Loss", color="red")
plt.xlabel("Predicted Probability (y^)")
plt.ylabel("Loss")
plt.title("Binary Cross-Entropy Loss Function")
plt.legend()
plt.grid()
plt.show()


# Printing a few example loss values
print("y^\tLoss")
for y_pred in [0.1, 0.3, 0.5, 0.7, 0.9]:
    loss = binary_cross_entropy(1, y_pred)
    print(f"{y_pred:.1f}\t{loss:.4f}")


# Weight Impact:
# In deep learning, multiple neurons process the same input but with different weights.
# If one neuron’s weight (w) is significantly increased, it can dominate the network and influence the final prediction disproportionately.
# This can reduce the effect of other neurons, making it difficult for the model to learn a balanced representation.
# The challenge: Optimizing these weights while preventing individual neurons from overpowering others.
# This is why regularization techniques like L1/L2 penalties (Lasso/Ridge), dropout, and batch normalization are commonly used in training deep learning models.
