import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Preprocessed data
dataset = pd.read_csv("regression/task5-support_vector_regression/svr.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
# print(X)
# print(y)

y = y.reshape(len(y), 1)
# print(y)


from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


from sklearn.svm import SVR

# Draw a line such that the distance from the data points outside the epsilon margin is minimized.
# The epsilon parameter is used to control the width of the margin.
# The larger the value of epsilon, the larger the margin.
regressor = SVR(kernel="linear", epsilon=0.1)
regressor.fit(X, y)
plt.scatter(sc_X.inverse_transform(X), sc_y.inverse_transform(y), color="red")
plt.plot(
    sc_X.inverse_transform(X),
    sc_y.inverse_transform(regressor.predict(X).reshape(-1, 1)),
    color="blue",
)
plt.show()
