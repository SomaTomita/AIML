import numpy as np

X = np.array([[1, 1], [1, 2], [2, 2], [4, 4]])


import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Simple dataset
X = np.array([[1, 1], [1, 2], [2, 2], [4, 4]])


# Compute the dendrogram using hierarchical clustering.
# sch.linkage performs hierarchical clustering using the Ward's method,
# which minimizes the increase in variance when merging clusters.
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()


from sklearn.cluster import AgglomerativeClustering

# Initialize the AgglomerativeClustering model to create 2 clusters.
# - n_clusters=2: The final number of clusters desired.
# - metric="euclidean": The distance metric used for clustering (Euclidean distance).
# - linkage="ward": Ward's linkage minimizes the variance increase when merging clusters.
hc = AgglomerativeClustering(n_clusters=2, metric="euclidean", linkage="ward")
y_hc = hc.fit_predict(X)
# Visualize the clusters
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c="red", label="Cluster 1")
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c="blue", label="Cluster 2")
plt.title("Clusters")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()


# K-nearest neighbor methods (e.g., K-means)** are more appropriate than **Hierarchical Clustering (Hierarchical Clustering)**
# when there is a large amount of data.

# - High computational cost: ** Hierarchical Clustering
#   Hierarchical clustering calculates the distance between data points one by one and builds a cluster structure for all data.
#   As the number of data points increases, the computational complexity increases to O(n²) or O(n³), where n is the number of data points.
#   This makes the computation very expensive and inefficient to execute on large data sets.
# - High memory usage:.
#   Memory consumption is huge because all distances need to be kept.
#   This can be a serious bottleneck when dealing with large amounts of data.
# - Number of static clusters:.
#   Once a cluster structure is created, new data points cannot be easily added.
#   This is inappropriate when dynamic updating of data is required
