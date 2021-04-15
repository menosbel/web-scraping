# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:10:15 2021

@author: bfernandez
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "https://www.infobae.com/politica/"
response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')


titulos = soup.find_all('h2', {'class': 'headline-title'})

for titulo in titulos:
    if 'Sarlo' in titulo.text:
        print('TITULO: ', titulo.text)
        
        title_url = titulo.find('a').get('href')
        
        new_url = "https://www.infobae.com" + str(title_url)
        
        response = requests.get(new_url)
        
        data = response.text
        
        soup = BeautifulSoup(data, 'html.parser')
        
        tags = soup.find_all('div', {'class': 'nd-article-tag'})
        
        for tag in tags:
            print('TAG: ', tag.text)
        
        print('---')




url = "https://www.pagina12.com.ar/secciones/el-pais"

npo_news = {}
noticia_num = 0

while True:
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    
    noticias = soup.find_all('div', {'class': 'article-item__content-footer-wrapper'})
    
    for noticia in noticias:
        titulo_tag = noticia.find('a')
        titulo = titulo_tag.text if titulo_tag else "N/A"
        if 'vacuna' in titulo:
            date_tag = noticia.find('div', {'class': 'date'})
            date = date_tag.text if date_tag else "N/A"
            
            print('TITULO: ', titulo)
            print('FECHA: ', date)
            
            noticia_num +=1
            npo_news[noticia_num] = [titulo, date]
    
    next_page = soup.find('a', {'class': 'next'})
    if next_page.get('href'):
        if next_page.get('href')[-1] == '5':
            break
        else:
            url = 'https://www.pagina12.com.ar' + str(next_page.get('href'))
    else:
        break
    
print('Total noticias: ', noticia_num)
npo_news_df = pd.DataFrame.from_dict(npo_news, orient = 'index', columns = ['Titulo', 'Fecha'])

npo_news_df.head()

npo_news_df.to_csv('npo_news.csv')




# tags = soup.find_all('a')

# for tag in tags:
#     print(tag.get('href'))
    
    
# news = soup.find_all("div", {"class": "card-container"})

# for n in news:
#     title_tag = n.find('h2', {'class' :'headline-title'})
#     description_tag = n.find('div', {'class' :'deck'})

#     title = title_tag.text if title_tag else "N/A"
#     description = description_tag.text if description_tag else "N/A"
#     print(title, description, '\n')
    
    
    
