#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Ovweview : Numpy : Numy is a numerical computation lirary used for all the numerical calculations and also for 
the scientific computation. It stands as a foundational library to all remaining libraries.

Numpy stands fr numerical python==num -py.

We can also perform the statistical computing by using the numpy.

Data type of Numpy: Numpy is having a datatype  called as an ndarray.
    
Overview of Ndaaray-----    num of dimesions array.......


        


# In[ ]:


Array is similar like a list.

get_ipython().set_next_input('What is the diff between array and list');get_ipython().run_line_magic('pinfo', 'list')

Array------Internal implementations and working is very efficient in a array compared to list.


# In[ ]:





# In[ ]:


#how to install numpy


# In[4]:


get_ipython().system('pip install numpy')


# In[ ]:





# In[ ]:


import numpy as np


# In[ ]:


1. Create an array from a regular Python list or tuple using the array function


# In[5]:


array_one=np.array([1,2,3,4])
array_one


# In[7]:


numbers=[9,8,7,6]
array_two=np.array(numbers)
array_two


# In[ ]:


#to confirm and validate the datatype.......


# In[8]:


type(array_two)


# In[ ]:


2. Numpy offers several functions to create arrays with initial placeholder content


# In[ ]:


Note: Internal implementation of an array is float(decimal numbers)


# In[ ]:


Create an array of zeroes with desired shape(X,Y)

X==number of rows
y==number of columns


# In[9]:


array_of_zeroes=np.zeros((3,4))
array_of_zeroes


# In[ ]:


Use dtype in order to specify the datatype


# In[10]:


array_of_ones_int=np.ones((3,4)),dtype=np.int16
array_of_ones_int


# In[ ]:


np.eye() creates an eyeidentity matrix


# In[11]:


array_eye=np.eye(5)
array_eye


# In[ ]:


3.To create sequences of numbers,NumPy provides a function analogous to range that returns arrays instead of lists


# In[ ]:


arange(start,stop,step,dtype)


# In[12]:


array_of_evens=np.arange(2,20,2)
array_of_evens


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




