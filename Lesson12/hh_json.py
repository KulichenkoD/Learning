from pprint import pprint
import re
from collections import Counter
import json
import requests

#  поиск интересующей вакансии
# search_vacancy = input('Введите текст для поиска вакансии: ')
search_vacancy = 'python developer Уфа'
url = 'https://api.hh.ru/vacancies'

params = {'text': search_vacancy}
res = requests.get(url=url, params=params).json()
count_pages = res['pages']
all_count = res['found']

result = {
        'keywords': search_vacancy,
        'count': all_count}
all_skills = []

print(f'Всего найдено вакансий: {all_count} на {count_pages} страницах.', '\n' + '-' * 30)
for page in range(count_pages):
    print(f'Обрабатывается страница {page}')
    params = {'text': search_vacancy, 'page': page}
    res = requests.get(url=url, params=params).json()
    for vac in res['items']:
        skills_vac = set()
        res_vac = requests.get(vac['url']).json()
        #  обработка описания вакансии
        description_vac = res_vac['description']
        description_skills = re.findall(r'\s[A-Za-z-?]+', description_vac)
        skills_desc = set(x.strip(' -').lower() for x in description_skills)
        # print(skills_desc)
        for skill in res_vac['key_skills']:
            all_skills.append(skill['name'].lower())
            skills_vac.add(skill['name'].lower())
        for skill in skills_desc:
            if not any(skill in x for x in skills_vac):
                all_skills.append(skill)

#print(all_skills)
skills_counter = Counter(all_skills)

to_json = []
for name, count in skills_counter.most_common(20):
    to_json.append({'skill': name,
                'count': count,
                'percent': round((count / result['count'])*100, 2)})
result['skills'] = to_json
pprint(result)
# сохранение файла с результами работы
with open('result.json', mode='w') as f:
    json.dump([result], f)

