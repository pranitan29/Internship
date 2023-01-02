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
driver.get('https://www.guru99.com/')
driver.maximize_window()


# In[4]:


selenium_link=driver.find_elements(By.XPATH,"//ul[@class='menu1'][1]/li[3]/a")
try:
    selenium_link.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(selenium_link.get_attribute('href'))


# In[5]:


selenium_link=driver.find_element_by_xpath('//table[@class="table"][5]/tbody/tr[34]/td[1]/a')
try:
    selenium_link.click()
except ElementNotInteractableException:#handling element not clickable exception
    driver.get(selenium_link.get_attribute('href'))


# In[6]:


name=[]
try:
    names=driver.find_elements_by_xpath('//table[@class="table table-striped"]/tbody/tr/td[1]')
    for x in names:
        name.append(x.text)
except NoSuchElementException:
    name.append('-')
except StaleElementReferenceException:
    name.append('-')
print(len(name),name)


# In[7]:


description=[]
try:
    des=driver.find_elements_by_xpath('//table[@class="table table-striped"]/tbody/tr/td[2]')
    for x in des:
        description.append(x.text)
except NoSuchElementException:
    description.append('-')
except StaleElementReferenceException:
    description.append('-')
print(len(description),description)


# In[8]:


df=pd.DataFrame()
df['Exception Name']=name
df['Description']=description
df


# In[ ]:




