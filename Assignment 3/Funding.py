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
url="https://trak.in/india-startup-funding-investment-2015/"
driver.get(url)


# In[4]:


Dates=[]
Company=[]
Industry=[]
Investor_Name=[]
Investment_Type=[]
Amount=[]


# In[5]:


companies=driver.find_elements(By.XPATH,"//td[@class='column-3']")
for i in companies:
    if i.text is None :
        Company.append("--") 
    else:
        Company.append(i.text)
print(len(Company),Company)


# In[6]:


Ind=driver.find_elements(By.XPATH,"//td[@class='column-4']")
for i in Ind:
    if i.text is None :
        Industry.append("--") 
    else:
        Industry.append(i.text)
print(len(Industry),Industry)


# In[7]:


dt=driver.find_elements(By.XPATH,"//td[@class='column-2']")
for i in dt:
    if i.text is None :
        Dates.append("--") 
    else:
        Dates.append(i.text)
print(len(Dates),Dates)


# In[ ]:


IN=driver.find_elements(By.XPATH,"//td[@class='column-7']")
for i in IN:
    if i.text is None :
        Investor_Name.append("--") 
    else:
        Investor_Name.append(i.text)
print(len(Investor_Name),Investor_Name)


# In[ ]:


IT=driver.find_elements(By.XPATH,"//td[@class='column-8']")
for i in IT:
    if i.text is None :
        Investment_Type.append("--") 
    else:
        Investment_Type.append(i.text)
print(len(Investment_Type),Investment_Type)


# In[ ]:


Price=driver.find_elements(By.XPATH,"//td[@class='column-9']")
for i in Price:
    if i.text is None :
        Amount.append("--") 
    else:
        Amount.append(i.text)
print(len(Amount),Amount)


# In[ ]:


Funding=pd.DataFrame()
Funding['Company']=Company
Funding['Industry']=Industry
Funding['Investor_Name']=Investor_Name
Funding['Amount Invested']=Amount
Funding['Specification']=Investment_Type
Funding['Dates']=Dates


# In[ ]:


Funding


# In[ ]:




