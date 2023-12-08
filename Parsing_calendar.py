#импортируем нужные бибилиотеки
from bs4 import BeautifulSoup
import requests
import re
#целевая ссылка
url = requests.get('https://my-calend.ru/holidays')
#объявляем суп с данными
soup = BeautifulSoup(url.content, "lxml")
# ищем только необходимый участок в ответе
title = soup.find("ul", class_="holidays-items")
#делим наши данные на список с предложениями
split_regex = re.compile(r'  ')
sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(title.text)])
# выводим наш список без цифр от лайков и каждый с новой строки
print("\n".join(list(sentences)[::2]))

