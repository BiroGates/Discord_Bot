import requests
from itertools import islice
from bs4 import BeautifulSoup
import pandas as pd
import re


def matchup(jogando, contra_o, lane):
    # Deixando todas as letras em baixocaps
    jogando = jogando.lower()
    contra_o = contra_o.lower()
    lane = contra_o.lower()

    # Pegando os valores no site
    contra_n = contra_o.replace(' ', '-')
    response = requests.get(f'https://www.counterstats.net/league-of-legends/{jogando}/vs-{contra_n}/{lane}/all')
    site = BeautifulSoup(response.text, 'html.parser')

    # filtrando os valores
    stats = site.findAll('div', attrs={'class': 'bar'})
    sli = islice(stats, 10)
    numbers_list = []

    # Pegando só os 4 primeiros
    for c in sli:
        c.find('label', attrs={'class': ''})
        numbers_list.append(c.text)

    # tirando os \n da lista e deixando so numero
    new_numbers = []
    for n in numbers_list:
        new_number = n.replace(str('\n'), '')
        new_numbers.append(new_number)

    return new_numbers

