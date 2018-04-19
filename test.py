
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime


# In[2]:


df = pd.read_csv('test report.csv')


# In[3]:


df['Time'] = pd.to_datetime(df['Time'], format='%m/%d/%Y %H:%M:%S')


# In[4]:


df['Time2'] = df['Time'].where(df['Device'].str.contains('Turnstile Out')).shift(-1)
df['TimeDiff'] = (df['Time'] - df['Time2']).astype('timedelta64[h]')
df = df.set_index("Device")
df = df.drop("Turnstile Out", axis=0)


# In[5]:

df.to_csv('output.csv', columns=['Personnel Record','Time','Time2','TimeDiff', 'Credential'])

