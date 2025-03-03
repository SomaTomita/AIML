############# Question #############
# Suppose you have a data set containing examples with multiple attributes and no labels.
# Which type of machine learning would be appropriate?
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


# ---------------------------------------------------------------
############# Question 1 #############
# Which of the following is an example of supervised learning?
# Group of answer choices
# - Clustering customers based on their purchasing behavior.
# - Identifying fraudulent transactions without prior labels.
# - Predicting house prices based o n historical sales data.
# - Reducing the number of features in a high-dimensional dataset.

############# Answer 1 #############
# ---------------------------------------------------------------
# 1. Understanding the Types of Machine Learning
# ---------------------------------------------------------------

# A. Clustering Customers (❌ Incorrect)
# - Clustering is an unsupervised learning technique.
# - It does not use labeled data; instead, it groups similar data points based on patterns.
# - Example: Segmenting customers based on purchasing habits.

# B. Fraud Detection Without Labels (❌ Incorrect)
# - If fraud detection is done without labeled data, it falls under unsupervised learning (e.g., anomaly detection).
# - Supervised learning requires labeled examples (e.g., past transactions labeled as "fraud" or "not fraud").

# C. Predicting House Prices (✅ Correct Answer)
# - Supervised learning uses labeled training data.
# - House price prediction involves:
#   - Input Features (X): House size, location, number of rooms, etc.
#   - Output Label (Y): House price.
# - Since we train the model on known input-output pairs, this is a supervised learning problem.

# D. Dimensionality Reduction (❌ Incorrect)
# - Dimensionality reduction is typically an unsupervised learning method.
# - It does not involve explicit labels; instead, it reduces the number of variables while retaining important information.
# - Example: Principal Component Analysis (PCA).

# ---------------------------------------------------------------
# 2. Why Predicting House Prices is the Best Answer?
# ---------------------------------------------------------------
# - Supervised learning requires labeled data (input-output pairs).
# - The model learns from historical sales data and predicts future prices.
# - It is a regression problem, a common type of supervised learning.

# ---------------------------------------------------------------
# 3. Real-World Applications of Supervised Learning
# ---------------------------------------------------------------
# - Spam Detection: Classifying emails as spam or not spam.
# - Medical Diagnosis: Predicting diseases based on patient symptoms.
# - Credit Scoring: Assessing loan risk based on credit history.


# ---------------------------------------------------------------
############# Question 2 #############
# Which learning method is best suited for training an AI agent to play a video game by trial and error?
# Group of answer choices
# - Supervised learning.
# - Unsupervised learning.
# - Reinforcement learning.
# - Semi-supervised learning.

############# Answer 2 #############
# ---------------------------------------------------------------
# 1. Understanding the Learning Approaches
# ---------------------------------------------------------------

# A. Supervised Learning (❌ Incorrect)
# - Requires labeled data with correct answers.
# - AI learns from past examples, but video games involve dynamic environments where predefined labels are not available.

# B. Unsupervised Learning (❌ Incorrect)
# - Unsupervised learning finds patterns in unlabeled data.
# - Does not involve decision-making based on rewards and penalties, which is crucial in a gaming scenario.

# C. Reinforcement Learning (✅ Correct Answer)
# - Involves an agent that interacts with an environment.
# - Uses rewards and penalties to learn optimal actions.
# - Example: An AI playing chess learns by winning (reward) or losing (penalty).
# - Trial-and-error approach is essential for tasks like game playing, robotics, and self-driving cars.

# D. Semi-Supervised Learning (❌ Incorrect)
# - Uses a mix of labeled and unlabeled data.
# - Not designed for interactive learning environments like video games.

# ---------------------------------------------------------------
# 2. Why Reinforcement Learning is the Best Fit?
# ---------------------------------------------------------------
# - The AI must explore different strategies and learn from experience.
# - Trial and error is fundamental to its learning process.
# - Example algorithms: Q-learning, Deep Q Networks (DQN), Proximal Policy Optimization (PPO).

# ---------------------------------------------------------------
# 3. Real-World Applications of Reinforcement Learning
# ---------------------------------------------------------------
# - Game AI: AlphaGo, OpenAI Five (Dota 2), DeepMind’s Atari AI.
# - Robotics: Teaching robots to walk and interact with environments.
# - Autonomous Driving: Self-driving cars optimizing routes and avoiding collisions.


# ---------------------------------------------------------------
############# Question 3 #############
# Which of the following best describes the primary goal of clustering in machine learning?
# Group of answer choices
# - To predict a continuous value based on input data.
# - To find hidden patterns or groupings within a dataset.
# - To classify data points into predefined categories.
# - To improve the accuracy of a reinforcement learning agent.

############# Answer 3 #############
# ---------------------------------------------------------------
# 1. Understanding Clustering
# ---------------------------------------------------------------

# A. Predicting a Continuous Value (❌ Incorrect)
# - Regression is used for predicting continuous values (e.g., predicting house prices).
# - Clustering does not involve labeled output values.

# B. Finding Hidden Patterns or Groups (✅ Correct Answer)
# - Clustering is an unsupervised learning technique.
# - It identifies natural groupings in data without predefined labels.
# - Example: Customer segmentation (grouping similar customers for targeted marketing).

# C. Classifying Data into Predefined Categories (❌ Incorrect)
# - Classification is a supervised learning method.
# - Requires labeled data (e.g., distinguishing between spam and non-spam emails).
# - Clustering does not rely on predefined categories.

# D. Improving Reinforcement Learning Accuracy (❌ Incorrect)
# - Clustering is not directly related to reinforcement learning.
# - RL focuses on learning through rewards and penalties, while clustering focuses on data structure exploration.

# ---------------------------------------------------------------
# 2. Why Clustering is the Best Answer?
# ---------------------------------------------------------------
# - It helps discover underlying patterns without labels.
# - Used for data exploration, anomaly detection, and segmentation.

# ---------------------------------------------------------------
# 3. Real-World Applications of Clustering
# ---------------------------------------------------------------
# - Customer Segmentation: Grouping customers by shopping habits.
# - Image Segmentation: Dividing images into meaningful regions.
# - Biology & Genetics: Identifying species based on genetic similarities.
# - Anomaly Detection: Detecting fraudulent transactions in banking.
