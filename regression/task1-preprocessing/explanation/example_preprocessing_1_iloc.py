############# Importing the dataset #############
# Data Preprocessing Template

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("regression/task1-preprocessing/Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

# how to use iloc:
# This allows you to select specific rows and columns from the dataset by position (not by name).
# : means "select all rows."
# :-1 means "select all columns except the last one."
# -1 means "select only the last column."
