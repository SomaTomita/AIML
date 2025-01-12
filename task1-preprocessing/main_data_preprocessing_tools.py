# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

############# 1. Importing the dataset #############
dataset = pd.read_csv("task1-preprocessing/Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# print(X)
# print(y)


############# 12 Taking care of missing data #############
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
# specifically selecting the columns from index 1 to index 2 (3 is exclusive) which means "age" and "Salary" in the dataset.
imputer.fit(X[:, 1:3])  # caluculate
X[:, 1:3] = imputer.transform(X[:, 1:3])  # replace
# print(X)


############# 3. Encoding categorical data #############
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(
    # "Country" (index 0) column will be one-hot encoded.
    transformers=[("encoder", OneHotEncoder(), [0])],
    remainder="passthrough",
)
X = np.array(ct.fit_transform(X))
# print(X)

# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(y)
# print(y)


############# 4. Splitting the dataset into the Training set and Test set #############
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)


############# 5. Feature Scaling #############
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)
