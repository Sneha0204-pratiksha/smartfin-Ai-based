import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data/savings.csv')

# Preprocess data
features = data[['income', 'expenses']]
target = data['savings']

# Fit Linear Regression model
model = LinearRegression()
model.fit(features, target)

# Make predictions
predictions = model.predict(features)

# Plot results
plt.scatter(target, predictions)
plt.xlabel('Actual Savings')
plt.ylabel('Predicted Savings')
plt.title('Savings Optimization')
plt.show()
