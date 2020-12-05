#!/usr/bin/env python
# coding: utf-8

# In[2]:


#2. Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element
list=[11,45,8,11,23,45,23,45,89]
list1={}
for x in list:
    if(x in list1):
        list1[x]+=1
    else:
        list1[x]=1
print("printing count of each item:",list1)


# In[ ]:




