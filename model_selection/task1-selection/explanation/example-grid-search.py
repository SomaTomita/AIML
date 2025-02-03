import numpy as np
import logging

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV

# --------------------------------------------------------------------------------------
# Configure logging
# --------------------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO, format="%(message)s")

# --------------------------------------------------------------------------------------
# 1. Create a sample dataset (10 samples, 2 features, binary classification)
# --------------------------------------------------------------------------------------
logging.info("Step 1: Creating a sample dataset.")
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
y = np.array([0, 1, 0, 1, 1, 0, 1, 1, 0, 1])

logging.info("\nDataset:")
for i, (features, label) in enumerate(zip(X, y)):
    logging.info(f" Sample {i+1}: Features={features}, Label={label}")

# --------------------------------------------------------------------------------------
# 2. Split the dataset into train and test sets
# --------------------------------------------------------------------------------------
logging.info("\nStep 2: Splitting dataset into train and test sets.")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
logging.info(f" Train size: {len(X_train)}, Test size: {len(X_test)}")

# --------------------------------------------------------------------------------------
# 3. Define a parameter grid for Grid Search
# --------------------------------------------------------------------------------------
# We'll explore different values of C and gamma for the RBF kernel.
# This helps find the best combination that might reduce bias (if the model is too simple)
# and variance (if the model overfits).
logging.info("\nStep 3: Defining parameter grid for SVC.")
param_grid = {"C": [0.1, 1, 10], "gamma": [0.001, 0.01, 0.1], "kernel": ["rbf"]}
logging.info(f"Parameter grid: {param_grid}")

# --------------------------------------------------------------------------------------
# 4. Set up the GridSearchCV
# --------------------------------------------------------------------------------------
# GridSearchCV will run an internal k-Fold Cross Validation (cv=5 by default in this example)
# for each combination of parameters, then select the best combination based on the scoring.
# Using cross validation inside the grid search helps mitigate the variance of the results.
logging.info("\nStep 4: Performing GridSearchCV with k-Fold Cross Validation (k=5).")
svc = SVC()
grid_search = GridSearchCV(
    estimator=svc, param_grid=param_grid, scoring="accuracy", cv=5
)

# --------------------------------------------------------------------------------------
# 5. Train the model using GridSearchCV
# --------------------------------------------------------------------------------------
# Here, GridSearchCV will try every combination of parameters in param_grid.
# It will also do k-Fold Cross Validation for each combination, obtaining an average accuracy.
# We log the results of each combination.
logging.info("\nStep 5: Training the model via GridSearch.")

grid_search.fit(X_train, y_train)

logging.info("\nGrid Search Completed.")
logging.info("All parameter combinations with their mean test scores:")
for params, mean_score, scores in zip(
    grid_search.cv_results_["params"],
    grid_search.cv_results_["mean_test_score"],
    grid_search.cv_results_["std_test_score"],
):
    logging.info(f" Params: {params}, Mean Accuracy: {mean_score:.4f}")

# --------------------------------------------------------------------------------------
# 6. Evaluate best parameters and final model
# --------------------------------------------------------------------------------------
logging.info("\nStep 6: Evaluating the best parameters and the best model.")
logging.info(f"Best Parameters: {grid_search.best_params_}")
logging.info(f"Best Score (Mean CV Accuracy): {grid_search.best_score_:.2f}")

# The best model found by GridSearchCV is stored in grid_search.best_estimator_
final_model = grid_search.best_estimator_

# --------------------------------------------------------------------------------------
# 7. Test the final model on the test set
# --------------------------------------------------------------------------------------
# This test set is unseen data, so we can evaluate how well the chosen parameters
# generalize to new data.
logging.info("\nStep 7: Testing the best model on the held-out test set.")
test_accuracy = final_model.score(X_test, y_test)
logging.info(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# --------------------------------------------------------------------------------------
# Explanation of how Grid Search and CV help mitigate bias and variance:
# --------------------------------------------------------------------------------------
# 1) Bias is reduced because we search for parameters that can make the model more flexible.
#    For instance, if C is too small, the model might be too simple (high bias).
#    By searching a range of C values, we can find a more optimal point.
# 2) Variance is reduced because internal k-Fold CV checks how consistent the model's accuracy
#    is across different data partitions. If the model overfits, it will get inconsistent
#    results across folds. GridSearchCV uses these folds to pick a parameter set that is
#    stable across the splits, thus reducing variance.
# 3) If the final accuracy is consistently high across folds and on the final test set,
#    it typically indicates that overfitting is not severe. However, we must also check
#    the difference between training and validation/test accuracies.
#    If training accuracy is extremely high but test accuracy is moderate, there may be overfitting.

# --------------------------------------------------------------------------------------
# 8. Check Overfitting: If test accuracy is close to cross-validation accuracy,
#    we can infer that overfitting is not significant.
# --------------------------------------------------------------------------------------
cv_accuracy = grid_search.best_score_
logging.info("\nStep 8: Checking for potential overfitting.")
logging.info(f"Best Mean CV Accuracy: {cv_accuracy:.2f}")
logging.info(f"Test Set Accuracy: {test_accuracy:.2f}")

if abs(cv_accuracy - test_accuracy) < 0.05:
    logging.info(
        "The difference between CV accuracy and test accuracy is small. Overfitting is likely minimal."
    )
else:
    logging.info(
        "The difference between CV accuracy and test accuracy is noticeable. Could indicate some overfitting or underfitting."
    )

logging.info("\n--- Grid Search Example Completed ---")
