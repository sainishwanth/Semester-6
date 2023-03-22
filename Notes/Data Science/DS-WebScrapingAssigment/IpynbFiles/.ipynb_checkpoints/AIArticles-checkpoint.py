#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


URL = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


# In[3]:


page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
list_of_articles = soup.find('ul', class_ = "sc-9zxyh7-0 cMKaMj")
lst = []


# In[13]:


for article in list_of_articles.find_all('li'):
    name = article.find('a')
    authors = article.find('span', 'sc-1w3fpd7-0 dnCnAO').contents[0]
    date = article.find('span', 'sc-1thf9ly-2 dvggWt')
    link = name['href']
    lst.append([name.find('h2').contents[0],
                authors,
                date.find('span').text,
                link])


# In[17]:


df = pd.DataFrame(lst, columns=["Name", "Authors", "Date of Publication", "Link"])
df.to_csv('AIArticles.csv')
df.head(10)


# In[ ]:




