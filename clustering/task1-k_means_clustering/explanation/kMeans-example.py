import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Small toy dataset
X = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])
# Visualize the toy dataset
plt.scatter(X[:, 0], X[:, 1], s=100, c="blue")
plt.title("Toy Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()


# Number of clusters
k = 2
# Applying K-Means
kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
centroids = kmeans.cluster_centers_
# Visualize clusters and centroids
for i in range(k):
    plt.scatter(X[y_kmeans == i, 0], X[y_kmeans == i, 1], s=100, label=f"Cluster {i+1}")
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c="yellow", label="Centroids")
plt.title("K-Means Clustering on Toy Dataset")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
print("Cluster Centroids:\n", centroids)


# Elbow Method: Determine the optimal number of clusters
wcss = []  # Within-Cluster Sum of Squares
max_clusters = len(X)  # Maximum possible clusters = number of samples
for i in range(1, max_clusters + 1):  # Iterate only up to the number of samples
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, max_clusters + 1), wcss, marker="o")
plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# When k=1, all points are included in one cluster, so the variation is maximal.
# As (k) increases, the variation (WCSS) decreases because the clusters are subdivided.
# However, beyond a certain point (elbow point), the WCSS decreases less as the number of clusters is increased.
# The graph of the elbow method shows an “elbow point” where the decrease in WCSS is drastically less when k=2.
# From this we can conclude that it is appropriate to divide the data into two clusters.
