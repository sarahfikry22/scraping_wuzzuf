#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


req=requests.get("https://wuzzuf.net/search/jobs/?q=data+analyst&a=navbl")
req


# In[3]:


req.content[ :2000]


# In[4]:


soup=BeautifulSoup(req.content,'lxml')


# In[5]:


job_title = soup.find_all("h2",{"class":"css-m604qf"})


# In[6]:


company_name = soup.find_all("a", {"class": "css-17s97q8"})


# In[7]:


location = soup.find_all("span", {"class": "css-5wys0k"})


# In[12]:


job_skill=soup.find_all( 'div',{"class":"css-y4udm8"})


# In[13]:


job_titles=[]
company_names=[]
locations=[]
job_skills=[]


# In[15]:


for i in range (len(job_title)):
    job_titles.append(job_title[i].text)
    company_names.append(company_name[i].text)
    locations.append(location[i].text)
    job_skills.append(job_skill[i].text)


# In[16]:


skills=[i.split('·', 2)[2:] for i in job_skills]


# In[17]:


skills[0]


# In[18]:


time=[i.split('·', 2)[1] for i in job_skills]


# In[19]:


time[0]


# In[20]:


job_type=[i.split('·', 2)[0] for i in job_skills]


# In[21]:


job_type[0]


# In[22]:


data = {'job_title':job_titles ,
        'company_name': company_names,
        'location':locations,
        'job_type':job_type ,
        'job_skills':skills,
        'time':time}


# In[23]:


df = pd.DataFrame(data)


# In[24]:


df


# In[25]:


df.to_csv('wuzzuf.csv')


# In[ ]:




