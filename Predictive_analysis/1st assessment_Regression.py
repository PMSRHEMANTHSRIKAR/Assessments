# -*- coding: utf-8 -*-
"""Predictive_Analysis-1A.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19MGshppo_YEMrXoOYXZuh3XTUb4Oypqk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

df=pd.read_csv('/content/expenses.csv')
df

df.shape

df.duplicated().sum()

duplicated_rows = df[df.duplicated(keep=False)]
print(duplicated_rows)

df = df.drop_duplicates()

df.shape

df.isna().sum()

bmi_score=df['bmi'].mode()[0]
df['bmi']=df['bmi'].fillna(bmi_score)

df.isna().sum()

df.info()

df.describe()

for i in df.select_dtypes(include=['float64','int64']):
  df[i].value_counts().plot(kind='bar')
  plt.xlabel(i)
  plt.ylabel('Frequency')
  plt.title(f'Bar chart of {i}')
  plt.show()

  #no outliers

for i in df.select_dtypes(include='object'):
  df[i].value_counts().plot(kind='bar')
  plt.xlabel(i)
  plt.ylabel('Frequency')
  plt.title(f'Bar chart of {i}')
  plt.show()

le=LabelEncoder()
for i in df.select_dtypes(include='object').columns:
  df[i]=le.fit_transform(df[i])

df

X = df.drop('charges',axis=1)
y=df['charges']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

scaler= StandardScaler()
X_train_scaled=scaler.fit_transform(X_train)
X_test_scaled=scaler.transform(X_test)

lin_reg=LinearRegression()
model = LinearRegression()
model.fit(X_train_scaled,y_train)
y_pred=model.predict(X_test_scaled)

r2score=r2_score(y_test,y_pred)
print(f'R2 score is{r2score}')
mse=mean_squared_error(y_test,y_pred)
print(f'Mean squared error is {mse}')
