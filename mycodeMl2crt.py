#!/usr/bin/env python
# coding: utf-8

# In[29]:


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 21:17:01 2021

@author: nagarathna
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import linear_model


# In[3]:



# loading the data from csv file to a Pandas DataFrame
insurance_dataset = pd.read_csv('insurance.csv')


# In[4]:



# first 5 rows of the dataframe
insurance_dataset.head()


# In[5]:


# number of rows and columns
insurance_dataset.shape


# In[6]:



# getting some informations about the dataset
insurance_dataset.info()


# In[7]:



# checking for missing values
insurance_dataset.isnull().sum()


# In[8]:



# statistical Measures of the dataset
insurance_dataset.describe()


# In[9]:



# distribution of age value
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['age'])
plt.title('Age Distribution')
plt.show()


# In[10]:




# Gender column
plt.figure(figsize=(6,6))
sns.countplot(x='sex', data=insurance_dataset)
plt.title('Sex Distribution')
plt.show()
insurance_dataset['sex'].value_counts()


# In[11]:



# bmi distribution
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['bmi'])
plt.title('BMI Distribution')
plt.show()


# In[12]:



# children column
plt.figure(figsize=(6,6))
sns.countplot(x='children', data=insurance_dataset)
plt.title('Children')
plt.show()
insurance_dataset['children'].value_counts()


# In[13]:



# smoker column
plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=insurance_dataset)
plt.title('smoker')
plt.show()
insurance_dataset['smoker'].value_counts()


# In[14]:



# region column
plt.figure(figsize=(6,6))
sns.countplot(x='region', data=insurance_dataset)
plt.title('region')
plt.show()
insurance_dataset['region'].value_counts()


# In[15]:



# distribution of charges value
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['charges'])
plt.title('Charges Distribution')
plt.show()


# In[16]:



# encoding sex column
insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)


# In[17]:



3 # encoding 'smoker' column
insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)


# In[18]:



# encoding 'region' column
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)
X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X.shape, X_train.shape, X_test.shape)


# In[51]:


mydata=insurance_dataset.head(5)
print(mydata)


# In[52]:


reg=linear_model.LinearRegression()
reg.fit(mydata[['age','sex','bmi','children','smoker','region']],mydata.charges)


# In[53]:


reg.coef_


# In[54]:


reg.intercept_


# In[55]:


reg.predict([[18,0,33.770,1,1,0]])


# In[ ]:


#y=m1x1+m2x2+m3x3+b

#m1,m2,m3 are coeffient
#b is intercept
#x1,x2,x3 are independent varible


# In[60]:


#print((-378.3129839*18+879.31986567*0+-2995.2920476*33.770+2100.33233118*1-879.31986567*1-1702.98703565*0)+108465.18599200742)


# In[ ]:





# In[ ]:





# In[ ]:




