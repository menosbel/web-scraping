# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 09:58:03 2021

@author: bfernandez
"""

# lxml
# beautifulsoup4
# html5lib
# requests

from bs4 import BeautifulSoup


with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
    
# print(soup.prettify())

match = soup.title.text
print(match)

article = soup.find('div', {'class': 'article'})
print(article)

headline = article.h2.a.text
print(headline)