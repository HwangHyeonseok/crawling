# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

# naver ������ ��ȭ�� �õ�
response = requests.get("https://www.naver.com/", headers={'User-Agent' : 'Mozila/5.0'})

# naver ���� html�� �ش�.
html = response.text

# html �������������� ������ �������.
soup = BeautifulSoup(html, 'html.parser')

# id ���� NM_set_home_btn�� �� "�� ��"�� ã�Ƴ���. (�������� soup.select)
#word = soup.select_one('#NM_set_home_btn')

# class ���� MyView-module__link_more___sbxGh �� �� "�� ��"�� ã�Ƴ���.
word = soup.select_one('.service_name')

# �ؽ�Ʈ ��Ҹ� ����Ѵ�.
print(word.text)