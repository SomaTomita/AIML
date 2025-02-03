import numpy as np

# Backpropagation Explanation:
# Backpropagation (Backward Propagation of Errors) is a supervised learning algorithm used to train neural networks.
# It calculates the gradient of the loss function with respect to each weight using the chain rule of calculus.
# The weights are updated using gradient descent, ensuring the network learns to minimize error iteratively.

# The key steps in backpropagation:
# 1. Forward Pass: Compute the output of the network layer by layer.
# 2. Compute the Loss: Compare the predicted output with the true output using a loss function.
# 3. Backward Pass: Calculate the gradient of the loss function with respect to each weight using the chain rule.
# 4. Update Weights: Use gradient descent (or another optimization algorithm) to update the weights.


# Example: A simple neural network with one hidden layer
# We use sigmoid activation function and mean squared error (MSE) loss.


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)  # Derivative of the sigmoid function


def mse_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)  # Mean Squared Error loss function


# Neural Network Parameters
np.random.seed(0)
input_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # XOR inputs
expected_output = np.array([[0], [1], [1], [0]])  # XOR outputs

input_layer_neurons = 2  # Input layer neurons
hidden_layer_neurons = 2  # Hidden layer neurons
output_neurons = 1  # Output layer neurons

# Initialize weights and biases
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

# Learning rate
learning_rate = 0.5
epochs = 10000

# Training the neural network
for epoch in range(epochs):
    # Forward Pass
    hidden_layer_activation = np.dot(input_data, hidden_weights) + hidden_bias
    hidden_layer_output = sigmoid(hidden_layer_activation)

    final_activation = np.dot(hidden_layer_output, output_weights) + output_bias
    predicted_output = sigmoid(final_activation)

    # Compute Loss
    loss = mse_loss(expected_output, predicted_output)

    # Backward Pass
    error = expected_output - predicted_output
    d_predicted_output = error * sigmoid_derivative(predicted_output)

    error_hidden_layer = d_predicted_output.dot(output_weights.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Updating weights and biases
    output_weights += hidden_layer_output.T.dot(d_predicted_output) * learning_rate
    output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * learning_rate
    hidden_weights += input_data.T.dot(d_hidden_layer) * learning_rate
    hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

    # Print loss every 1000 epochs
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Print final predictions
print("Final Predictions:")
print(predicted_output)
