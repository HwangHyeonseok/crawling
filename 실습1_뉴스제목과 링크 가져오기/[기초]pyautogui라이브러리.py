# -*- coding: euc-kr -*-

# pyautogui ���̺귯���� �̿��Ͽ� �Է¹޴� â�� �������.

import requests
from bs4 import BeautifulSoup
import pyautogui

#keyword = input("�˻�� �Է����ּ���: ")
keyword = pyautogui.prompt("�˻�� �Է����ּ���. ")
i=1

# f string ���
response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")

html = response.text

soup = BeautifulSoup(html, "html.parser")

links = soup.select(".news_tit")

for link in links:
    print(f"{i}��° ��� : {link.text}")
    i=i+1
