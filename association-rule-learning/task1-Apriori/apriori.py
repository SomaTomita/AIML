import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# This data does not have information as a header on the first line. => header=None
dataset = pd.read_csv(
    "association-rule-learning/task1-Apriori/Market_Basket_Optimisation.csv",
    header=None,
)
# Preprocessing the data
transacions = []
for i in range(0, 7501):
    transacions.append(
        [str(dataset.values[i, j]) for j in range(0, 20)]
    )  # max row = 20 => range(0, 20)
# print(transacions)


from apyori import apriori

# Applying the Apriori algorithm
rules = apriori(
    transacions,
    min_support=0.003,  # Itemsets that appear at least 0.3% (22 times or more) of the total transactions (7500 items) are included in the analysis
    min_confidence=0.2,  # The probability that a subsequent event will occur when the previous event occurs. (20% or more)
    min_lift=3,  # Extract only strongly related rules (lifts of 3 or more)
    min_length=2,
    max_length=2,
)


results = list(rules)
# print(results)


# Defining the inspect function
def inspect(results):
    # condition（Left Hand Side）
    lhs = [tuple(result[2][0][0])[0] for result in results]
    # result（Right Hand Side）
    rhs = [tuple(result[2][0][1])[0] for result in results]
    # support, confidence, lift
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))


# Creating a DataFrame for easier analysis
retultsinDataFrame = pd.DataFrame(
    inspect(results),
    columns=["Left Hand Side", "Right Hand Side", "Support", "Confidence", "Lift"],
)
print(retultsinDataFrame)
