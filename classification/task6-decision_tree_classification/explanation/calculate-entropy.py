import numpy as np
from collections import Counter


# The higher the entropy, the more impure the data (mixed with multiple classes), and the lower the entropy, the more pure (close to a single class).
def calculate_entropy(y):
    """Calculate entropy of a dataset."""
    total_samples = len(y)
    if total_samples == 0:
        return 0
    counts = Counter(y)
    probabilities = [count / total_samples for count in counts.values()]
    entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
    return entropy


def information_gain(X, y, feature_index, threshold):
    """Calculate information gain for a specific feature split."""
    parent_entropy = calculate_entropy(y)

    # Split the data
    left_indices = X[:, feature_index] <= threshold
    right_indices = ~left_indices

    # Calculate entropies for each subset
    left_entropy = calculate_entropy(y[left_indices])
    right_entropy = calculate_entropy(y[right_indices])

    # Weighted average of subset entropies
    left_weight = np.sum(left_indices) / len(y)
    right_weight = np.sum(right_indices) / len(y)
    weighted_entropy = left_weight * left_entropy + right_weight * right_entropy

    # Information gain
    gain = parent_entropy - weighted_entropy
    return gain


# Example dataset
X = np.array([[25, 50000], [30, 60000], [35, 70000], [40, 80000]])
y = np.array([0, 0, 1, 1])  # Labels

# Compute information gain for splitting on the first feature at threshold = 30
feature_index = 0
threshold = 30
gain = information_gain(X, y, feature_index, threshold)
print(f"Information Gain: {gain:.4f}")
