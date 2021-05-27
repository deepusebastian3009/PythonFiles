#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Shallow copying and Deep copying


# In[ ]:





# In[ ]:


get_ipython().set_next_input('What do you understand by shallow copying and deep copying');get_ipython().run_line_magic('pinfo', 'copying')


# In[ ]:


get_ipython().set_next_input('What is the difference between them');get_ipython().run_line_magic('pinfo', 'them')


# In[ ]:





# In[ ]:


View vs Copy

When the contents are physically stored in another location, it is called copy.

On the other hand, a diff view of the same memory content is provided


# In[ ]:


impoty numpy as np


# In[ ]:


fruits=np.array(["Apple","Orange","Mango","Grapes"])


# In[ ]:


We will create basket now as a view of fruits


# In[ ]:


basket_1=fruits.view()
basket_2=fruits.view()


# In[1]:


print(basket_1)
print(basket_2)


# In[ ]:





# In[ ]:





# In[3]:


print("Ids for the arrays are different")
print("Id for the fruit is")
print(id(fruits))
print("Id for the basket is")
print(id(basket_1))
print(id(basket_2))


# In[ ]:





# In[4]:


basket_1.base is fruits   #memory location


# In[ ]:





# In[ ]:


Change a few elements of basket. It chanes the elements of fruits

Here we assign a new value to the first element of baket_2. 
You might be astonished that the list of fruits has been automatically


# In[ ]:


basket_2[0]="Strawberry"


# In[5]:


basket_2


# In[6]:


fruits  #points to be noted


# In[7]:


basket_1 #It is also being affected


# In[ ]:





# In[ ]:


Change the entire elements of basket.It does not change fruits.


# In[ ]:





# In[ ]:


basket_1=np.array(["Peach","Pineapple","Banana","Orange"])


# In[8]:


basket_1


# In[9]:


fruits


# In[ ]:





# In[ ]:


IN THIS CASE A NEW MEMORY LOCATION HAS BEEN ALLOCATED FOR BASKET_1


# In[ ]:





# In[ ]:


Deep Copy

The copy[] method makes a complete copy of the array and its data and doen't share with the original array


# In[ ]:





# In[ ]:


import numpy as np


# In[ ]:


fruits=np.array(["Apple","Mango","Grapes","Orange"])


# In[ ]:


We now creates a deep copy of fruits


# In[ ]:


basket=fruits.copy()


# In[10]:


basket


# In[11]:


basket is fruits


# In[12]:


basket.base is fruits       # basket doen't share anything with fruits


# In[ ]:


Change contents or shape of basket. It doe not change the contents of fruits.


# In[ ]:


basket[0]="Strawberry"


# In[13]:


basket


# In[ ]:


array(["Strawberry", "Mango","Grapes","Watermelon"],dtype='<U10')


# In[14]:


fruits       #It is not being impacted


# In[ ]:





# In[15]:


basket.shape=2,2


# In[16]:


print("Shape of basket:")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




