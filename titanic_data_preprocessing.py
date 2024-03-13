# Importing the necessary libraries
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
df = pd.read_csv('titanic.csv', header=0)

# Identify the categorical data
cat = ['Sex','Embarked']

print(df)

print(df[cat])

# Implement an instance of the ColumnTransformer class
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), cat)], remainder='passthrough')

# Apply the fit_transform method on the instance of ColumnTransformer
x = ct.fit_transform(df)

# Convert the output into a NumPy array
x = np.array(x)
print(x)

# Use LabelEncoder to encode binary categorical data


# Print the updated matrix of features and the dependent variable vector

