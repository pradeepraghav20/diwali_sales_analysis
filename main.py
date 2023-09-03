import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv(r'C:\Users\prade\OneDrive\Desktop\pandas_project\diwali_sales\data.csv',encoding='unicode_escape')
# print(df.head(10))
df.drop(['Status','unnamed1'],axis=1,inplace=True)


print(df.describe())
print(df.info())


print(df.isnull().sum())
print(df.shape) 
print(df.head(10))

# count the null value 
print (df.isnull().sum())
print(df)


# droping null value
df.dropna(inplace=True)
print (df.isnull().sum())

# change the data type of column

df['Amount']=df['Amount'].astype('int32')
# print(df['Amount'].dtype)

print(df.columns)
df.rename(columns={'Marital_Status':'Shhadi'},inplace=True)
print(df)

gb=df.groupby('State').agg({"Age":'count'})
print(gb)

plt.pie(gb,autopct="%1.2f %%")
plt.show()


# Gender Count
ax=sns.countplot(x='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)

ax=sns.countplot(x = 'Age Group', hue = 'Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)

plt.show()


gensales=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount' ,data = gensales)

agegroup_sales=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = agegroup_sales)

print(agegroup_sales)


state_data=df.groupby('State',as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False,).head(10)
sns.barplot(x='State',y='Amount',data=state_data)
plt.show()



sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
