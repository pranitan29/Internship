#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[5]:


scraped_ranks= soup.find_all('td', class_='gsc_mvt_p')
scraped_ranks


# In[6]:


ranks=[]
for i in scraped_ranks:
    ranks.append(i.get_text().replace('\n',' '))
    
ranks


# In[7]:


scraped_publication= soup.find_all('td', class_='gsc_mvt_t')
scraped_publication


# In[8]:


publication=[]
for i in scraped_publication:
    publication.append(i.get_text().replace('\n',' '))
    
publication


# In[9]:


scraped_index= soup.find_all('td', class_='gsc_mvt_n')
scraped_index


# In[10]:


index=[]
for i in scraped_index:
    index.append(i.get_text().replace('\n',' '))
    
index


# In[11]:


scraped_median= soup.find_all('span', class_='gs_ibl gsc_mp_anchor')
scraped_median


# In[12]:


Median=[]
for i in scraped_median:
    Median.append(i.get_text().replace('\n',' '))
    
Median


# In[13]:


import pandas as pd
df = pd.DataFrame()
df['Rank'] = ranks
df['Publication']= publication
df['Median']= Median
df['Index']= index
df.head(10)


# In[ ]:




