# -*- coding: utf-8 -*-
"""Churn_Modelling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YXK3GTBfIEIajFP6W2QGsd3Jwkw7uqhj
"""

## import required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

path = "/content/drive/MyDrive/Churn_Modelling.csv"
df = pd.read_csv(path)

#load the dataset

df.head()

df.shape

df.info()

df.isnull().any()

df.describe()

df.Gender.value_counts()

df.Age.value_counts()

df.Balance.value_counts()

sns.displot(df.Gender)

sns.displot(df.Balance)

sns.lineplot(df.Age,df.CreditScore)

sns.lineplot(df.Gender,df.Tenure)

"""# **Univariate** **Analysis**"""

sns.distplot(df.EstimatedSalary) #numeric
sns.boxplot(df.EstimatedSalary) # numeric
sns.distplot(df.NumOfProducts)
sns.countplot(df.CreditScore) # categorical
sns.countplot(df.Exited)

# Bivariate Analysis

path = "/content/drive/MyDrive/Churn_Modelling.csv"
df = pd.read_csv(path)
sns.jointplot('EstimatedSalary', 'NumOfProducts', data = df, kind='scatter') #numeric
sns.lmplot(df.EstimatedSalary, df.NumOfProducts, data=df, hue='Balance', fit_reg=False) #numeric
sns.countplot('CreditScore', hue = 'Balance', data=df) #categorial

df.hist(figsize=(8,8))

## Multivariate analysis

sns.pairplot(df)

display(df, df.describe())

pd.set_option('max_colwidth',256)
pd.set_option('display.max_rows',10000)
pd.set_option('display.max_columns',10000)

sns.boxplot(df.CreditScore)

df.describe()

df.median()

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
outliers=[]
def detect_outliers(data):
  threshold=3
  mean=np.mean(data)
  std=np.std(data)
  for i in data:
    z_score=(i-mean)/std
    if np.abs(z_score)>threshold:
      outliers.append(y)
  return outliers   
  outlier_pt=detect_outliers(dataset)
  outlier_pt

import pandas as pd
s = pd.Series(list('gender'))
pd.get_dummies(s)

import pandas as pd
        
df = pd.DataFrame({
          'A':['a','b','a'],
          'B':['b','a','c']
        })
df

# Get one hot encoding of columns B

one_hot = pd.get_dummies(df['B'])

# Drop column B as it is now encoded

df = df.drop('B',axis = 1)

# Join the encoded df

df = df.join(one_hot)
df

import pandas as pd

path = "/content/drive/MyDrive/Churn_Modelling.csv"
df = pd.read_csv(path)
df.head()
df_tips=pd.get_dummies(df)
df_tips

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
path = "/content/drive/MyDrive/Churn_Modelling.csv"
df = pd.read_csv(path)
x=df.iloc[:,1:5]
y=df.iloc[:,5]
print(df.describe())

path = "/content/drive/MyDrive/Churn_Modelling.csv"
df = pd.read_csv(path)
x=df.iloc[:,1:14]
print(df.describe())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=1)

x_train.shape

y_train.shape

x_test.shape

y_test.shape