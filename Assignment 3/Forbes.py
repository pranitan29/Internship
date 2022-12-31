#!/usr/bin/env python
# coding: utf-8

# In[1]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.by import By
import time


# In[2]:


driver = webdriver.Chrome(r"C:\Users\vgoda\chromedriver.exe")


# In[3]:


driver.maximize_window()
url="https://www.forbes.com/billionaires/"
driver.get(url)


# In[4]:



Name=[]
Rank=[]
Net_worth=[]
Citizenship=[]


# In[5]:


name_tag=driver.find_elements(By.XPATH,'//div[@class="personName"]/div[1]')
for x in name_tag:
    Name.append(x.text)


# In[6]:


print(len(Name),Name)


# In[7]:


net=driver.find_elements(By.XPATH,'//div[@class="netWorth"]/div[1]')
for x in net:
    Net_worth.append(x.text.replace('B',' Billion Dollers').replace('$',''))
print(len(Net_worth),Net_worth)


# In[8]:


citizenship=driver.find_elements(By.XPATH,'//div[@class="countryOfCitizenship"]')
for x in citizenship:
    Citizenship.append(x.text)
print(len(Citizenship),Citizenship)


# In[9]:


Source=[]
source=driver.find_elements(By.XPATH,'//div[@class="expand-row__icon-container"]/span[1]')
for x in source:
    Source.append(x.text)
print(len(Source),Source)


# In[10]:


rank_tag=driver.find_elements(By.XPATH,'//div[@class="rank"]')
for x in rank_tag:
    Rank.append(x.text.replace('.',''))
print(len(Rank),Rank)


# In[11]:


billionaires=pd.DataFrame()
billionaires['Rank']=Rank
billionaires['Name']=Name
billionaires['Net Worth']=Net_worth
billionaires['Citizenship/Country']=Citizenship
billionaires['Source']=Source


# In[12]:


billionaires


# In[13]:


billionaires.to_csv('Billionaires.csv')


# In[ ]:




