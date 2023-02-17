"""
Сколько HTML-тегов в коде главной страницы сайте greenatom.ru?
Сколько из них содержит атрибуты? Напиши скрипт на Python, который выводит ответы на вопросы выше
"""

import requests
from lxml import html

url = 'https://greenatom.ru'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.824 Yowser/2.5 Safari/537.36"
    }

page = requests.get(url, headers=headers)

tree = html.fromstring(page.content)

all_el = tree.cssselect('*')

tags = len(all_el)

counter = 0

for tag in all_el:
    if tag.attrib:
        counter += 1
 
print(f'Тегов на странице = {tags}')
print(f'Тегов с атрибутами = {counter}')