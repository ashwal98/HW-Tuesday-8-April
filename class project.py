
import pandas as pd
import numpy as np

# code goes here
data = pd.read_csv("diabetes.csv")
print(data.head())
print(len(data.columns))
print(len(data))
print(data.isnull().sum())
print(data.describe())
data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)
print(data.isnull().sum())
print(data[data.isnull().any(axis=1)])
print(data.dtypes)
print(data.Outcome.unique())
data['Outcome'] = data['Outcome'].replace('O', 0)
data['Outcome'] = data['Outcome'].astype('int64')
print(data.Outcome.unique())