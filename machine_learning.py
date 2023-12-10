#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
import seaborn as sn


# ### <cente> data set for machin learning

# In[5]:


data = {'CAR NAME':['BMW','Volvo','VW',"VW",'Ford','VW','Tesla','BMW','Volvo','Ford','Toyata','VW','Toyata'],
       'COLOR':['red','black','gray','white','white','white','red','black','gray','white','gray','white','blue'],
       'YEAR':[5,7,8,7,2,17,2,9,4,11,12,9,6],
       'speed':[99,86,87,88,111,86,103,87,94,78,77,85,86],
       'auto pilot':['Y','Y','N','Y','Y','Y','Y','Y','N','N','N','N','Y']}
df = pd.DataFrame(data)


# In[6]:


df


# ### mean , mode , medain

# In[17]:


import numpy
list = [99,86,87,88,111,86,103,87,94,78,77,85,86]

me = numpy.mean(list)
print(me)


# In[18]:


import numpy
list = [11,22,33,44,55,6,77,88,99]
x = numpy.mean(list)
print(x)


# In[20]:


# now we find mode 
import numpy
speed = [22,33,44,55,66,77,88,99,44]
x = numpy.median(speed)
print(x)


# In[23]:


## now we find mode
import numpy
speed = [11,222,333,44,555,66,77,88,99,8887,11]
x = numpy.mod(speed)
print(x)


# In[25]:


from scipy import stats
x = [11,22,33,44,55]
speed = stats.mode(x)
print(speed)


# ## to find out standart deviation

# import numpy
# speed = [32,111,138,28,59,77,97]
# 
# means = numpy.mean(speed)
# print("the mean of the speed ",means)
# standard = numpy.std(speed)
# print(standard,'the standart deviation is this')

# ## <center> variance

# In[28]:


#example of w3 school
import numpy

speed = [32,111,138,28,59,77,97]

x = numpy.var(speed)

print(x)


# In[ ]:




