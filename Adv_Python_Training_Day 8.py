#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to pandas:


# In[ ]:





# In[ ]:


#intall pandas


# In[2]:


get_ipython().system('pip install pandas')


# In[ ]:





# In[ ]:


Overview of pandas : It is a very hihly utilised library for doing all the data analysis operations.
    It is capable of handling all the file formats, data transformation and having quick and fast performance efficiency. 


# In[ ]:





# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[ ]:





# In[ ]:


Datatypes in Pandas :
    
    It offers two different dattypes:
        1. Series datatype-------single dimension data
        2. DataFrames------------two dimensional(represented in tabular form)


# In[ ]:





# In[ ]:


Introduction to Series Datatype:


# In[ ]:


Series is one-dimensional labelled array, capable of holding data aof any type.
The axis labels are collectively called index.


# In[ ]:





# In[ ]:


#General syntax of a series


# In[ ]:


pandas.Series(data,index,dtype)


# In[ ]:





# In[ ]:


A series can be created using various inputs like :
    1.Array
    2.Dict
    3.Scalar value or constant


# In[ ]:





# In[ ]:


#creating an empty Series:


# In[7]:


s=pd.Series()
print(s)


# In[6]:


type(s)


# In[ ]:


#creating a Series from ndarray


# In[10]:


data=np.array(['a','b','c','d','e'])

s=pd.Series(data)

print(s)         #labels or indices-------which will be printig the series


# In[11]:


type(s)


# In[ ]:


#giving custom indexes:


# In[13]:


data=np.array(['a','b','c','d','e'])


# In[15]:


s=pd.Series(data, index=[100,101,102,103,104])
print(s)


# In[ ]:





# In[ ]:


#creating a series from a dictionary:


# In[17]:


data={'a':0.,'b':1.,'c':2.,'d':3.,'e':4.}


# In[18]:


s=pd.Series(data)
print(s)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




