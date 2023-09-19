#!/usr/bin/env python
# coding: utf-8

# In[28]:


#solution1 
class vehicle:
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
    def distance_potential(self,petrol):
        return (self.average_of_vehicle * petrol)


# In[33]:


#solution2
class car_1(car):
    def seating_capacity(self,seating_capacity):
        return self.name_of_vehicle, seating_capacity


# In[31]:


"""
solution3
Multiple inheritance is when a class inherits the property of multiple classes including the parameters and the methods"""
#example
class road:
    def __init__(self,fuel_type):
        self.fuel_type = fuel_type

class car(vehicle,road):
    def __init__(self,name_of_vehicle,max_speed,average_of_vehicle,fuel_type):
        vehicle.__init__(self,name_of_vehicle,max_speed,average_of_vehicle)
        road.__init__(self,fuel_type)


# In[58]:


"""
Solution4
Getter method is used to get the hidden attributes in a class
setter method is used to change the hidden attributes in the class """
class weapons:
    def __init__(self, weapon1,weapon2,weapon3):
        self.__weapon1 = weapon1
        self.weapon2 = weapon2
        self.weapon3 = weapon3
    def hidden_weapon(self):
        return self.__weapon1
    def update_hidden_weapon(self,new_weapon):
        self.__weapon1 = new_weapon


# In[68]:


"""
Solution5
Method overiding is used to rewrite a method in a class """
class student:
    def __init__(self,height):
        self.average_height = height
    def height(self):
        print(f"Avergae height is :{self.average_height}")
class girl(student):
    def height(self):
        print(f"height is less than average of boys:{self.average_height}")


# In[69]:





# In[ ]:




