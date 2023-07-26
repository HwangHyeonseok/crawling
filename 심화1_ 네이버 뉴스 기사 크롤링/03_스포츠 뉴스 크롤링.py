# -*- coding: euc-kr -*-
# ���̹����� �����, ����ȯ�� ���� ������ ���� �˻��� ũ�Ѹ��ϱ�

import requests
from bs4 import BeautifulSoup
import pyautogui
import time

search = pyautogui.prompt("� ���� �˻��Ͻðھ��?")

response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={search}&oquery=%EC%98%B7%EC%9C%BC%ED%99%98&tqi=i74G%2FdprvTossZPeMhCssssssko-058644")
html = response.text
soup = BeautifulSoup(html, "html.parser")
articles = soup.select(".info_group")

for article in articles:
    # '���̹�����' �� �ִ� ��縸 �����Ѵ�. (<a> �����۸�ũ�� 2�� �̻��� ��쿡 �ش�)
    links = article.select("a.info")
    if len(links) >=2 :
        url = links[1].attrs['href']
        response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        
        # ������ ����� ���
        if "sports" in response.url: # response.url�� ����ϴ� ��� : html �ڵ� �ȿ� �ִ� url ��ũ�� ���� �� �� �������� ��ũ�� �ٸ� ���
            article_title = soup.select_one("h4.title")
            article_body = soup.select_one("#newsEndContents")
            # ���� ���� ���ʿ��� ���� ���� p�±׿� div�±��� ������ ����� �ʿ䰡 ����. ��������.
            p_tags = article_body.select("p") # �������� p �±��� �͵��� ����
            for p_tag in p_tags:
                p_tag.decompose()

            div_tags = article_body.select("div") # �������� div �±��� �͵��� ����
            for div_tag in div_tags:
                div_tag.decompose()
        
        # ���� ����� ���
        elif "entertain" in response.url:
            article_title = soup.select_one("h2.end_tit")
            article_body = soup.select_one("#articeBody")
            print(article_title)
            print(article_body)
        
        # �Ϲ� ���� ����� ���
        else:
            article_title = soup.select_one("#title_area")
            article_body = soup.select_one("#dic_area")

        # ��¹�
        print("==================================================== �ּ� ===========================================================")
        print(url.strip())
        print("==================================================== ���� ===========================================================")
        print(article_title.text.strip())
        print("==================================================== ���� ===========================================================")
        print(article_body.text.strip()) #strip �Լ��� �� ���� ������ �����Ѵ�.
        time.sleep(0.3)