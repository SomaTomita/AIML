############# Question #############

# Reinforcement learning systems learn by:
# Group of answer choices

# - Clustering similar examples in a set of unlabelled examples.
# - Passively observing their environment and generalising from the set of observations.
# - Taking actions in their environment and learning from the good or bad outcomes of those actions.
# - Generalising from a set of labelled examples to construct a function that maps from an example to a prediction of the label.


############# Answer #############
"Taking actions in their environment and learning from the good or bad outcomes of those actions."


# ------------------------------------------------------------------------------
# Detailed Explanation
# ------------------------------------------------------------------------------
# 1. What is Reinforcement Learning (RL)?
#    - Reinforcement Learning (RL) is a type of machine learning where an agent
#      interacts with an environment by taking actions.
#    - The agent receives **rewards (positive feedback)** for good actions and
#      **penalties (negative feedback)** for bad actions.
#    - The goal is to learn an optimal policy that maximizes **cumulative rewards**
#      over time.
#    - This process is inspired by trial-and-error learning seen in humans and animals.

# 2. Why is the correct answer "Taking actions in their environment and learning from outcomes"?
#    - RL systems learn by **actively making decisions** rather than passively observing.
#    - The agent explores different **actions**, receives **feedback**, and adjusts
#      future actions based on that feedback.
#    - This is the core of RL: **learning by interacting** with the environment.

# ------------------------------------------------------------------------------
# 3. Why are the other options incorrect?
# ------------------------------------------------------------------------------
#    - "Clustering similar examples in a set of unlabelled examples."
#       → This describes **unsupervised learning**, such as k-means clustering.
#       → In unsupervised learning, the system groups similar data points based on
#         patterns, without requiring labels.
#       → RL, on the other hand, does not focus on clustering but **decision-making
#         through interactions**.

#    - "Passively observing their environment and generalising from the set of observations."
#       → This approach is **closer to supervised learning** or passive learning.
#       → In **supervised learning**, a model learns from labeled training data and
#         generalizes based on those examples.
#       → However, RL requires **active exploration**—not just passive observation.

#    - "Generalising from a set of labelled examples to construct a function that
#       maps from an example to a prediction of the label."
#       → This is **supervised learning**, where models learn a mapping function
#         from input features to output labels.
#       → Supervised learning relies on **predefined correct answers**, whereas RL
#         does not require labeled data but instead learns through rewards and
#         penalties.
# ------------------------------------------------------------------------------


# Short Summary
# Reinforcement Learning (RL) is like training a pet. The agent (like a dog) performs actions, and we give it rewards (treats) or penalties (scolding).
# Over time, it learns which actions maximize rewards.
# Incorrect choices describe other types of machine learning:
# Clustering (Unsupervised Learning)
# Passive Observation (Supervised Learning)
# Label-Based Predictions (Supervised Learning)
