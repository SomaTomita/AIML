# K-Means Clustering

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("clustering/task1-k_means_clustering/Mall_Customers.csv")
X = dataset.iloc[:, [3, 4]].values  # Annual Income (k$), Spending Score (1-100)


############# Using the elbow method to find the optimal number of clusters ############
from sklearn.cluster import KMeans

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.show()

# Training the K-Means model on the dataset
# Based on the elbow method, we choose 5 clusters for the dataset
# Training the K-Means model on the dataset with 5 clusters
kmeans = KMeans(n_clusters=5, init="k-means++", random_state=42)
y_kmeans = kmeans.fit_predict(X)
# print(y_kmeans)


# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c="red", label="Cluster 1")
plt.scatter(
    X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c="blue", label="Cluster 2"
)
plt.scatter(
    X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c="green", label="Cluster 3"
)
plt.scatter(
    X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c="cyan", label="Cluster 4"
)
plt.scatter(
    X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=100, c="magenta", label="Cluster 5"
)
plt.scatter(
    kmeans.cluster_centers_[:, 0],  # X-coordinates of centroids
    kmeans.cluster_centers_[:, 1],  # Y-coordinates of centroids
    s=300,  # Size of the centroid markers
    c="yellow",  # Color of centroids
    label="Centroids",  # Legend label for centroids
)
plt.title("Clusters of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.show()


############# About print(y_kmeans) ############
# Interpretation:
# Data point [15, 39] (annual income 15, spending score 39) belongs to cluster 4.
# This cluster may be the “low annual income and moderate spending propensity” group.
# Data point [15, 81] (annual income 15, spending score 81) belongs to cluster 2.
# This cluster may be the “low income and high propensity to spend” group...

# Cluster 0:
# People with high annual incomes and low spending scores.
# Cluster 1: People with high annual income and high spending scores.
# People with high annual incomes and high spending scores.
# Cluster 2: Low annual income, high spending scores.
# Low annual income, high spending scores.
# Cluster 3: People with
# Medium annual income, average spending score.
# Cluster 4: People with
# Low annual income, low spending scores.
