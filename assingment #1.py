#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('''
Twinkle, twinkle, little star,

         How I wonder what you arel

               Up above the world so high,

               Like a diamond in the sky.

Twinkle, twinkle, little star,

         How I wonder what you are''')


# In[2]:


from platform import python_version
print(python_version())


# In[3]:


from datetime import datetime

# datetime object containing current date and time
current = datetime.now()
 
print("current date and time =", current)

# dd/mm/YY H:M:S
dt = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt)	


# In[4]:


radius=float(input("enter radius:"))
pi=3.14
area=pi*radius*radius
print("area of a circle:", area)


# In[5]:


firstname=input(" enter first name:")
secname=input(" enter second name:")
name=(firstname+" "+secname) [::-1]
print(name)


# In[6]:


num1=float(input("enter 1st num:"))
num2=float(input("enter 2nd num:"))
add=num1+num2
print(add)

