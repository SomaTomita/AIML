import numpy as np
import logging
from sklearn.model_selection import KFold, cross_val_score
from sklearn.svm import SVC
from sklearn.datasets import make_classification

# Configure logging to display intermediate results
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Step 1: Create a sample dataset
# Creating a simple binary classification dataset with 10 samples and 2 features
X = np.array(
    [
        [2.0, 4.1],
        [3.1, 5.2],
        [1.5, 3.7],
        [2.8, 4.8],
        [3.2, 5.3],
        [1.8, 3.9],
        [2.5, 4.5],
        [3.0, 5.0],
        [1.2, 3.5],
        [2.6, 4.6],
    ]
)
y = np.array([0, 1, 0, 1, 1, 0, 1, 1, 0, 1])  # Labels (binary classification)

# Logging dataset
logging.info("Dataset (Features and Labels):")
for i, (features, label) in enumerate(zip(X, y)):
    logging.info(f"Sample {i+1}: Features={features}, Label={label}")

# Step 2: Define k-Fold Cross Validation
k = 5  # Number of folds
kf = KFold(n_splits=k, shuffle=False)  # No shuffle to maintain order

logging.info("\nSplitting data into 5 folds:")

# Display fold distribution manually
folds = list(kf.split(X))
for i, (train_idx, test_idx) in enumerate(folds):
    logging.info(f"Fold {i+1}: Test Data Indices = {test_idx.tolist()}")

# Step 3: Train and Evaluate model using k-Fold Cross Validation
classifier = SVC(kernel="rbf", random_state=0)
accuracy_list = []

for i, (train_index, test_index) in enumerate(kf.split(X)):
    # Split data
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Train model
    classifier.fit(X_train, y_train)

    # Evaluate model
    accuracy = classifier.score(X_test, y_test) * 100
    accuracy_list.append(accuracy)

    # Log fold-wise results
    logging.info(f"\nFold {i+1}:")
    logging.info(f"Train Data Indices: {train_index.tolist()}")
    logging.info(f"Test Data Indices: {test_index.tolist()}")
    logging.info(f"Accuracy: {accuracy:.2f}%")

# Step 4: Calculate Mean and Standard Deviation
mean_accuracy = np.mean(accuracy_list)
std_dev = np.std(accuracy_list)

logging.info("\nFinal Results:")
logging.info(f"Mean Accuracy: {mean_accuracy:.2f}%")
logging.info(f"Standard Deviation: {std_dev:.2f}%")
