import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/budget.csv')

# Preprocess data
features = data[['income', 'expenses', 'savings']]

# Fit K-Means model
kmeans = KMeans(n_clusters=3)
kmeans.fit(features)

# Predict clusters
data['cluster'] = kmeans.predict(features)

# Plot results
plt.scatter(data['income'], data['expenses'], c=data['cluster'], cmap='viridis')
plt.xlabel('Income')
plt.ylabel('Expenses')
plt.title('Budget Clusters')
plt.show()
