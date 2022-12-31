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


# In[ ]:


driver.maximize_window()
url="https://www.latlong.net/"
driver.get(url)


# In[ ]:


def Lat(x):
    place=driver.find_element(By.XPATH,'//*[@id="place"]')
    place.send_keys(x)
    find=driver.find_element(By.XPATH,'/html/body/main/div[2]/div[1]/form/button')
    find.click()


# In[ ]:


Lat('Mumbai')
d = driver.find_element(By.XPATH, '//span[@id="latlngspan"]')
d.text


# In[ ]:




