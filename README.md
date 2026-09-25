# Smart Hospital Resource Clustering

## Major Project

### Submitted By
**Catherin Jesintha J**

**B.Sc. Computer Science**  
**St. Anne's Arts and Science College**

**Internship:** Corizo - Machine Learning with Python

## Abstract

This project groups hospital operational records into meaningful clusters using Machine Learning. The project uses the K-Means clustering algorithm implemented in Python. Hospital data such as Age, Severity Level, Length of Stay, Wait Time and Treatment Cost are processed and standardized before clustering.

## Introduction

Machine Learning can be used to analyze hospital operational data and discover patterns in records. This project demonstrates the use of unsupervised learning through K-Means clustering to identify groups of similar hospital records based on selected operational features.

## Objectives

- Analyze the hospital operations dataset.
- Perform data preprocessing and remove duplicate records.
- Convert Severity Level into numerical values.
- Standardize the selected features.
- Apply K-Means clustering.
- Use the Elbow Method to examine different numbers of clusters.
- Visualize the resulting hospital resource clusters.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Visual Studio Code

## Dataset

**Dataset:** `Hospital_Operations_Dataset.csv`

### Selected Features

- Age
- Severity_Level
- Length_of_Stay_Days
- Wait_Time_Minutes
- Treatment_Cost_USD

Severity Level is converted into numerical values:

- Low = 0
- Medium = 1
- High = 2

## Methodology

1. Load the hospital operations dataset.
2. Display the first five records and dataset information.
3. Check for missing values.
4. Remove duplicate records.
5. Select the required features.
6. Convert Severity Level into numerical values.
7. Remove missing values.
8. Standardize the features using StandardScaler.
9. Apply the Elbow Method for k values from 1 to 10.
10. Train the final K-Means model with 3 clusters.
11. Add cluster labels to the processed data.
12. Visualize the clusters.

## Machine Learning Algorithm

### K-Means Clustering

K-Means is an unsupervised Machine Learning algorithm used to divide data into groups based on similarity.

The final model in this project uses:

- Number of Clusters: 3
- Random State: 42
- Number of Initializations: 10

## Results

The project generates:

- Dataset preview
- Missing-value information
- Standardized feature data
- Elbow Method graph
- Clustered data with cluster labels
- Hospital Resource Clusters scatter plot

## Project Structure

```text
Smart-Hospital-Resource-Clustering/
│
├── Dataset/
│   └── Hospital_Operations_Dataset.csv
│
├── Python Code/
│   └── hospital_resource_clustering.py
│
├── Report/
│   └── Smart_Hospital_Resource_Clustering_Simple_Report.docx
│
├── Screenshot/
│   └── Project screenshots
│
└── ppt/
    └── Smart_Hospital_Resource_Clustering_Presentation.pptx
