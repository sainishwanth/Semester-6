#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[2]:


URL = "https://www.dineout.co.in/bangalore-restaurants/welcome-back"
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


# In[3]:


page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')


# In[4]:


restaurant_main_div = soup.find("div", class_="restnt-card-wrap-new")
lst = []
for restaurant in restaurant_main_div.find_all("div", "restnt-card restaurant"):
    name = restaurant.find('a', class_="restnt-name ellipsis").contents[0]
    location = restaurant.find('div', "restnt-loc ellipsis").find_all('a')
    cuisine = restaurant.find("div", "detail-info").find_all('a')
    try:
        ratings = restaurant.find('div', "restnt-rating rating-4").contents[0]
    except AttributeError:
        ratings = restaurant.find('div', "restnt-rating rating-5").contents[0]
    image_url = restaurant.find('img', "no-img")["data-src"]
    loc_list, food_list = [loco.contents[0] for loco in location], [foo.contents[0] for foo in cuisine]
    loc, food = ",".join(loc_list), ",".join(food_list)
    lst.append([name, food, loc, ratings, image_url])


# In[5]:


df = pd.DataFrame(lst, columns=["Name", "Cuisine", "Location", "Ratings", "Image URL"])
df.to_csv('dineout.csv')
print(df.head(10))


# In[ ]:




