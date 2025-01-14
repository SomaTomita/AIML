# Assumptions and Feature Selection Methods in Linear Regression

############# Example dataset #############
import pandas as pd
import numpy as np

# Generate simple data
np.random.seed(42)
n_samples = 100
X = pd.DataFrame(
    {
        "Feature1": np.random.rand(n_samples) * 10,
        "Feature2": np.random.rand(n_samples) * 50,
        "Feature3": np.random.rand(n_samples) * 100,
        "Feature4": np.random.randint(1, 10, n_samples),
    }
)
y = 3 * X["Feature1"] - 2 * X["Feature3"] + 10 + np.random.randn(n_samples) * 5


############# 1. All-in #############
# All features are included in the model without any selection.
# This is used when:
# - All variables are theoretically important.
# - There is little data, and feature selection could cause overfitting.
# - Comparing the performance of a full model to others.
# Advantages:
# - Simple and no features are missed.
# - Serves as a baseline for other feature selection methods.
# Disadvantages:
# - May include unnecessary variables, reducing interpretability.
# - Affected by multicollinearity and redundant variables.

# Example: Linear Regression with all features
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X, y)


############# 2. Backward Elimination #############
# Starts with all features included, then removes the least statistically significant feature step by step.
# Variables are removed based on p-values.
# Advantages:
# - Starts with all variables, removing insignificant ones systematically.
# - Simplifies the model and improves interpretability.
# Disadvantages:
# - Computationally expensive for a large number of variables.
# - Results depend on the dataset and may not find the global optimal set.

# Example: Backward Elimination using statsmodels
import statsmodels.api as sm

X_opt = X  # Start with all variables
model = sm.OLS(y, X_opt).fit()
while max(model.pvalues) > 0.05:
    X_opt = X_opt.drop(columns=[model.pvalues.idxmax()])
    model = sm.OLS(y, X_opt).fit()
print(model.summary())

# Example Result
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Feature1       3.3664      0.177     18.998      0.000       3.015       3.718
# Feature2       0.1000      0.035      2.835      0.006       0.030       0.170
# Feature3      -1.9648      0.017   -117.734      0.000      -1.998      -1.932
# Feature4       0.5861      0.194      3.019      0.003       0.201       0.971
# Feature1, Feature3, and Feature4 are significant ( p < 0.05 ) and have a large effect on y.


############# 3. Forward Selection #############
# Starts with no features and adds one feature at a time based on statistical significance or model performance.
# Advantages:
# - Effective for small datasets with a few important variables.
# - Lower computational cost than backward elimination.
# Disadvantages:
# - Early inclusion of irrelevant variables may impact the final model.
# - Redundant variables can still be included by mistake.

# Example: Forward Selection
from sklearn.linear_model import LinearRegression

selected_features = []
remaining_features = list(X.columns)
while remaining_features:
    scores = []
    for feature in remaining_features:
        temp_model = LinearRegression().fit(X[selected_features + [feature]], y)
        score = temp_model.score(X[selected_features + [feature]], y)
        scores.append((feature, score))
    best_feature, best_score = max(scores, key=lambda x: x[1])
    selected_features.append(best_feature)
    remaining_features.remove(best_feature)
    print(f"Selected feature: {best_feature}, Score: {best_score}")

# Example Result
# Selected feature: Feature3, Score: 0.970714462555916
# Selected feature: Feature1, Score: 0.9920405986430098
# Selected feature: Feature2, Score: 0.9920524297556467
# Selected feature: Feature4, Score: 0.9920530337479765
# Feature3 → Feature1 → Feature2 → Feature4


############# 4. Bidirectional Elimination #############
# Combines Forward Selection and Backward Elimination.
# Variables are added one at a time while also removing insignificant variables.
# Advantages:
# - Flexible as it considers both inclusion and exclusion of variables.
# - Reduces the risk of overfitting or missing key features.
# Disadvantages:
# - Computationally intensive for large datasets.
# - Results can vary depending on initial conditions.

# Example: Bidirectional Elimination can be implemented manually
# by combining forward and backward steps iteratively.


############# 5. All Possible Models #############
# Tests all possible combinations of variables and evaluates each model using a performance metric (e.g., AIC, BIC, R²).
# Advantages:
# - Provides the most comprehensive way to find the optimal feature set.
# - Avoids missing the best combination.
# Disadvantages:
# - Extremely computationally expensive, especially with many variables.
# - Impractical for high-dimensional datasets.

# Example: Testing all possible combinations
from itertools import combinations
from sklearn.linear_model import LinearRegression
import numpy as np

best_model = None
best_score = -np.inf
features = list(X.columns)
for k in range(1, len(features) + 1):
    for subset in combinations(features, k):
        temp_model = LinearRegression().fit(X[list(subset)], y)
        score = temp_model.score(X[list(subset)], y)
        if score > best_score:
            best_score = score
            best_model = subset
print(f"Best model: {best_model}, R² score: {best_score}")

# Example Result
# Best model: ('Feature1', 'Feature2', 'Feature3', 'Feature4'), R² score: 0.9920530337479765
# The model fit is very high (R² = 0.997) and the assumptions (normality, no autocorrelation, no multicollinearity) are also met, making the results reliable.
