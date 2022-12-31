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


driver=webdriver.Chrome("chromedriver_win32")


# In[3]:


driver.get("https://www.naukri.com/")


# In[4]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input")
designation.send_keys('Data Scientist')


# In[5]:


location=driver.find_element(By.XPATH,"/html/body/div[1]/div[6]/div/div/div[5]/div/div/div/input")
location.send_keys('Bangalore')


# In[6]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[7]:


job_title=[]
job_location=[]
company_name=[]


# In[8]:


title_tags=driver.find_elements(By.XPATH,'//a[@class="title fw500 ellipsis"]')
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//li[@class="fleft grey-text br2 placeHolderLi location"]')
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)

company_tags=driver.find_elements(By.XPATH,'//a[@class="subTitle ellipsis fleft"]')
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)


# In[9]:


print(len(job_title),len(job_location),len(company_name))


# In[10]:


df=pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name})
df


# In[ ]:




