import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv(r'C:\Users\prade\OneDrive\Desktop\pandas_project\diwali_sales\data.csv',encoding='unicode_escape')
# print(df.head(10))
df.drop(['Status','unnamed1'],axis=1,inplace=True)
# print(df.describe())
# print(df.info())
# print(df.isnull().sum())
# print(df.shape) 
print(df.head(10))
# print (df.isnull().sum()
print(df)




