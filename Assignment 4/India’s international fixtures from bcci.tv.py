#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[2]:


from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from selenium.common.exceptions import ElementNotInteractableException


# In[3]:


driver=webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")
driver.get('https://www.bcci.tv/')
driver.maximize_window()


# In[4]:


try:
    fixtures=driver.find_element_by_xpath('/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a')
    fixtures.click()
except ElementNotInteractableException:
    driver.get(fixtures.get_attribute('href'))


# In[5]:


Series=[]
try:
    series=driver.find_elements_by_xpath('//div[@class="fixture-card-top"]/h5[2]/span[1]')
    for x in series:
        Series.append(x.text)
except NoSuchElementException:
    Series.append('-')
except StaleElementReferenceException:
    Series.append('-')
print(len(Series),Series)


# In[6]:


match=[]
try:
    matchs=driver.find_elements_by_xpath('//span[@class="matchOrderText ng-binding ng-scope"]')
    for x in matchs:
        match.append(x.text.replace(' -',''))
except NoSuchElementException:
    match.append('-')
except StaleElementReferenceException:
    match.append('-')
print(len(match),match)


# In[7]:


place=[]
try:
    places=driver.find_elements_by_xpath('//div[@class="fix-place ng-binding ng-scope"]')
    for x in places:
        place.append(x.text)
except NoSuchElementException:
    place.append('-')
except StaleElementReferenceException:
    place.append('-')
print(len(place),place)


# In[8]:


date=[]
try:
    dates=driver.find_elements_by_xpath('//div[@class="match-card-left match-schedule"]/h5')
    for x in dates:
        date.append(x.text)
except NoSuchElementException:
    date.append('-')
except StaleElementReferenceException:
    date.append('-')
print(len(date),date)


# In[9]:


time=[]
try:
    tim=driver.find_elements_by_xpath('//div[@class="match-card-right match-schedule "]/h5[1]')
    for x in tim:
        time.append(x.text)
except NoSuchElementException:
    time.append('-')
except StaleElementReferenceException:
    time.append('-')
print(len(time),time)


# In[10]:


df=pd.DataFrame()
df['Match Title']=match
df['Series']=Series
df['Place']=place
df['Match Date']=date
df['Match Time']=time
df


# In[ ]:




