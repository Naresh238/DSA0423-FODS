from sklearn.cluster import KMeans
import numpy as np

data = np.array([[100,5],[200,8],[50,2],[300,10]])

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

print(kmeans.labels_)
