#!/usr/bin/env python
# coding: utf-8

# In[ ]:


np.eye() creates an eyedentity matrix


# In[1]:


array_eye=np.eye(5)  #5*5 matrix
array_eye


# In[ ]:


3. To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of list

arange(start,stop,step,dtype)


# In[2]:


array_of_evens=np.arange(2,20,2)
array_of_evens


# In[ ]:


Note:Last value is always exclusive


# In[ ]:


It also acceots float arguments


# In[3]:


array_of_floats=np.arange(0,2,0.3)
array_of_floats


# In[ ]:





# In[ ]:


Two Dimensional Arrays


# In[ ]:





# In[4]:


array_2d=np.array([(2,4,6),(3,5,7)])
array_2d


# In[5]:


array_2d.shape


# In[ ]:





# In[ ]:


Using reshape to create n dimensional arrays


# In[6]:


np.arange(6)


# In[7]:


array_nd=np.arange(6).reshape(3,2)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




