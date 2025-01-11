############# Taking care of missing data #############
import numpy as np
from sklearn.impute import SimpleImputer

# Input data
X = np.array([[1, np.nan, 2], [3, 5, np.nan], [6, 8, 9]])

# Imputer with mean strategy
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# Fit and transform
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

print(X)


# The transform method replaces missing values (np.nan) in the selected columns with their respective calculated means:
# Column 1 (Index 1): [np.nan, 5, 8] → [6.5, 5, 8]  - (5+8)/2=6.5
# Column 2 (Index 2): [2, np.nan, 9] → [2, 5.5, 9]  - (2+9)/2=5.5


# The parameter strategy determines how the missing values will be filled.
# "mean": Replaces missing values with the mean of the column.
# Other options include "median", "most_frequent", and "constant".
