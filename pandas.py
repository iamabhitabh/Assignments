#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[15]:


#solution1
a = {'data': (4,8,15,16,32)}
a = pd.Series(a)


# In[16]:


#Solution2
b = [2,4,5,6,'er',34,78,89,'name','date']
b = pd.Series(b)
print(b)


# In[34]:


#Solution3
table = {'Name' : ('Alice', 'Bob', 'Claire'),'Age':(25,30,27),'Gender':('Female','Male','Female')}
table = pd.DataFrame(table)
table.set_index('Name')


# In[ ]:


"""
#Solution4
A data frame is a table or a data structure which is 2 dimensional having number of rows and columns where as a series is a one dimensional structure only having a single column.
"""


# In[1]:


"""
Solution5
common functions that can be used to manipulate data in a data frame are gorupby, sort, isnull etc. Groupby function is used to group the whole data set based on the values in a given column"""


# In[2]:


#Solution 6
Series and dataframe are mutable in nature.



#Solution7
a = pd.Series([1,3,5,7,9])
b = pd.Series([2,4,6,8,10])
c['even'] = pd.DataFrame(b)
c['odd'] = pd.DataFrame(a)


