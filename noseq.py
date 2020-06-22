#!/usr/bin/env python
# coding: utf-8

# In[13]:


def most_frequent(b):
    rep={}
    for i in b:
        if i in rep:
            rep[i]+=1
        else:
            rep[i]=1
            

    list1=list(rep.items())
    list1.sort(reverse=True)
    print(list1)
    rep1=dict(list1)
    print(rep1)
    
x=str(input("please enter a string:"))
most_frequent(x)


# In[ ]:





# In[ ]:




