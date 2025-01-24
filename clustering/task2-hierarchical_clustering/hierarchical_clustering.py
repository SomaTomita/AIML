# Hierarchical Clustering

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("clustering/task2-hierarchical_clustering/Mall_Customers.csv")
X = dataset.iloc[:, [3, 4]].values


############# Using the dendrogram to find the optimal number of clusters ############
import scipy.cluster.hierarchy as sch

dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.show()

# Training the Hierarchical Clustering model on the dataset
from sklearn.cluster import AgglomerativeClustering

hc = AgglomerativeClustering(n_clusters=5, metric="euclidean", linkage="ward")
y_hc = hc.fit_predict(X)
# print(y_hc)


# Visualising the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c="red", label="Cluster 1")
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c="blue", label="Cluster 2")
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=100, c="green", label="Cluster 3")
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s=100, c="cyan", label="Cluster 4")
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s=100, c="magenta", label="Cluster 5")
plt.title("Clusters of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()


############# Interpretation by Cluster ############
# Cluster 0: Low Income, High Spending

# Customers with low income but a high spending score.
# Likely to include younger individuals or customers with a strong inclination towards high consumption.
# ex) Marketing and promotions targeting luxury products may be effective for this group.


# Cluster 1: Medium Income, Medium Spending

# Customers with both average income and spending scores.
# Products and services targeted at the general population are suitable for this group.
# ex) Recommending cost-effective products is a good strategy for these customers.


# Cluster 2: High Income, High Spending

# Customers with high income and a strong willingness to spend.
# High-end products and exclusive services targeted at affluent customers are effective.
# ex) Building relationships through customer loyalty programs is also beneficial.


# Cluster 3: High Income, Low Spending

# Customers with high income but low spending scores.
# Likely to include individuals who are budget-conscious or make purchases infrequently.
# ex) Offering discounts or incentives can help activate this group.


# Cluster 4: Low Income, Low Spending

# Customers with both low income and low spending scores.
# Likely to be cost-sensitive, making affordable products more effective for this group.
# This group is less likely to generate significant profits.
