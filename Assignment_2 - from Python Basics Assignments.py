#!/usr/bin/env python
# coding: utf-8

# # Assignment_2 - Answers.

# ### 1.What are the two values of the Boolean data type? How do you write them?
# 
# * True with an Upper case 'T'
# * False with an Upper case 'F'

# ### 2. What are the three different types of Boolean operators?
# 
# * and
# * or
# * not

# ### 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# 
# #### and operator:
# * True and True is True.
# * False and False is False.
# * True and False is False.
# * False and True is False.
# 
# #### or operator:
# * True or True is True.
# * False or False is False.
# * True or False is True.
# * False or True is True.
# 
# #### not operator:
# * not True is False.
# * not False is True.

# ### 4. What are the values of the following expressions?
# 
# * (5 > 4) and (3 == 5) --> False
# * not (5 > 4) --> False
# * (5 > 4) or (3 == 5) --> True
# * not ((5 > 4) or (3 == 5)) --> False
# * (True and True) and (True == False) --> False
# * (not False) or (not True) --> True
# 

# In[4]:


(5 > 4) and (3 == 5) 


# In[5]:


not (5 > 4) 


# In[6]:


(5 > 4) or (3 == 5)


# In[7]:


not ((5 > 4) or (3 == 5)) 


# In[8]:


(True and True) and (True == False) 


# In[9]:


(not False) or (not True)


# ### 5. What are the six comparison operators?
# 
# * ==
# * !=
# * <
# * |>|   was unable to keep that sign without these || marks.
# * <=
# * |>|=.  was unable to keep that sign without these || marks.

# #### 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# 
# * == equal to operator is an operator which compares two values and evaluates to a boolean value.
# * = assignment operator assigns and stores the value in variable.

# #### 7. Identify the three blocks in this code:
# 
#  

# In[14]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')
    print('spam')
    
    # three blocks are inside the if statements and lines print('ham'), print('bacon'), print('spam'


# #### 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

# In[21]:


spam = 0

if spam == 1:
    print('Hello')
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# In[22]:


spam = 1

if spam == 1:
    print('Hello')
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# In[24]:


spam = 2

if spam == 1:
    print('Hello')
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# #### 9.If your programme is stuck in an endless loop, what keys you’ll press?
# 
# We can press CTRL + C to stop when you're stuck in a loop.

# #### 10. How can you tell the difference between break and continue?
# 
# The Break statement will perform outisde and after the loop.
# The continue statement moves to the start of the loop.

# #### 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# 
# * range(10) - 0 to 9 range of count.
# * range(0,10) - to start from 0 range.
# * range(0,10,1)- 0 to 9 but skips one number at each instance.

# #### 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[25]:


for i in range (1,11):
    print(i)


# In[26]:


i = 1
while i <= 10:
    print(i)
    i = i + 1


# #### 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# After importing spam the function name would be : spam.bacon()

# In[ ]:




