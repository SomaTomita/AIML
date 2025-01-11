############# Encoding categorical data #############
# How OneHotEncoder Works
# Each unique value in the Country column (France, Spain, Germany) is turned into a binary column:
from re import S


France = [1, 0, 0]
Spain = [0, 1, 0]
Germany = [0, 0, 1]

# transformers=[("encoder", OneHotEncoder(), [0])]: Apply OneHotEncoder to the first column (Country).
# remainder="passthrough": Keep all other columns (Age, Salary) as they are.

# LabelEncoder: Converts categorical values into integers.
# Applied to the Purchased column (y).


############# Splitting the dataset into the Training set and Test set #############
# Training Set:
# Used to train the machine learning model.
# The model learns patterns and relationships in this data.

# Test Set:
# Used to evaluate the performance of the trained model.
# It acts as unseen data, helping to estimate how well the model generalizes to new, real-world data.


############# Feature Scaling #############
import numpy as np

# sample data (age, salary)
X = np.array(
    [
        [38.77777777777778, 52000.0],
        [40.0, 63777.77777777778],
        [44.0, 72000.0],
        [38.0, 61000.0],
        [27.0, 48000.0],
        [48.0, 79000.0],
        [50.0, 83000.0],
        [35.0, 58000.0],
    ]
)

# average and standard deviation of each column
mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

# ************ standardize the data ************
X_scaled = (X - mean) / std

print("original data:")
print(X)
print("\n standardization data:")
print(X_scaled)

# check the mean and standard deviation of each column
print("\n mean:", mean)
print("std:", std)


# Math Explained
# @calculation_for_standardization_simple.png
# The mean (20) becomes the center, represented as 0
# The standard deviation (8.16) ensures that the data's spread is consistent, with most values within [-1, 1] if the data is normally distributed.
