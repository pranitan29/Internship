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


driver.get('https://www.azquotes.com/')


# In[ ]:


driver.find_element_by_link_text("Top Quotes").click()


# In[ ]:


quote = driver.find_elements(By.XPATH,'//div[@class="title"]')
author = driver.find_elements(By.XPATH,'//div[@class="author"]')
type_of_quote = driver.find_elements(By.XPATH,'//div[@class="author"]')


# In[ ]:


print(quote)
print(author)
print(type_of_quote)


# In[ ]:


driver.close()

