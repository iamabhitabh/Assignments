#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Solution1
Files can be opened using open function. ex = file = open("file name", 'r')
File can be opened in reading mode, writing mode, binaryread mode 
In read mode files can only be read, in writing mode file can be written and in binary read and write mode file can be read and write in binary characters like audion or video. """


# In[2]:


"""
Solution 2
If the exceptions are not handled properly the program will stop execution at the line where the error is thrown by the compiler as the python compiler works line by line.
example:
a = 10
b = int(input) # here the program will throw div by zero error if user input 0
print(f'the value of b is {b}') # this line wont be executed
so error handling is important for a program to continue"""


# In[6]:


#solution3
file = open('file.txt', 'w')
file.write('I want to become a Data Scientist')
file.close()
rd = open('file.txt', 'r')
rd.read()
rd.close()


# In[7]:


"""
Solution4
read(): This method is used to read and existing file
readlines():this method is used to create a list of all the lines in a file
readline(): This method is used to read fist line of the file"""


# In[8]:


"""
Solution5
With open statement is used togather so as to reudce the lines of code and automate the process of closing the file.
If the open statement is not used with with statement then the file has to be close saperatley and the coder might forget that.
Using with statement automates this process and makes the runnig of the programme more seamless"""


# In[19]:


"""
Solutoin6
Write function writes the text or string into a file but write lin function wrties a list element by element into a file
"""
#example of write function
string = 'cat,dog,horse,pig'
file = open('file.txt','w')
file.write(string)
file.close()
data = open('file.txt','r')
data.read()
#example of writelines function
lst = ['cat,','dog,','horse,','pig']
file = open('file.txt','w')
file.writelines(lst)
file.close()
data = open('file.txt','r')
data.read()


# In[ ]:




