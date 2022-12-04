#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get("https://www.cnbc.com/world/?region=world")
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[4]:


scraped_headline= soup.find_all(class_='LatestNews-headline')
scraped_headline


# In[5]:


headline=[]
for i in scraped_headline:
    headline.append(i.get_text().replace('\n',' '))
    
headline


# In[7]:


scraped_time= soup.find_all(class_='LatestNews-timestamp')
scraped_time


# In[8]:


time=[]
for i in scraped_time:
    time.append(i.get_text().replace('\n',' '))
    
time


# In[9]:


import pandas as pd
df = pd.DataFrame()
df['Headline'] = headline
df['Time']= time
df.head(30)


# In[ ]:




