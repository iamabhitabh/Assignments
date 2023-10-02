#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Solution1
Databases are the technology used to store and use the data for any software or a program. Databases allow the user to access the data and do the mainupulations on it for any required purposes
SQL databases are the Relational databses which stores data in for of rows and columns .NoSQL is not only sql databases which are not relational in nature. it can also store data in form of sound video etc which doesn't neccesarily have tables"""


# In[2]:


"""
Solution2
DDL is Data definition language which is used to define, modify and manage the data in database
Create is used to create a new database as well as new table.
Alter is used to modify the existing database/ tables by adding or removing the columns
Drop is used to delete a table or contents from the table
Truncate is used to remove all the records from the table while keeping the structure intact"""


# In[4]:


"""
DML is used to manipulate data in the databsaes it is used to insert, update and delete the values in the databases
Insert is used to add a new record to the table. (a new row)
ex: Insert into table_name(column1,column2....)
values(vlaue_c1,value_c2...)
#the above syntax will insert value_c1 at column1 and so on.
update statement is used to update existing rows with another value.
example: 
update table table_name
set col_1 = val_1 where col_2 = x;
#the above syntaxt will change the value of col_1 to val_1 in all the rows where value of col_2 is x
delete is used to delete the rows from the table based on a given condtion.
example: 
delete from table_1
wehre col_name = x
# The above syntax will delete all the rows from the table in which value of col_name is equal to x
  """


# In[5]:


"""
Primary key is a column in a table which is used as an identifier in the table. The values in a primary key cannot be null or duplicate. 
A foreign key is a column in a table which is primary key in someother table, it is used to link both of the tables. """


# In[5]:


#solution5 
get_ipython().system('pip install PyMySQL')
import pymysql
database = pymysql.connect(host = 'local_host_name',user = 'root', password = '*********') (#i am not giving the ip of my local host)
#cursor is used to bring the pointer in a place wehre query can be written and executed
cursor = database.cursor()
# execute is used in side cursor to execute a query in the database
cursor.execute('create database if not exists database_1 create table if not exist db_tb_1')
# i am using PyMySQL because mysql.connector was not workig with my jupyter notebook


# In[6]:


#Solution6
database = pymysql.connect(host = 'local_host_name',user = 'root', password = '*********') (#i am not giving the ip of my local host)
cursor.execute('create table student(roll_no int primary key, name varchar(50), marks float (50), grade float, city varchar(50));
insert into student values (123,'Abhitabh',762,8.25,'Bhilai'),(124, 'Ali',600,8.5,'Patan');
select name from student where city = 'Bhilai'' )
#the above syntax will give the output 'Abhitabh'


# In[ ]:




