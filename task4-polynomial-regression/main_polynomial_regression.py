# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("task4-polynomial-regression/Position_Salaries.csv")
# :: → all columns,
# And 1:-1 → Select the second row (Level) to the last to the first row (before Salary)
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values


############# Training the Linear Regression model on the whole dataset #############
from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)

############# Visualising the Linear Regression results  #############
# plt.scatter(X, y, color="red")
# plt.plot(X, lin_reg.predict(X), color="blue")
# plt.title("Truth or Bluff (Linear Regression)")
# plt.xlabel("Position Level")
# plt.ylabel("Salary")
# plt.show()


############# Training the Polynomial Regression model on the whole dataset #############
from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

############# Visualising the Polynomial Regression results #############
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg_2.predict(X_poly), color="blue")
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()


############# Predicting a new result with Regressions #############
# Predicting a new result with Linear Regression
lin_reg.predict([[6.5]])

# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
