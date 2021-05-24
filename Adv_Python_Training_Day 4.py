#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Printing Arrays


# In[1]:


import numpy as np


# In[ ]:


1D array


# In[14]:


a=np.arange(6)


# In[15]:


print(a)


# In[ ]:


2D array


# In[22]:


l=np.arange(24).reshape(2,3,4)


# In[23]:


print(l)


# In[ ]:





# In[ ]:


3D array


# In[9]:


c=np.arange(24).reshape(2,3,4)


# In[10]:


print(c)


# In[ ]:


np.set_printoptions(threshold=np.nan)


# In[24]:


print(np.arange(10000).reshape(100,100))


# In[ ]:


Arithmetic Operations on Array


# In[ ]:


If the dimensions of 2 arrays are disimilar, we can't perform operations. However NumPy allows it


# In[33]:


c=np.array([10,10,10])
d=np.array([5,5,5])


# In[34]:


c+d


# In[36]:


c/d


# In[37]:


c%3


# In[39]:


c<35


# In[41]:


c>25


# In[42]:


c**2


# In[ ]:


dot function or method


# In[43]:


A=np.array([[1,1],[0,1]])
B=np.array([[2,0],[3,4]])

print('A:\n',A)
print('B:\n',B)


# In[44]:


A*B     #This gives element wise multiplication


# In[45]:


A.dot(B)    #This gives the matrix multiplication


# In[46]:


np.dot(A,B)


# In[ ]:


Modifying an existing array rather than creating a new one


# In[47]:


a*=3
a


# In[ ]:


Unary Operators


# In[ ]:


c=np.array[12,15,18,20]


# In[52]:


c.sum()


# In[55]:


c.min()


# In[56]:


c.max()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




