# Day 3 - Pandas Basics

import pandas as pd

# Create sample dataset
data = {
    "Name": ["Amit", "Sakshi", "Rahul"],
    "Age": [22, 21, 23],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Basic info
print("\nShape:", df.shape)
print("\nColumns:", df.columns)

# Statistics
print("\nAverage Marks:", df["Marks"].mean())

# Filter data
high_marks = df[df["Marks"] > 80]
print("\nStudents with marks > 80:")
print(high_marks)
