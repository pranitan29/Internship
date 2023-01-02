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
driver.get('http://statisticstimes.com/')
driver.maximize_window()


# In[4]:


country_link=driver.find_element_by_xpath('//div[@class="navbar"]/div[2]/div[1]/a[3]')
try:
    country_link.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(country_link.get_attribute('href'))


# In[5]:


link=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
link.click()


# In[6]:


rank=[]
try:
    ranks=driver.find_elements_by_xpath('//table[@class="display dataTable"][1]/tbody/tr/td[1]')
    for x in ranks:
        rank.append(x.text)
except NoSuchElementException:
    rank.append('-')
except StaleElementReferenceException:
    rank.append('-')
rank=rank[0:33]
print(len(rank),rank)


# In[7]:


state=[]
try:
    names=driver.find_elements_by_xpath('//table[@class="display dataTable"][1]/tbody/tr/td[2]')
    for x in names:
        state.append(x.text)
except NoSuchElementException:
    state.append('-')
except StaleElementReferenceException:
    state.append('-')
state=state[0:33]
print(len(state),state)


# In[8]:


GSDP_18_19=[]
try:
    gsdp_18_19=driver.find_elements_by_xpath('//table[@class="display dataTable"][1]/tbody/tr/td[4]')
    for x in gsdp_18_19:
        GSDP_18_19.append(x.text)
except NoSuchElementException:
    GSDP_18_19.append('-')
except StaleElementReferenceException:
    GSDP_18_19.append('-')
GSDP_18_19=GSDP_18_19[0:33]
print(len(GSDP_18_19),GSDP_18_19)


# In[9]:


GSDP_19_20=[]
try:
    gsdp_19_20=driver.find_elements_by_xpath('//table[@class="display dataTable"][1]/tbody/tr/td[3]')
    for x in gsdp_19_20:
        GSDP_19_20.append(x.text)
except NoSuchElementException:
    GSDP_19_20.append('-')
except StaleElementReferenceException:
    GSDP_19_20.append('-')
GSDP_19_20=GSDP_19_20[0:33]
print(len(GSDP_19_20),GSDP_19_20)


# In[10]:


GSDP_19=[]
try:
    gsdp_19=driver.find_elements_by_xpath('//table[@class="display dataTable"][1]/tbody/tr/td[5]')
    for x in gsdp_19:
        GSDP_19.append(x.text)
except NoSuchElementException:
    GSDP_19.append('-')
except StaleElementReferenceException:
    GSDP_19.append('-')
GSDP_19=GSDP_19[0:33]
print(len(GSDP_19),GSDP_19)


# In[11]:


GDP=[]
try:
    gsdp=driver.find_elements_by_xpath('//table[@class="display dataTable"][1]/tbody/tr/td[6]')
    for x in gsdp:
        GDP.append(x.text)
except NoSuchElementException:
    GDP.append('-')
except StaleElementReferenceException:
    GDP.append('-')
GDP=GDP[0:33]
print(len(GDP),GDP)


# In[12]:


df=pd.DataFrame()
df['Rank']=rank
df['State Name']=state
df['State GSDP(18-19)']=GSDP_18_19
df['State GSDP(19_20)']=GSDP_19_20
df['State Share(2019)']=GSDP_19
df['State GDP($Billions)']=GDP
df


# In[13]:


df.to_csv('State GDP.csv')


# In[ ]:




