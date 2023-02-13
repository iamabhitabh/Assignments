#!/usr/bin/env python
# coding: utf-8

# In[6]:


#question 1
x = int(input())
if x >90:
    print('Grade A')
elif x> 80 and x <= 90:
    print('Grade B')
elif x>= 60 and x <= 80:
    print('Grade C')
else: print('Grade D')


# In[27]:


#question 2
price = int(input())
if price <=50000:
    tax = 0.05*price
elif price > 50000 and price <= 100000:
    tax = .1*price
else:
    tax = 0.15* price
print("Pay rs {} as tax ".format(tax) )


# In[1]:


#question 3
city = input()
if city == 'Delhi':
    print ('Red Fort')
if city == 'Agra':
    print('Taj Mahal')
if city == 'Jaipur':
    print('Jal Mahal')


# In[7]:


#question 4
number = int(input())
n = 0
while number >10:
    if (number /3 - number //3) ==0:
        n = n+1
        number = number /3
    else:
        break
print(n)
    


# In[23]:


#Question 6
n=1
x = int(input())
for i in range(1,x,2):
    str = ((x-i)//2)*" " + i*'*' +((x-i)//2)*" "
    print(str)
        

    


# In[51]:


#question 7
x = 10
for i in range(x,0,-1):
    print (i)


# In[ ]:




