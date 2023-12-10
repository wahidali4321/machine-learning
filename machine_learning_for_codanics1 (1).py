#!/usr/bin/env python
# coding: utf-8

# ## how to deal with missing values

# ## <center>import four basic library

# In[31]:


# Template with Four Basic Libraries

# 1. NumPy for numerical operations
import numpy as np

# 2. Pandas for data manipulation and analysis
import pandas as pd

# 3. Matplotlib for data visualization
import matplotlib.pyplot as plt

# 4. Requests for making HTTP requests
import requests

# Rest of your code goes here...
import seaborn as sns
from sklearn.impute import SimpleImputer


# ## load the data set

# In[32]:


df = pd.read_csv('amazon.csv')


# In[3]:


df.head()


# In[4]:


## vizulize the data
plt.figure(figsize =(8,5))
sns.heatmap(df.isnull(), cbar = True)
plt.show()


# In[5]:


#another way to find out missing values
df.isnull()


# In[6]:


# also find out it's sum
df.isnull().sum()


# In[7]:


# now to find out it's percentage
df.isnull().sum()/len(df)*100


# In[8]:


# also  find through info() function
df.info()


# In[9]:


# now to find out through sort function
df.isnull().sum().sort_values(ascending=False)


# ## now i'm deleting some columns
# 

# In[10]:


df.drop('cpu_speed',axis = 1,inplace=True)


# In[11]:


df


# In[12]:


# now we are droping another columns
df.drop('special_features',axis=1,inplace =True)
df


# In[13]:


df.describe()


# ## <center> Mean

# In[14]:


df['rating'].mean()


# ## <center> Mode

# In[15]:


df['brand'].mode()


# In[16]:


# now to find out mode of the model
df['model'].mode()


# ## <center> fillna

# #### replace dollare sign with 1

# In[ ]:





# In[25]:


df


# In[27]:


df.


# In[28]:





# In[29]:


df.describe()


# In[30]:


df.describe()


# In[ ]:




