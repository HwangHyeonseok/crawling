# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# naver 서버에 대화를 시도
response = requests.get("https://www.naver.com/", headers={'User-Agent' : 'Mozila/5.0'})

# naver 에서 html을 준다.
html = response.text

# html 번역선생님으로 수프를 만들었다.
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn인 것 "한 개"를 찾아낸다. (여러개면 soup.select)
#word = soup.select_one('#NM_set_home_btn')

# class 값이 MyView-module__link_more___sbxGh 인 것 "한 개"를 찾아낸다.
word = soup.select_one('.service_name')

# 텍스트 요소만 출력한다.
print(word.text)