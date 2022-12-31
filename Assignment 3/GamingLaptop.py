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
url="https://www.digit.in/top-products/best-gaming-laptops-40.html"
driver.get(url)


# In[4]:


Brands              =[]
Products_Description=[]
Specification       =[]


# In[5]:


brand=driver.find_elements(By.XPATH,'//div[@class="TopNumbeHeading"]')
for i in brand:
    Brands.append(str(i.text).replace("\n",""))
Brands


# In[6]:


specification_tag=driver.find_elements(By.XPATH,"//div[@class='Specs-Wrap']")
for i in specification_tag:
    Specification.append(str(i.text).replace("\n",""))
Specification


# In[7]:


description=driver.find_elements(By.XPATH,"//div[@class='Section-center']")
for i in description:
    Products_Description.append(str(i.text).replace("\n",""))
Products_Description


# In[8]:


Price=[]
price_tag=driver.find_elements(By.PARTIAL_LINK_TEXT,"₹ ")
for i in price_tag:
    Price.append(str(i.text).replace("\n","").replace('₹ ',''))
Price


# In[9]:


laptop=pd.DataFrame()
laptop['Brands']=Brands[0:9]
laptop['Price']=Price[0:9]
laptop['Specification']=Specification[0:9]
laptop['Description']=Products_Description[0:9]


# In[10]:


laptop


# In[11]:


laptop.to_csv('laptop.csv')


# In[ ]:




