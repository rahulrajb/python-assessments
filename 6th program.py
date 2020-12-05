#!/usr/bin/env python
# coding: utf-8

# In[5]:


#6. write a recurssive function to print the fibonacci series of n numbers
def calculatesum(num):
    if num:
        return num + calculatesum(num-1)
    else:
        return 0

res = calculatesum(10)
print(res)


# In[ ]:




