#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[2]:


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.common.exceptions import 


# In[3]:


url='https://www.imdb.com/list/ls095964455/'
#open web driver
driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.get(url)


# In[ ]:


name=[]
try:
    names=driver.find_elements_by_xpath('//h3[@class="lister-item-header"]/a[1]')
    for x in names:
        name.append(x.text)
except NoSuchElementException:
    name.append('-')
except StaleElementReferenceException:
    name.append('-')
print(len(name),name)


# In[4]:


year=[]
try:
    years=driver.find_elements_by_xpath('//h3[@class="lister-item-header"]/span[2]')
    for x in years:
        year.append(x.text)
except NoSuchElementException:
    year.append('-')
except StaleElementReferenceException:
    year.append('-')
print(len(year),year)


# In[5]:


genre=[]
try:
    genres=driver.find_elements_by_xpath('//span[@class="genre"]')
    for x in genres:
        genre.append(x.text)
except NoSuchElementException:
    genre.append('-')
except StaleElementReferenceException:
    genre.append('-')
print(len(genre),genre)


# In[6]:


time=[]
try:
    run=driver.find_elements_by_xpath('//span[@class="runtime"]')
    for x in run:
        time.append(x.text)
except NoSuchElementException:
    time.append('-')
except StaleElementReferenceException:
    time.append('-')
print(len(time),time)


# In[7]:


rating=[]
try:
    ratings=driver.find_elements_by_xpath('//div[@class="ipl-rating-star small"]/span[2]')
    for x in ratings:
        rating.append(x.text)
except NoSuchElementException:
    rating.append('-')
except StaleElementReferenceException:
    rating.append('-')
print(len(rating),rating)


# In[8]:


vote=[]
try:
    votes=driver.find_elements_by_xpath('//div[@class="lister-item-content"]/p[4]/span[2]')
    for x in votes:
        vote.append(x.text)
except NoSuchElementException:
    vote.append('-')
except StaleElementReferenceException:
    vote.append('-')
print(len(vote),vote)


# In[9]:


df=pd.DataFrame()
df['Movie Name']=name
df['Year span']=year
df['Genre']=genre
df['Run Time']=time
df['Ratings']=rating
df['Votes']=vote
df


# In[10]:


df.to_csv('most watched tv series.csv')
#close the driver
driver.close()


# In[ ]:




