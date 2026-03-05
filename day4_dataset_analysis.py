# Day 4 - Dataset Analysis

import pandas as pd

# Load dataset
df = pd.read_csv("iris.csv")

# Display first rows
print("First 5 rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Statistical summary
print("\nStatistics:")
print(df.describe())

# Species count
print("\nSpecies count:")
print(df["species"].value_counts())
