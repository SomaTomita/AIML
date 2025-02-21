############# Question #############
# Suppose you have a data set containing examples with multiple attributes and no labels. Which type of machine learning would be appropriate?
# Group of answer choices

# Supervised learning.
# Unsupervised learning.
# Reinforcement learning.
# Deep learning.

############# Answer #############
# ---------------------------------------------------------------
# 1. Understanding the Types of Machine Learning
# ---------------------------------------------------------------

# A. Supervised Learning (❌ Not Suitable)
# - Supervised learning requires both input features (X) and corresponding output labels (Y).
# - The model learns from labeled data by mapping input features to their correct output labels.
# - Example: A dataset where each record describes a patient (age, weight, symptoms) and has a label indicating whether they have a disease (yes/no).
# - Since your dataset has no labels, supervised learning is not applicable.

# B. Unsupervised Learning (✅ Correct Choice)
# - Unsupervised learning is used when the dataset consists of only input features, with no associated labels.
# - The model attempts to find hidden patterns, structures, or groupings within the data.
# - Example tasks:
#   - Clustering: Grouping similar data points together (e.g., customer segmentation).
#   - Dimensionality Reduction: Reducing the number of features while retaining key information (e.g., PCA).
#   - Anomaly Detection: Identifying rare or unusual data points (e.g., fraud detection).
# - Since your dataset lacks labels, this approach is the best choice.

# C. Reinforcement Learning (❌ Not Suitable)
# - Reinforcement learning (RL) involves an agent that interacts with an environment and learns based on rewards and penalties.
# - The model takes actions, receives feedback (reward/punishment), and optimizes its future actions.
# - Example: A robot learning to walk by trying different movements and receiving rewards for successful steps.
# - Since your dataset is static (no interaction or feedback loops), reinforcement learning is not applicable.

# D. Deep Learning (❌ Not a Learning Type by Itself)
# - Deep learning refers to using deep neural networks (DNNs) for complex learning tasks.
# - Deep learning can be applied to both supervised and unsupervised learning.
# - Example: A deep neural network for image recognition (supervised) or an autoencoder for anomaly detection (unsupervised).
# - Since deep learning is a technique rather than a distinct category of learning, it is not a direct answer.

# ---------------------------------------------------------------
# 2. Why Unsupervised Learning is the Best Fit?
# ---------------------------------------------------------------
# - Since your dataset has no labels, a model cannot be trained in a supervised manner.
# - Unsupervised learning is ideal because:
#   1. It can discover hidden patterns and relationships in the data.
#   2. It does not require labeled data, making it useful when labeling is expensive or infeasible.
#   3. It allows for data exploration, grouping similar records together or reducing dimensionality.

# ---------------------------------------------------------------
# 3. Examples of Unsupervised Learning Applications
# ---------------------------------------------------------------
# - Customer Segmentation (Clustering): Grouping customers based on purchasing behavior.
# - Anomaly Detection: Identifying fraudulent transactions in financial datasets.
# - Genomics and Biology: Identifying unknown species based on genetic similarities.
# - Dimensionality Reduction: Reducing the number of variables in a high-dimensional dataset for visualization.
