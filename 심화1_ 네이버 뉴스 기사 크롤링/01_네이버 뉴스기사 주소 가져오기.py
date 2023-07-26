# -*- coding: euc-kr -*-

#Quiz : ���̹����� '�Ｚ����' �˻� �� ������ ������ �� �� '���̹�����' ��ũ�� �ִ� �͵��� ��ũ�� ��� �����´�.
#'���̹�����' �� ������ �������� �ʴ´�.

import requests
import pyautogui
from bs4 import BeautifulSoup

search = pyautogui.prompt("��� �ּҸ� ������ ���ϴ� �˻�� �Է��ϼ���.")

response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={search}&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%89%B4%EC%8A%A4&tqi=i74SGdprvTossZgYZvGssssssu0-425164")
html = response.text
soup = BeautifulSoup(html, "html.parser")
articles = soup.select("div.info_group") # div �±��� Ŭ���� �̸��� info_group �� �ڵ常 ����� (����Ʈ ����)

# �� �ڵ���� �ݺ����� ������ �� ���� �ڽ� �±׵� �� <a> �±װ� 2�� �̻����� �˻�
for article in articles:
    links = article.select("a.info")
    if(len(links) >= 2) :
        print(links[1].attrs["href"])