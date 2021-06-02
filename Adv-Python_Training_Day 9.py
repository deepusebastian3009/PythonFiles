#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Intro to DataFrames in Pandas:


# In[2]:


import pandas as pd


# In[3]:


import numpy as np


# In[ ]:





# In[ ]:





# In[ ]:


Datatypes in Pandas:
    
    1.Series
    2.Dataframes


# In[ ]:





# In[ ]:


A DataFrames is a 2D data structure...daa is alligned in the tabular fashion in rows and columns.


# In[ ]:


#General syntax

pandas.DataFrame(data,index,columns,dtype)


# In[ ]:





# In[ ]:


#creating the DataFrame:

A pandas DataFrame can be created by


# In[ ]:





# In[ ]:


How to create an empty dataframe


# In[4]:


df=pd.DataFrame()

print(df)


# In[ ]:


Creating a dataframe with a list:


# In[6]:


data=[1,2,3,4,5]


# In[8]:


df=pd.DataFrame(data)

print(df)


# In[ ]:





# In[9]:


data=[['gagan',9],['subhajit',8],['sumaiya',9],['afzal',6],['rishika',7]]


# In[10]:


df=pd.DataFrame(data)

print(df)


# In[11]:


df=pd.DataFrame(data,columns=['Name','Marks'])

print (df)


# In[13]:


df=pd.DataFrame(data,index=['Rank 1','Rank 2','Rank 3','Rank 4','Rank 5'],columns=['Name','Marks'])

print (df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




