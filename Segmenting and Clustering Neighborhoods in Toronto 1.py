#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd


# In[17]:


wiki = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M' #Import data from wiki page
wikipedia_page = requests.get(wiki)

df_raw = pd.read_html(wikipedia_page.content, header=0)[0]
df = df_raw[df_raw.Borough != 'Not assigned'] #Removing not assigned boroughs

df


# In[5]:


df.loc[df_new.Neighbourhood == 'Not assigned'] # Checking


# In[18]:


#Combining neighbourhoods
df_toronto = df.groupby(['Postal Code','Borough'])['Neighbourhood'].apply(lambda x: ', '.join(x))
df_toronto = df_toronto.reset_index()
df_toronto.rename(columns = {'Postal Ccode':'Postal Code'}, inplace = True)
df_toronto.rename(columns = {'Neighbourhood':'Neighborhood'}, inplace = True)
df_toronto


# In[16]:


df.shape

