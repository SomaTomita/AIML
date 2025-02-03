# Artificial Neural Network

from sklearn.base import accuracy_score
import numpy as np
import pandas as pd
import tensorflow as tf

# Part 1 - Data Preprocessing
dataset = pd.read_csv("deep-leaning/CNN/Churn_Modelling.csv")
X = dataset.iloc[:, 3:-1].values
y = dataset.iloc[:, -1].values
# print(X)
# print(y)

# Label Encoding the "Gender" column
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
X[:, 2] = le.fit_transform(X[:, 2])
# print(X)

# One Hot Encoding the "Geography" column
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [1])], remainder="passthrough"
)
X = np.array(ct.fit_transform(X))
# print(X)

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X = sc.fit_transform(X)
# print(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Part 2 - Building the ANN
# Initializing the ANN
ann = tf.keras.models.Sequential()

# Adding the input layer and the first hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation="relu"))
# Adding the second hidden layer
ann.add(tf.keras.layers.Dense(units=6, activation="relu"))
# Adding the output layer
ann.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))


# Part 3 - Training the ANN
# Compiling the ANN
ann.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Training the ANN on the Training set
ann.fit(X_train, y_train, batch_size=32, epochs=100)


# Part 4 - Making the predictions and evaluating the model
# Predicting the Test set results
y_pred = ann.predict(X_test)
y_pred = y_pred > 0.5
print(
    np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1)
)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)


# ------------------------------------------------------------------------------

# 1. Training Process and Accuracy Improvement
# ------------------------------------------------
# - Initially, at epoch 1, the model has a low accuracy (~49.62%) and a high loss (~0.7593).
# - By epoch 5, accuracy improves to ~81.77% with a decreasing loss (~0.4222).
# - As training progresses, accuracy stabilizes around ~86%-87% after ~30 epochs.
# - The final training accuracy reaches **~87.34%**, indicating decent performance.
# - The loss decreases gradually, showing that the model is learning effectively.


# 2. Model Convergence and Generalization
# ------------------------------------------------
# - After 100 epochs, the training accuracy is around 86%-87%.
# - This suggests that the model has **converged** and is no longer making significant improvements.
# - If the accuracy was still increasing sharply, more epochs might be needed.
# - If accuracy plateaus or decreases, early stopping could be considered to prevent overfitting.


# 3. Test Set Predictions and Thresholding
# ------------------------------------------------
# - The model makes predictions on the test set (`X_test`).
# - The raw output from the model is a probability (sigmoid activation), which is thresholded at **0.5**.
# - Any probability **≥ 0.5** is classified as `1` (churn), and any probability **< 0.5** is classified as `0` (no churn).


# 4. Confusion Matrix Analysis
# ------------------------------------------------
# - The confusion matrix:
#   ```
#   [[1515   80]
#    [ 193  212]]
#   ```
#   where:
#   - **True Negatives (TN) = 1515** (correctly classified as not churning)
#   - **False Positives (FP) = 80** (incorrectly predicted as churning)
#   - **False Negatives (FN) = 193** (missed actual churners)
#   - **True Positives (TP) = 212** (correctly predicted churners)

# 5. Performance Metrics Interpretation
# ------------------------------------------------
# - **Accuracy** = (TN + TP) / Total = (1515 + 212) / (1515 + 80 + 193 + 212) ≈ **86.4%**
# - **Precision (Positive Predictive Value)** = TP / (TP + FP) = 212 / (212 + 80) ≈ **72.63%**
#   - Measures how many of the predicted churn cases were actually correct.
# - **Recall (Sensitivity / True Positive Rate)** = TP / (TP + FN) = 212 / (212 + 193) ≈ **52.34%**
#   - Measures how many actual churn cases were correctly detected.
# - **F1 Score** = 2 × (Precision × Recall) / (Precision + Recall) ≈ **60.67%**
#   - A balanced metric considering both precision and recall.


# 6. Possible Issues and Improvements
# ------------------------------------------------
# - **False Negatives (193 cases) are relatively high**, meaning the model struggles to catch all churn cases.
#   - A higher recall (Sensitivity) would be ideal if detecting churn is critical.
#   - Solutions:
#     - Lower the **classification threshold** (e.g., from 0.5 to 0.4) to capture more positives.
#     - Use a different loss function (e.g., **focal loss**) if class imbalance exists.

# - **Overfitting risk:** Training accuracy is slightly higher than test accuracy, which may indicate minor overfitting.
#   - Solutions:
#     - Add **dropout layers** to reduce overfitting.
#     - Use **L2 regularization** to prevent excessive weight adjustments.

# - **Imbalanced Dataset Check:** If churn cases are much fewer than non-churn cases, try:
#   - **Oversampling** the minority class or **undersampling** the majority class.
#   - Using **class-weight balancing** in the model training.

# ------------------------------------------------------------------------------
