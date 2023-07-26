# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

i = 1

# 1. 해당 사이트의 정보를 get 요청을 통해 보내서 응답을 reponse 변수에 넣어준다.
response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&oquery=LG%EC%A0%84%EC%9E%90&tqi=i6%2BiDdp0J1ZssE87NEwssssstlR-041602")

# 2. response 응답 객체의 텍스트만 추출하면 웹사이트 전체의 코드를 가져온다. (html 변수)
html = response.text

# 3. beautifulsoup을 통해 HTML 텍스트를 가져오기 쉽게 만든다.
soup = BeautifulSoup(html, 'html.parser')

# 4. news_tit에 해당하는 클래스 "여러 개"의 코드를 가져온다.
links = soup.select(".news_tit")

# 5. 코드 중에서 텍스트인 것만 출력해준다.
for link in links :
    print("%d %s" %(i, link.text))
    i= i+1