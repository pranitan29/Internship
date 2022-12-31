#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
page


# In[3]:


soup=BeautifulSoup(page.content)
soup


# In[4]:


scraped_teams= soup.find_all(class_="u-hide-phablet")
scraped_teams


# In[5]:


teams=[]
for Team in scraped_teams:
    teams.append(Team.get_text().replace('\n',' '))
    
teams


# In[6]:


scraped_matches= soup.find_all('td', class_='table-body__cell u-center-text')
scraped_matches


# In[7]:


matches=[]
for match in scraped_matches:
    matches.append(match.get_text().replace('\n',""))
    
matches


# In[8]:


scraped_ratings= soup.find_all('td', class_='table-body__cell u-text-right rating')
scraped_ratings


# In[9]:


ratings=[]
for rating in scraped_ratings:
    ratings.append(rating.get_text().replace('\n',''))
    
ratings


# In[10]:


import pandas as pd
df = pd.DataFrame()
df['Teams'] = teams
df['Matches and points']=matches
df['Ratings']=ratings
df


# In[ ]:




