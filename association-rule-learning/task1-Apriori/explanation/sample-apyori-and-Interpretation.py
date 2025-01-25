import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transaction dataset
data = {
    "Bread": [1, 1, 0, 1, 0],
    "Butter": [1, 0, 0, 1, 1],
    "Jam": [0, 1, 1, 1, 0],
}
df = pd.DataFrame(data)

# Step 1: Calculate frequent itemsets using apriori
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

# Step 2: Generate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.1)

# Step 3: Display the results
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules[["antecedents", "consequents", "support", "confidence", "lift"]])


# Frequent Itemsets:
#    support              itemsets
# 0      0.6               (Bread)
# 1      0.6              (Butter)
# 2      0.6                 (Jam)
# 3      0.4       (Butter, Bread)
# 4      0.4          (Jam, Bread)
# 5      0.2         (Butter, Jam)
# 6      0.2  (Butter, Jam, Bread)

# Association Rules:
#         antecedents      consequents  support  confidence      lift
# 0          (Butter)          (Bread)      0.4    0.666667  1.111111
# 1           (Bread)         (Butter)      0.4    0.666667  1.111111
# 2             (Jam)          (Bread)      0.4    0.666667  1.111111
# 3           (Bread)            (Jam)      0.4    0.666667  1.111111
# 4          (Butter)            (Jam)      0.2    0.333333  0.555556
# 5             (Jam)         (Butter)      0.2    0.333333  0.555556
# 6     (Butter, Jam)          (Bread)      0.2    1.000000  1.666667
# 7   (Butter, Bread)            (Jam)      0.2    0.500000  0.833333
# 8      (Jam, Bread)         (Butter)      0.2    0.500000  0.833333
# 9          (Butter)     (Jam, Bread)      0.2    0.333333  0.833333
# 10            (Jam)  (Butter, Bread)      0.2    0.333333  0.833333
# 11          (Bread)    (Butter, Jam)      0.2    0.333333  1.666667


# Confidence:
# Example: (Butter) → (Bread) has a confidence level of 0.6667:
#  “Of those who buy butter, there is a 66.67% probability that they also buy bread.”

# Lift:
# Example: (Butter) → (Bread) has a lift value of 1.1111.
#  “The probability of purchasing bread is 11.11% higher than for a random purchase”

# Summary of Interpretation of lift values:
#  > 1: positive correlation (purchase relationship exists).
# Lift = 1: Independent (no relationship).
# Lift < 1: Negative correlation (rather unlikely to be purchased together).


# Rule with strong association:
#  (Butter, Jam) → (Bread):
# Support value: 0.2 (occurs in 20% of transactions).
# Confidence: 1.0 (100% probability that those who bought butter and jam also bought bread).
# Lift: 1.6667 (66.67% more likely than usual to buy bread).
# Interpretation: People who buy butter and jam together always tend to buy bread as well.
