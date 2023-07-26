# -*- coding: euc-kr -*-
# 시작 하기 전 터미널을 켜서 다음과 같은 명령어를 작성해야 한다.
# pip install beautifulsoup4 requests

# 원하는 검색어 + 내가 원하는 페이지까지 크롤링 해보기
# 즉, 입력으로 검색어를 입력받고 내가 원하는 페이지까지 모두 크롤링하여 기사 제목을 출력하기

# ex. 삼성전자를 10페이지까지 기사 제목을 크롤링하여 출력하는 코드를 작성해보자.

import requests;
from bs4 import BeautifulSoup;
import pyautogui

i = 1
search_query = pyautogui.prompt("검색어를 입력해주세요. ")
#search_query = input("검색어를 입력해주세요. ") // 참고로 pyautogui.prompt로 입력받는 것도 문자열로 입력받게 된다. / input으로 입력받는 것과 마찬가지.
# 그래서 정수형을 사용할 때는 int로 강제 형 변환을 해주어야 한다. 
# ex) search_query = int(pyautogui.prompt("검색어를 입력해주세요. "))

for pages in range(1,100,10) :
    # 1. 사이트에 요청을 받아오기
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search_query}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=13&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={pages}")

    # 2. 사이트 요청 중에서 text만 가져오기 -> 이 것이 페이지의 html 코드이다.
    html = response.text

    # 3. beautifulsoup 을 이용해서 html 텍스트를 제어할 수 있도록 한다.
    soup = BeautifulSoup(html, "html.parser") 

    # 4. 클래스 이름이 news_tit인 코드만 가져온다.
    links = soup.select(".news_tit")

    # 5. 기사의 제목만 출력한다.
    for link in links:
        print(f"{i} 번째 기사 : {link.text}")
        i = i+1


