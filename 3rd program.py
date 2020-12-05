#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3. Remove duplicate from a list and create a tuple and find the minimum and maximum number
samplelist=[87,45,41,65,94,41,99,94]
list1=[]
for x in samplelist:
    if(x in list1):
        x
    else:
        list1.append(x)
print("unique items" ,list1)
print("tuple",tuple(list1))
print("min",min(list1))
print("max",max(list1))


# In[ ]:




