# -*- coding: euc-kr -*-
# ���� �ϱ� �� �͹̳��� �Ѽ� ������ ���� ��ɾ �ۼ��ؾ� �Ѵ�.
# pip install beautifulsoup4 requests

# ���ϴ� �˻��� + ���� ���ϴ� ���������� ũ�Ѹ� �غ���
# ��, �Է����� �˻�� �Է¹ް� ���� ���ϴ� ���������� ��� ũ�Ѹ��Ͽ� ��� ������ ����ϱ�

# ex. �Ｚ���ڸ� 10���������� ��� ������ ũ�Ѹ��Ͽ� ����ϴ� �ڵ带 �ۼ��غ���.

import requests;
from bs4 import BeautifulSoup;
import pyautogui

i = 1
search_query = pyautogui.prompt("�˻�� �Է����ּ���. ")
#search_query = input("�˻�� �Է����ּ���. ") // ����� pyautogui.prompt�� �Է¹޴� �͵� ���ڿ��� �Է¹ް� �ȴ�. / input���� �Է¹޴� �Ͱ� ��������.
# �׷��� �������� ����� ���� int�� ���� �� ��ȯ�� ���־�� �Ѵ�. 
# ex) search_query = int(pyautogui.prompt("�˻�� �Է����ּ���. "))

for pages in range(1,100,10) :
    # 1. ����Ʈ�� ��û�� �޾ƿ���
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search_query}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=13&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={pages}")

    # 2. ����Ʈ ��û �߿��� text�� �������� -> �� ���� �������� html �ڵ��̴�.
    html = response.text

    # 3. beautifulsoup �� �̿��ؼ� html �ؽ�Ʈ�� ������ �� �ֵ��� �Ѵ�.
    soup = BeautifulSoup(html, "html.parser") 

    # 4. Ŭ���� �̸��� news_tit�� �ڵ常 �����´�.
    links = soup.select(".news_tit")

    # 5. ����� ���� ����Ѵ�.
    for link in links:
        print(f"{i} ��° ��� : {link.text}")
        i = i+1


