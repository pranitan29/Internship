#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[4]:


from bs4 import BeautifulSoup
import requests


# In[18]:


page=requests.get('https://en.wikipedia.org/wiki/Main_Page')


# In[19]:


page


# In[20]:


soup=BeautifulSoup(page.content)
soup


# In[21]:


first_title=soup.find(class_="mw-headline")
first_title


# In[22]:


first_title.text


# In[23]:


headers=[]


# In[25]:


for i in soup.find_all(class_="mw-headline"):
    headers.append(i.text)
    
headers


# In[ ]:





# In[ ]:




