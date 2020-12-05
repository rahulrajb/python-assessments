#!/usr/bin/env python
# coding: utf-8

# In[4]:


#5. Create an inner function to calculate the addition in the following way ● Create an outer function that will accept two parameters a and b ● Create an inner function inside an outer function that will calculatethe addition of a and b ● At last, an outer function will add 5 into addition and return it
def ad1(a,b):
    a1=a
    b1=b
    def ad2(a1,b1):
        return a1+b1
    add=ad2(a1,b1)
    return add
ad1(3,4)


# In[ ]:




