#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Iterating


# In[ ]:


import numpy as np


# In[ ]:





# In[ ]:


1D Arrays


# In[ ]:


a=np.arange(11)**2


# In[2]:


a


# In[3]:


for i in a:
    print(i**(1/2))


# In[ ]:


Multi Dimensional Arrays


# In[ ]:


Iterating over multidimensional arrays is done with respect to the first axis:


# In[ ]:


students=np.array([['Alice','Beth', 'Cathy', 'Dorothy'],
                  [65,78,90,81],
                   [71,82,79,92]])


# In[ ]:


Fortan order flattening

To flatten a 2D array column wise, use the Fortan order


# In[4]:


for element in students.flatten(order='F'):      #column based iteration
    print element


# In[ ]:


nditer

Efficient multi dimensional iterator object to iterate over arrays


# In[6]:


x=np.arange(12).reshape(3,4)


# In[ ]:


Fortan Order


# In[ ]:


This is like iterating over an array which has been flattened column wise


# In[12]:


for i in np.nditer(x,order='F'):
       print(i)


# In[ ]:





# In[ ]:


Flags

There are a number of flags which we can pass a list to nditer. Many of these involve setting buffering options 
If we want iterate over each column we can use the flag argument with value 'external_loop'


# In[13]:


for i in np.nditer(x,order='F',flags=['external loop']):
    print i


# In[ ]:


Modifying Array Values

By default the nditer treats the input array as a read only object. To modify the array elements, you mustspecify either read-write or write-only mode. This 
controlled with per operand flags.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




