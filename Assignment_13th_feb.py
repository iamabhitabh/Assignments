#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Solution1
While creating a custom class we need the exception class as well because, for the errors we are not providing the exception we need to raise error which already exist in the exception class"""


# In[33]:


"""
Solution2: I can try callinng the subclasses through a function and then calling that function again inside the funciton and provding the exception if the subclasses doesnt exist.
"""
def subclasses(E):
    print(E)
    for i in E.__subclasses__():
        print (i)
        try:
            subclasses(i.__subclasses__())
        except:
            pass
subclasses(Exception)


# In[34]:


"""
Solution3
Airthematic error class has errors which occurs during a mathematical operation. for example: floating point error when result is an imaginary number or divison by zero when result is infinity"""


# In[35]:


"""
Solution4
Lookup error are cause when the compiler or the interprestor tries to access a location but nothing is found at that location or that location doesnt exist.
Key error is a type of lookup error when the key is present in the given dictionary so the variable cannt be accessed.
Index error: This error occurs when an index is not present in an ordered iterable and that index is called.
"""


# In[36]:


"""
Solution5
Import error occurs when you try to use a library or a framework which is not present for you in the workspace it. Module not found error occurs when you try to import a module but it is not installed in the system or the IDE"""


# In[37]:


"""
Solution6
Specific exceptions must be used
Errors must be logged
Error Message should be valid
Multiple exceptions handleing must not be used for same type of error
RAM must be cleared 
All the exceptions handelled must be documented
"""


# In[ ]:




