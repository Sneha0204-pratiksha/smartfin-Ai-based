import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/transactions.csv')

# Preprocess data
features = data[['amount', 'category']]

# Fit Isolation Forest model
model = IsolationForest(contamination=0.01)
data['anomaly'] = model.fit_predict(features)

# Plot results
anomalies = data[data['anomaly'] == -1]
plt.scatter(data.index, data['amount'], label='Normal')
plt.scatter(anomalies.index, anomalies['amount'], color='red', label='Anomaly')
plt.legend()
plt.show()
