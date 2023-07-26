# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

i = 1

# 1. �ش� ����Ʈ�� ������ get ��û�� ���� ������ ������ reponse ������ �־��ش�.
response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&oquery=LG%EC%A0%84%EC%9E%90&tqi=i6%2BiDdp0J1ZssE87NEwssssstlR-041602")

# 2. response ���� ��ü�� �ؽ�Ʈ�� �����ϸ� ������Ʈ ��ü�� �ڵ带 �����´�. (html ����)
html = response.text

# 3. beautifulsoup�� ���� HTML �ؽ�Ʈ�� �������� ���� �����.
soup = BeautifulSoup(html, 'html.parser')

# 4. news_tit�� �ش��ϴ� Ŭ���� "���� ��"�� �ڵ带 �����´�.
links = soup.select(".news_tit")

# 5. �ڵ� �߿��� �ؽ�Ʈ�� �͸� ������ش�.
for link in links :
    print("%d %s" %(i, link.text))
    i= i+1