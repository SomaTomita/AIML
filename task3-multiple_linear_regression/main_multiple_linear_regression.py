# Multiple Linear Regression

# preprocessed data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("task3-multiple_linear_regression/50_Startups.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
# print(X)
# print(y)

ct = ColumnTransformer(
    transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough"
)
X = np.array(ct.fit_transform(X))
# print(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


############# Training the Multiple Linear Regression model on the Training set #############
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)  # Set to display up to two decimal places
# If the predictions are close to the actual values, it means that the model explains the objective variable well.
print(
    np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1)
)  # Transform y_pred (predicted values) and y_test (actual values) into a one-column two-dimensional array, concatenated horizontally (axis(third argument of np.concatenate)=1)


# Special Edition
############# Implementation to predict specific numbers #############
print(
    "Specific numbers (California)",
    regressor.predict([[1, 0, 0, 160000, 130000, 300000]]),
)

############# Coefficient (Slope) and Intercept #############
print("Coefficients:", regressor.coef_)
print("Intercept:", regressor.intercept_)
