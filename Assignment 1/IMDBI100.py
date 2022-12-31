#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://www.imdb.com/india/top-rated-indian-movies/')


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)
soup


# In[6]:


name=[]
for i in soup.find_all(class_="titleColumn"):
    name.append(i.text)
    
name


# In[7]:


rating=soup.find_all('td',class_="ratingColumn imdbRating")
rating


# In[8]:


rating=[]
for i in soup.find_all(class_="ratingColumn imdbRating"):
    rating.append(i.text.split('|'))
    
rating


# In[10]:


releasey=soup.find_all(class_="secondaryInfo")
releasey


# In[11]:


releasey=[]
for i in soup.find_all(class_="secondaryInfo"):
    releasey.append(i.text.split('|'))
    
releasey


# In[12]:


import pandas as pd


# In[13]:


df=pd.DataFrame({'Name':name,'Ratings':rating,'Release Year':releasey})
df.head(100)


# In[ ]:




