from pprint import pprint
from requests import get

#получение списка вакансий по поисковому запросу
url = 'https://api.hh.ru/vacancies'
params = {'text': 'python developer Уфа'}
# 'alternate_url': 'https://hh.ru/search/vacancy?area=99&enable_snippets=true&order_by=publication_time&text=python+developer'

# res = get(url, params=params).json()
# pprint(res)

#print(res['found'])        #найдено вакансий
# 'page': 0,
#  'pages': 4,
#  'per_page': 20,
#pprint(res['items'][:3])

#получение информации о каждой вакансии по ее url
url = 'https://api.hh.ru/vacancies/94737408?host=hh.ru'
res = get(url).json()
#
# #pprint(res['items'][:3])
pprint(res)

#'url': 'https://api.hh.ru/vacancies/94737408?host=hh.ru'
#'alternate_url': 'https://hh.ru/vacancy/94737408'
