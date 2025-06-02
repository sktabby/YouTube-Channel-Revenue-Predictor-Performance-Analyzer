# main.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

warnings.filterwarnings('ignore')

file_path = r'C:\Users\AQSA SHAH\OneDrive\Desktop\UM- Youtube Income Analysis\data\youtube_channel_real_performance_analytics.csv'
data = pd.read_csv(file_path)
print("\n Data loaded successfully!")

print("\n🧹 Data Cleaning and Preprocessing...")

data.dropna(inplace=True)


data['Video Publish Time'] = pd.to_datetime(data['Video Publish Time'])

print("\n Available columns in the dataset:")
print(data.columns.tolist())


print("\n Creating New Features...")


data['Revenue per View'] = data.apply(lambda row: row['Estimated Revenue (USD)'] / row['Views'] if row['Views'] > 0 else 0, axis=1)

# Engagement Rate: (Likes + Shares + New Comments) / Views * 100
data['Engagement Rate'] = data.apply(
    lambda row: (row['Likes'] + row['Shares'] + row['New Comments']) / row['Views'] * 100 if row['Views'] > 0 else 0,
    axis=1
)


print("\n Running EDA and saving plots...")

os.makedirs('outputs/plots', exist_ok=True)

# Revenue Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Estimated Revenue (USD)'], bins=50, kde=True, color='green')
plt.title("Revenue Distribution")
plt.savefig('outputs/plots/revenue_distribution.png')
plt.close()

# Revenue vs Views
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Views', y='Estimated Revenue (USD)', data=data)
plt.title("Revenue vs Views")
plt.savefig('outputs/plots/revenue_vs_views.png')
plt.close()

# Correlation Heatmap
plt.figure(figsize=(12, 8))
numeric_cols = data.select_dtypes(include=[np.number])
sns.heatmap(numeric_cols.corr(), annot=False, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig('outputs/plots/correlation_heatmap.png')
plt.close()

print(" Plots saved in 'outputs/plots/' folder.")


print("\n Training Random Forest Model...")


features = ['Views', 'Subscribers', 'Likes', 'Shares', 'New Comments', 'Engagement Rate']
X = data[features]
y = data['Estimated Revenue (USD)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n Model Performance:")
print(f" - Mean Squared Error: {mse:.2f}")
print(f" - R-squared Score: {r2:.2f}")


importances = model.feature_importances_
importance_df = pd.DataFrame({'Feature': features, 'Importance': importances}).sort_values(by='Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=importance_df)
plt.title("Feature Importance")
plt.savefig('outputs/plots/feature_importance.png')
plt.close()

print(" Feature importance plot saved.")


os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/youtube_revenue_predictor.pkl')
print("\n Model saved as 'models/youtube_revenue_predictor.pkl'.")


top_drivers = importance_df.head(3)['Feature'].tolist()
print(f"\n Key Revenue Drivers: {', '.join(top_drivers)}")

print("\n Analysis complete! Check the 'outputs/plots' folder for visuals.")
