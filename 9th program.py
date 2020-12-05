#!/usr/bin/env python
# coding: utf-8

# In[1]:


#9. Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.
x=input("enter string ")
count=0
count1=0
for i in range(len(x)):
    if((x[i].islower())==True):
        count+=1
    elif((x[i].isupper())==True):
        count1+=1
print("No. of Uppercase characters :",count)
print("No. of Lowercase Characters :",count1)


# In[ ]:




