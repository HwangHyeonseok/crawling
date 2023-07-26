# -*- coding: euc-kr -*-

# ���� ��Ȳ : 01_���̹� ������� �ּ� ��������.py �� '�Ｚ����'�� �Է��ϸ� ���������� ���̹� ���� ����� ���� ������ �� ũ�Ѹ��� �ȴ�.
# �׷���, 'BTS', '����ũ'�� ���� ���� �˻�� �Է��ϸ� ������ �߻��Ѵ�.
# �� ? -> �������� ���� ���̹� ���� ���� ���°� �ٸ��� �����̴�. (html �ڵ尡 �ٸ��� �����̴�.)

# ��������Ʈ�� ��û���� �� ����Ʈ URL�� ������������ ������ ������ �´� css �����ڸ� �������־�� �Ѵ�.
# �ذ� ��� : ���� ����������� �������� ����Ʈ�� �´� css �����ڸ� �����Ͽ� �������־�� �Ѵ�.
# ���� ���̹� �������, ���̹� ���� ����Ʈ�� �´� css �����ڸ� �����Ͽ� �������־�� �Ѵ�.

import requests
from bs4 import BeautifulSoup
import pyautogui
import time

search = pyautogui.prompt("� �˻�� �Է��ұ��?")

response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={search}&oquery=%EC%82%BC%EC%84%B1%EC%A0%84%EA%B8%B0&tqi=i74TZsprvTossZP6LTossssssvK-082600")
html = response.text
soup = BeautifulSoup(html, "html.parser")
articles = soup.select("div.info_group")

for article in articles:
    links = article.select("a.info")
    if(len(links) >= 2) :
        url = links[1].attrs['href']
        response = requests.get(url, headers={'User-agent':'Mozila/5.0'}) # ���̹� ���� ���� ���� �����ϱ� ���ؼ� headers �߰� # headers={'user-agent' : 'mozila/5.0'}�� ��谰�� ���̴� ������ ���� #�޾ƿ� url���� �ٽ� �ҷ��� 
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        
        if "entertain" in response.url: # �����̷��� ���� ������ response.url�� ���־�� �Ѵ�.
            article_title = soup.select_one(".end_tit").text
            article_content = soup.select_one("#articeBody").text
        #if "view" in url:
        else:
            article_title = soup.select_one("#title_area").text
            article_content = soup.select_one("#newsct_article").text
        
        print("==============================��ũ===============\n", url)
        print("==============================����===============\n", article_title.strip()) #strip �޼���� ���� �� ������ �������ش�.
        print("==============================����===============\n", article_content.strip())
        time.sleep(0.3) # ���α׷��� �������� �ø��� ���� ����� �Ϸ�� �ķ� 0.3�ʵ����� ���α׷��� ������.(�����ش�.)