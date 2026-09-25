import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sklearn

print("Python version check")
print("Scikit-learn version:", sklearn.__version__)

from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv(r"C:\Users\acer\Desktop\ML MAJOR PROJECT\Dataset\Hospital_Operations_Dataset.csv")

# First 5 rows
print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Select features
features = df[[
    "Age",
    "Severity_Level",
    "Length_of_Stay_Days",
    "Wait_Time_Minutes",
    "Treatment_Cost_USD"
]].copy()

# Convert Severity_Level to numbers
features["Severity_Level"] = features["Severity_Level"].map({
    "Low": 0,
    "Medium": 1,
    "High": 2
})

# Remove missing values
features = features.dropna()

print(features.head())

# Standardize
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

print("Shape:", scaled_features.shape)
print(scaled_features[:5])
from sklearn.cluster import KMeans

# Elbow Method
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42, n_init=10)
    kmeans.fit(scaled_features)
    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.figure(figsize=(8,5))
plt.plot(range(1,11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.grid(True)
plt.show()
# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(scaled_features)

# Add cluster labels
features["Cluster"] = clusters

# Display first 5 rows
print(features.head())
from sklearn.cluster import KMeans

# Final KMeans Model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
features["Cluster"] = kmeans.fit_predict(scaled_features)

# Display clustered data
print(features.head())
plt.figure(figsize=(8,6))
plt.scatter(
    features["Age"],
    features["Treatment_Cost_USD"],
    c=features["Cluster"],
    cmap="viridis"
)

plt.title("Hospital Resource Clusters")
plt.xlabel("Age")
plt.ylabel("Treatment Cost (USD)")
plt.colorbar(label="Cluster")
plt.show()