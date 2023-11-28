import json
import sys

import requests


url_all = 'https://restcountries.com/v2/all'
url_name = 'https://restcountries.com/v2/name'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200: 
            return resposta.text
    except ConnectionError as error:
        print(error,f'Erro ao realizar requisição na ulr {url}')


def parsing(response_text):
    try:
        return json.loads(response_text)
    except:
        print('Erro ao fazer parsing')


def count_countries():
    response = requisicao(url_all)
    if response:
        response_parsing = parsing(response)
        if response_parsing:    
            return len(response_parsing)


def list_countries(countries_list):
    for country in countries_list:
        print(country['name'])


def list_population(country_name):
    response = requisicao(f'{url_name}/{country_name}')
    if response:
        response_parsing = parsing(response)
        if response_parsing:
            for country in response_parsing:
                print(f'{country["name"]}: {country["population"]}')
    else:
        print('País não encontrado')


def show_currencies(country_name):
    response = requisicao(f'{url_name}/{country_name}')
    if response:
        response_parsing = parsing(response)
        if response_parsing:
            for country in response_parsing:
                print(country['name'])
                currencies = country['currencies']
                for num,currency in enumerate(currencies,start=1):
                    print(f'{num} - {currency["name"]}: {currency["code"]}')
    else:
        print('País não encontrado')


def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print('É preciso passar o nome do país')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('## Bem vindo ao sistema de países ##')
        print('Uso: python paises.py <ação> <nome do país>')
        print('Ações disponíveis: contagem, moeda, população')
    else:
        argumento1 = sys.argv[1]
        if argumento1 == 'contagem':
            print(f'Quantidade de países: {count_countries()}')
        elif argumento1 == 'moeda':
            country = read_country_name()
            if country:
                show_currencies(country)
        elif argumento1 == 'populacao':
            country = read_country_name()
            if country:
                list_population(country)
        else:
            print('Argumento inválido')

