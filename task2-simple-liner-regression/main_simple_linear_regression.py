# Simple Linear Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# preprocessed data
dataset = pd.read_csv("task2-simple-liner-regression/Salary_Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=1 / 3, random_state=0
)  # Allocate 1/3 of the data to the test set.


############# Training the Simple Linear Regression model on the Training set #############
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)

############# Predicting the Test set results #############
y_pred = regressor.predict(X_test)
# print(y_pred)

############# Visualising the Training set results #############
# plt.scatter(X_train, y_train, color="red")
# plt.plot(X_train, regressor.predict(X_train), color="blue")
# plt.title("Salary vs Experience (Training set)")
# plt.xlabel("Years of Experience")
# plt.ylabel("Salary")
# plt.show()

############# Visualising the Test set results #############
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary vs Experience (Test set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# Special Edition
############# Predicting a new result with Simple Linear Regression #############
years_of_experience = np.array([[12]])
predicted_salary = regressor.predict(years_of_experience)
print(f"Predicted salary for 12 years of experience: {predicted_salary[0]}")

############# Coefficient (Slope) and Intercept #############
coefficient = regressor.coef_[0]
intercept = regressor.intercept_

print(f"Coefficient (Slope): {coefficient}")
print(f"Intercept: {intercept}")
