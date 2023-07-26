# -*- coding: euc-kr -*-

# pyautogui 라이브러리를 이용하여 입력받는 창을 띄워보자.

import requests
from bs4 import BeautifulSoup
import pyautogui

#keyword = input("검색어를 입력해주세요: ")
keyword = pyautogui.prompt("검색어를 입력해주세요. ")
i=1

# f string 사용
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")

html = response.text

soup = BeautifulSoup(html, "html.parser")

links = soup.select(".news_tit")

for link in links:
    print(f"{i}번째 기사 : {link.text}")
    i=i+1
