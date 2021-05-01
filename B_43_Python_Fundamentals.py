#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to Python Functions


# In[ ]:


Overview : We have to use the keyword called def
We have to use small case letters for naming the functions.    


# In[ ]:





# In[ ]:


#req:Create a greet function


# In[ ]:


#defining or declaring the function

def greet():    #funname  
""creating a function to greet"" #doc strings----commenting inside te function
print("hello!")


# In[ ]:





# In[11]:


greet()  #calling the function or function call


# In[ ]:


#code -reusability


# In[ ]:





# In[ ]:


#enhancement of the requirement


# In[ ]:


#req: Write a function to greet the user..!


# In[ ]:





# In[21]:


def greetuser(username)
""creating the function to greet the user""
print(f"Hello, {username}")


# In[9]:


greetuser('Sunitha')#during the fun call-----arguments passing


# In[10]:


greetuser('Naveen')#argument passing


# In[12]:


greetuser('Kubra')#argument passing------runtime arguments passing..!


# In[ ]:





# In[ ]:


#Types of arguments:


# In[ ]:





# In[13]:


#req:Create a describe_pet function and consider the below parameters:

#1. animal_type
#2. pet_name


# In[ ]:





# In[ ]:


#defined a function and given the params, args

def describe_pet(animal_type,pet_name):
    ""creating a function for capturing the details of a pet""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")


# In[14]:


describe_pet('dog','Bruno')


# In[ ]:


#1. Positional Arguments....by default function will be accepting arguments in the order of the param defined. 


# In[ ]:





# In[15]:


describe_pet(pet_name='rex',animal_type='dog')


# In[ ]:


#2.Keyword Arguments....!


# In[20]:


describe_pet('Sheru')


# In[ ]:


#3. Default Arguments....!----dog


# In[ ]:


Keep the deafualt arguments at the end of the function


# In[22]:


def describe_pet(pet_name,animal_type='dog'):
    ""creating a function for capturing the details of a pet""
    print(f"I have a {animal_type}")
    print(f"My {animal_type} 's name is {pet_name}")


# In[23]:


describe_pet('Sheru')


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




