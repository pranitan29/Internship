#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[3]:


page=requests.get('https://www.imdb.com/chart/top/')


# In[4]:


page


# In[5]:


soup=BeautifulSoup(page.content)
soup


# In[18]:


name=soup.find_all('td',class_="titleColumn")
name


# In[24]:


name=[]
for i in soup.find_all(class_="titleColumn"):
    name.append(i.text)
    
name


# In[33]:


#rating 
rating=soup.find_all('td',class_="ratingColumn imdbRating")
rating


# In[34]:


rating=[]


# In[35]:


rating=[]
for i in soup.find_all(class_="ratingColumn imdbRating"):
    rating.append(i.text.split('|'))
    
rating


# In[20]:


releasey=soup.find_all(class_="secondaryInfo")
releasey


# In[25]:


releasey=[]
for i in soup.find_all(class_="secondaryInfo"):
    releasey.append(i.text.split('|'))
    
releasey


# In[38]:


import pandas as pd


# In[40]:


df=pd.DataFrame({'Name':name,'Ratings':rating,'Release Year':releasey})
df.head(100)


# In[ ]:





# In[ ]:





# In[ ]:




