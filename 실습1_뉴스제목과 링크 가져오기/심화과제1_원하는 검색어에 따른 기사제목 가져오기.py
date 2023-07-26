# -*- coding: euc-kr -*-


# ���α׷��� �����ϸ� �˻�� �Է¹ް�, �ش� �˻���� ��� ���� ũ�Ѹ��� �ǵ��� ������.

import requests
from bs4 import BeautifulSoup

# 0. ���ڿ��� �Է¹ޱ�
search_query = input("� ���� �˻��ұ��? : ")
i = 1

# 1. �ش� url �ּ��� ��û�� �����ͼ� response ������ ����
response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={}&oquery={}&tqi=i6%2BiDdp0J1ZssE87NEwssssstlR-041602".format(search_query, search_query))
#(������ �� %d ���������ں��� {} �� ���� .format�� ���°� �� ������ ���δ�.)

# 2. response ���� ��ü�� �ؽ�Ʈ�� �����Ͽ� ������Ʈ ��ü �ڵ带 �����´�.
html = response.text

# 3. beautifulsoup�� ���� HTML �ڵ忡�� �ؽ�Ʈ�� ���� ���������� �Ѵ�.
soup = BeautifulSoup(html, 'html.parser')

 # 4. Ŭ������ news_tit �� �ڵ� �������� �����´�.
links = soup.select(".news_tit")

# 5. �ݺ������� ���� ���� ������� ����Ѵ�.(�ؽ�Ʈ ����)
for link in links:
    print("%d ��° ��� : %s" %(i, link.text))
    i=i+1