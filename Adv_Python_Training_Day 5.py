#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Universal Functions

NumPy provides standard trignometric functions, functions for arithmetic operations,
handlin complex numbers, statistical functions. In NumPy, these are called Universal Functions.


# In[8]:


import numpy as np


# In[ ]:





# In[ ]:


Trignometric Functions


# In[ ]:


angles=np.array[0,30,45,60,90]


# In[ ]:


Angles need to be converted to radians


# In[9]:


angles_radians=np.radians(angles)
angles_radians


# In[4]:


print('Sine of the angles in the array:')
print(np.sin(angles_radians))


# In[ ]:





# In[10]:


arcsin, arcos and arctan functions return the trignometric inverse of sin, cos and tan of the given angle.


# In[11]:


sin=np.sin(angles*np.pi/180)
print('Compute sine inverse of angles. Reurned values are in radians.')

inv=np.arcsin(np)
print(inv)


# In[ ]:





# In[ ]:


Statistical Functions


# In[ ]:


test_scores=np.array([32.32,56.98,21.52,44.32,55.63,43.47,43,34])


# In[15]:


print('Mean test scores of students:')
print(np.mean(test_scores))


# In[ ]:





# In[13]:


salaries=np.genfromtxt('data/salary.csv',delimiter='')


# In[16]:


salaries


# In[17]:


salaries.shape


# In[ ]:


mean=np.mean(salaries)
median=np.median(salaries)
sd=np.sd(salaries)
variance=np.var(salaries)


# In[18]:


print('Mean=%i' %mean)
print('Median=%i' %median)
print('Standard Deviation=%i' %sd)
print('Variance=%i' %variance)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




