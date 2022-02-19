from asyncio.windows_utils import pipe
from gettext import install
from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from os import pipe2
from urllib import request
import requests
url = 'https://api.exchangerate-api.com/v6/lastest'
req = request.get(url)
print(req.status_code)

dados = req.json() 
print(dados)

valor_reais = float('Infome o valor em reais a ser convertido\n')
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem US$ {(valor_reais / cotacao):.2f}')



