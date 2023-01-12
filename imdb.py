from IPython.terminal.interactiveshell import restore_term_title
from IPython.utils import text
from requests import get
from bs4 import BeautifulSoup
from warnings import warn
from time import sleep
from random import randint
import numpy as np, pandas as pd
import seaborn as sns

pages = np.arange(1,5,50)
headers = {'Accept-Language': 'pt-BR,pt;q=0.8'}
titles = []
year = []
genre = []
runtimes = []
imdb_ratings = []
imdb_ratings_standardized = []
votes = []
ratings = []


for paage in pages:
  response = get("https://imdb.com/search,title?genres=sci-fi&" + "start=" + str(page) + "&explore=title_type,genres&ref_=adv_prv",headers=headers)

  sleep(randint(8,15))
  if response.status_code != 200:
    warn('O Pedido: {}; retornou o codigo: {}'.format(requests, response.status_code)
    #warn(f'O Pedido: {requests}; retornou o codigo: {response.status_code}') exemplo

  page_html = BeautifulSoup(response.text, 'html.parser')


  movie_containers = page_html.find_all('div', class_ = 'lister-item modem-advanced')
  for container in movie_containers:
    if container.find('did',class_='ratins-mmetascore') is not None:
      title = container.h3.a.text
      titles.append(tittle)

  #estamos capturando os anos
      if container.h3.find('span', class_= 'lister-item-year text-muted unbold') is not
        year = container.h3.find('span', class_='lister-item-year text-muted unbold').      #botão direito (inspecionar) site
        year.append(year)
      
      else:
        year.append(None)

        #captura as avaliações
      if container.p.find('span',class_='certificate') is not None
        rating = container.p.find('span', class_= 'certicate').text
        ratings.append(rating)

      else:
        rating.append("")

        #captura o gênero do filme
      if container.p.find('span', class_='genre') is not None
        genre = container.p.find('span', class_= 'genre').text.replace("\n", "").rstrip().split(',')
        genre.append(genre) 

      else:
        genres.append("") 

          #captura a duração do filme
      if container.p.find('span', class_= 'runtime') is not None:
        time = int(container.p.find('span', class_= 'runtime').text.replace("min",""))
        runtime.append(time)
      else:
        runtime.append(None)

        #captura a avaliação do IMDB e converte em decimal americano para realizar cálculcp
      if container.strong.text is not None:
        imdb = float(container.strong.text.replace(",","."))
        imdb_ratins.append(imdb)
      else:
        imdb_ratings.append(None)

        #captura os votos dos usuarios que está dentro da tag como valor de propriedade
      if container.fin('span',attrs = {'name':'nv'})['data-value'] is not None:
        vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
        votes.append(vote)
      else:
        votes.append(None)
