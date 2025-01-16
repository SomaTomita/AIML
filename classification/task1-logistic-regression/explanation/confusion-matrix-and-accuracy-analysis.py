# Confusion Matrix and Accuracy Analysis

# This table represents the confusion matrix results:
# |                 | Actual Class 0 (Purchased=0) | Actual Class 1 (Purchased=1) |
# |-----------------|------------------------------|------------------------------|
# | Predicted 0     | True Negatives (TN) = 65     | False Negatives (FN) = 8     |
# | Predicted 1     | False Positives (FP) = 3     | True Positives (TP) = 24     |


# Confusion Matrix Breakdown:
# 1. True Negatives (TN = 65):
#    - Users who did not purchase (Purchased=0), correctly predicted as not purchasing.

# 2. False Positives (FP = 3):
#    - Users who did not purchase but were incorrectly predicted as purchasing.

# 3. False Negatives (FN = 8):
#    - Users who did purchase (Purchased=1) but were incorrectly predicted as not purchasing.

# 4. True Positives (TP = 24):
#    - Users who did purchase, correctly predicted as purchasing.


# Accuracy Calculation:
# Accuracy formula: (TP + TN) / Total
# TP = 24, TN = 65, Total = 100 (sum of all matrix values: 65 + 3 + 8 + 24)
# Accuracy = (65 + 24) / 100 = 89%

# The model has an accuracy of 89%, meaning it correctly predicted 89% of all cases.
