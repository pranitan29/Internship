#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[4]:


page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


scraped_Names= soup.find_all('div', 'h3', class_="presidentListing")
scraped_Names


# In[6]:


Names=[]
for Name in scraped_Names:
    Names.append(Name.get_text().replace('\n',''))
    
Names


# In[7]:


import pandas as pd
df = pd.DataFrame()
df['PRESIDENT NAME', 'DOB', 'TERM'] = Names

df


# In[ ]:




