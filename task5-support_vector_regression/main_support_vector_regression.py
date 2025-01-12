import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Preprocessed data
dataset = pd.read_csv("task5-support_vector_regression/Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
# 1:-1 → Select the second row (Level) to the last to the first row (before Salary)
y = dataset.iloc[:, -1].values
y = y.reshape(len(y), 1)

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)
# print(X)
# print(y)


############# Training the SVR model on the whole dataset #############
from sklearn.svm import SVR

regressor = SVR(kernel="rbf")
regressor.fit(X, y.ravel())

############# Predicting a new result (Calculate the projected value (salary) for a position at “Level 6.5.”) #############
y_pred = sc_y.inverse_transform(  # Inverse conversion of standardized predictions to the original scale (actual salary range).
    # sc_X.transform() = Input value of 6.5 is standardized (scale conversion) and converted to a scale that the model can easily handle.
    regressor.predict(sc_X.transform([[6.5]])).reshape(-1, 1)
)
print("Predicted Salary for Level 6.5:", y_pred)


############# Visualising the SVR results #############
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color="red")
plt.plot(
    sc_X.inverse_transform(X),
    sc_y.inverse_transform(regressor.predict(X).reshape(-1, 1)),
    color="blue",
)
plt.title("Truth or Bluff (SVR)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()


############# Visualising the SVR results (for higher resolution and smoother curve) #############
X_grid = np.arange(
    min(sc_X.inverse_transform(X)[:, 0]), max(sc_X.inverse_transform(X)[:, 0]), 0.1
)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color="red")
plt.plot(
    X_grid,
    sc_y.inverse_transform(regressor.predict(sc_X.transform(X_grid)).reshape(-1, 1)),
    color="blue",
)
plt.title("Truth or Bluff (SVR)")
plt.xlabel("Position level")
plt.ylabel("Salary")
plt.show()
