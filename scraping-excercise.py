# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 18:00:44 2021

@author: bfernandez
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd


# table = pd.read_html('https://www.programmableweb.com/category/tools/api')[0]


url = "https://www.programmableweb.com/category/tools/api"
response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())



rows = soup.find_all('tr')

apis_no = 0
apis_dict = {}
for row in rows:
    if row.th:
        pass
    else:
        
        name = row.find('td', {'class': 'views-field-title'})
        href = name.a.get('href')
    
        name = name.a.text
        href = 'https://www.programmableweb.com/category/tools' + str(href)
        
        description = row.find('td', {'class': 'views-field-field-api-description'}).text
        description = description.replace("\n"," ")

        category = row.find('td', {'class': 'views-field-field-article-primary-category'}).text
        
        apis_no += 1
        apis_dict[apis_no] = [name, description, category, href]
    
apis_df = pd.DataFrame.from_dict(apis_dict, orient = 'index', columns = ['Name', 'Description', 'Category', 'Link'])

apis_df.head()

apis_df.to_csv('apis_scraper.csv')




    