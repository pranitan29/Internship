#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[27]:


from bs4 import BeautifulSoup
import requests


# In[28]:


page = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[29]:


soup=BeautifulSoup(page.content)
soup


# In[30]:


scraped_titles= soup.find_all(class_='sc-5smygv-0 fIXTHm')
scraped_titles


# In[31]:


titles=[]
for title in scraped_titles:
    titles.append(title.get_text().replace('\n',' '))
    
titles


# In[32]:


scraped_authors= soup.find_all(class_='sc-1w3fpd7-0 dnCnAO')
scraped_authors


# In[33]:


authors=[]
for i in scraped_authors:
    authors.append(i.get_text().replace('\n',' '))
authors  


# In[34]:


scraped_publish= soup.find_all(class_='sc-1thf9ly-2 dvggWt')
scraped_publish


# In[35]:


publish=[]
for i in scraped_publish:
    publish.append(i.get_text().replace('\n',' '))
    
publish


# In[37]:


import pandas as pd
df = pd.DataFrame()
df['Title'] = titles
df['Authors']= authors
df['Published']=publish
df


# In[ ]:





# In[ ]:




