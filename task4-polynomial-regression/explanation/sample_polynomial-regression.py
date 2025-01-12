############# PolynomialFeatures #############
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("task4-polynomial-regression/Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
# print(X_poly)
# Output:
# [[  1.   1.   1.]
#  [  1.   2.   4.]
#  [  1.   3.   9.]
#  [  1.   4.  16.]
#  [  1.   5.  25.]
#  [  1.   6.  36.]
#  [  1.   7.  49.]
#  [  1.   8.  64.]
#  [  1.   9.  81.]
#  [  1.  10. 100.]]

# result = [1, x, x ^ 2]  - (if degree=2)


############# LinearRegression #############
from sklearn.linear_model import LinearRegression
import numpy as np

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

print("Coefficients（β1, β2）:", lin_reg_2.coef_)
print("Intercept（β0）:", lin_reg_2.intercept_)

# @example-calculations.png
y_pred = lin_reg_2.predict(X_poly)
print("Predicted value（y_pred）:", y_pred)
