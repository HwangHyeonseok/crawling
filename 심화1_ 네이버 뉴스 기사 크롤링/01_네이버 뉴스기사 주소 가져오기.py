# -*- coding: euc-kr -*-

#Quiz : 네이버에서 '삼성전자' 검색 후 뉴스에 나오는 것 중 '네이버뉴스' 링크가 있는 것들의 링크를 모두 가져온다.
#'네이버뉴스' 가 없으면 가져오지 않는다.

import requests
import pyautogui
from bs4 import BeautifulSoup

search = pyautogui.prompt("기사 주소를 가져올 원하는 검색어를 입력하세요.")

response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={search}&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%89%B4%EC%8A%A4&tqi=i74SGdprvTossZgYZvGssssssu0-425164")
html = response.text
soup = BeautifulSoup(html, "html.parser")
articles = soup.select("div.info_group") # div 태그의 클래스 이름이 info_group 인 코드만 추출됨 (리스트 형태)

# 그 코드들을 반복문을 돌려서 그 안의 자식 태그들 중 <a> 태그가 2개 이상인지 검사
for article in articles:
    links = article.select("a.info")
    if(len(links) >= 2) :
        print(links[1].attrs["href"])