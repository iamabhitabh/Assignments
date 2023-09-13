#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Solution1
The exception in python are a way of handling errors when occured in a program. The exceptios are provided so that the program doesnt stop working even if an error is thrown by the compiler.
The difference between an syntax error and an exception is syntax eror occur when there is a mistake in the script of a programme.
If the syntax of the programme is correct but there is some error in the logic or other operation because of some other reason we dont want to stop next steps of program to work so we provide exceptions to those errors"""


# In[2]:


'''
Solution2
Handleing exceptions are a way of telling the compiler an alternative route or the remedies to perform if an error occurs while performing an operation.
If the exceptions are not handeled it will cause the progrrame to not perform functions properly and may even lead to stopping of the programe abruptly.'''


# In[6]:


'''
Solution3
Try and except statements are used to handle exceptions '''
#example
lst = [1,3,5,6,7,8,9]
try:
    for i in range(0,8):
        print(lst[i]**2)
except:
    print('Index out of range')


# In[25]:


"""
Solution4
try and else: This method is used when the try block runs succesfully.
finally: This method is used to execute a script at the end, irrespective of the success of the try function.
raise: this method is used to raise error  manually. 
raise is used to let the compiler know that for the given programme we want a specific error to be raise if a given condition is satisfied.
"""
a = int(input())
try:
    x = (12/a) - (12//a)
except:
    print('a cannnot be Zero')
else:
    print(f'Remainder is {x}')#Example Try and else
finally:
    print("The programe is executed")#Example finally
            #Example of raise
class firstletter(Exception):
    pass
def setname(a):
    if a[0].isupper() == False:
        raise firstletter("First letter must be capital")
    else:
        return print(f'Username is:{a}')
try:
    username = input('Please enter a user name:')
    setname(username)
except firstletter as e:
    print(e)


# In[27]:


"""
Solution5
Custom exceptions are used handle specific conditions which we dont want to exist in the programme.
If we want to raise an error when a specific condition is met and that error doesnt already exist we might to create a custom error to handle that situation"
Example: to raise and error if the password needs to have atleast 1 number and 1 special word and we want to raise an error if user entered a password not satifying the conditions
"""


# In[29]:


"""
Solution6
"""
class firstletter(Exception):
    pass
def setname(a):
    if a[0].isupper() == False:
        raise firstletter("First letter must be capital")
    else:
        return print(f'Username is:{a}')
try:
    username = input('Please enter a user name:')
    setname(username)
except firstletter as e:
    print(e)


# In[ ]:




