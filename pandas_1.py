#!/usr/bin/env python
# coding: utf-8

# In[82]:


import pandas as pd


# In[104]:


#Solution2
x = pd.DataFrame({'a':(2,3,4,5,6), 'b':(1,3,5,7,9), 'c':(23,34,36,77,56)})
lst = []
for i in range(0,len(x)):
    lst.append(2*i+1)
x['index'] = pd.DataFrame(lst)
x.set_index('index')
    


# In[107]:


#Solution3
n = int(input('enter the number of values in value column '))
lst = []
for i in range(0,n):
    lst.append(int(input('enter a value')))
df['values'] = pd.DataFrame(lst)
df_sum = df['values'][0:3].sum()
print(df_sum)


# In[165]:


#Solution4
f = pd.DataFrame()
f['Text'] = pd.DataFrame(['tr','eregr','eferftergv', 'New word'])
wordcount = lambda x:len(x.split())
f['word_count'] = f['Text'].apply(wordcount)


# In[168]:


"""
#Solution5
DataFrame.size tells about the total number of elements in the table
DataFrame.shape tells about the dimension of the matrix or the number of rows,columns in the table
"""


# In[169]:


"""
Solution6
df = pd.read_excel('file_path') #is used to read excel file
"""


# In[182]:


#Solution7
def username(x):
    lst = x.split('@')
    return lst[0]
dataframe['username'] = dataframe['email'].apply(username)


# In[205]:


#Solution8
z = {'a':(3,8,6,2,9),'b':(5,2,9,3,7),'c':(1,7,4,5,2)}
data = pd.DataFrame(z)
df = data[(data['a']>5) & (data['b']<10)]
df


# In[221]:


#Solution9
def eda(x):
    return (print('mean:',x.mean(),'meadian:',x.median(), 'st deviation:',x.std()))
eda(df['values'])


# In[ ]:


#Solution10
data['MovingAverage'] = data['sales'].rolling(7).mean()
data


# In[232]:


#Solution11
from datetime import datetime
def weekdaY(x):
    dt = datetime.strptime(x, '%Y-%m-%d')
    weekday = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return weekday[dt.weekday()]
df['Weekdday'] = df['Date'].apply(weekdaY)


# In[ ]:


#Solution12
def date_parse(x):
    dt = datetime.strptime(x, '%Y-%m-%d')
    return dt.date()
df['date'] = df['date'].apply(date_parse)
df[(df['date']>datetime.strptime('2023-01-01', '%Y-%m-%d')) & (df['date']<>datetime.strptime('2023-01-31', '%Y-%m-%d')) ]


# In[277]:


#Solution 13
#Most important library to use pandas is pandas. it can be imported as shown in the first line of the document.
import pandas as pd


# In[ ]:




