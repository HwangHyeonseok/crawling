# -*- coding: euc-kr -*-


# 프로그램을 실행하면 검색어를 입력받고, 해당 검색어로 기사 제목만 크롤링이 되도록 만들어보자.

import requests
from bs4 import BeautifulSoup

# 0. 문자열을 입력받기
search_query = input("어떤 것을 검색할까요? : ")
i = 1

# 1. 해당 url 주소의 요청을 가져와서 response 변수에 저장
response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={}&oquery={}&tqi=i6%2BiDdp0J1ZssE87NEwssssstlR-041602".format(search_query, search_query))
#(가져올 때 %d 형식지정자보다 {} 을 쓰고 .format을 쓰는게 더 오류를 줄인다.)

# 2. response 응답 객체의 텍스트만 추출하여 웹사이트 전체 코드를 가져온다.
html = response.text

# 3. beautifulsoup을 통해 HTML 코드에서 텍스트를 쉽게 가져오도록 한다.
soup = BeautifulSoup(html, 'html.parser')

 # 4. 클래스가 news_tit 인 코드 여러개를 가져온다.
links = soup.select(".news_tit")

# 5. 반복문으로 여러 개의 제목들을 출력한다.(텍스트 형태)
for link in links:
    print("%d 번째 기사 : %s" %(i, link.text))
    i=i+1