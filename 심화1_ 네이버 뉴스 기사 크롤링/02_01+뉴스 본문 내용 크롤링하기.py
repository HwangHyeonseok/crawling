# -*- coding: euc-kr -*-

# 문제 상황 : 01_네이버 뉴스기사 주소 가져오기.py 로 '삼성전자'를 입력하면 정상적으로 네이버 뉴스 기사의 본문 내용이 잘 크롤링이 된다.
# 그런데, 'BTS', '블랙핑크'와 같은 연예 검색어를 입력하면 오류가 발생한다.
# 왜 ? -> 연예뉴스 기사는 네이버 뉴스 기사와 형태가 다르기 때문이다. (html 코드가 다르기 때문이다.)

# 본문사이트로 요청했을 때 사이트 URL이 스포츠뉴스면 스포츠 뉴스에 맞는 css 선택자를 지정해주어야 한다.
# 해결 방법 : 만약 연예뉴스라면 연예뉴스 사이트에 맞는 css 선택자를 지정하여 추출해주어야 한다.
# 만약 네이버 뉴스라면, 네이버 뉴스 사이트에 맞는 css 선택자를 지정하여 추출해주어야 한다.

import requests
from bs4 import BeautifulSoup
import pyautogui
import time

search = pyautogui.prompt("어떤 검색어를 입력할까요?")

response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={search}&oquery=%EC%82%BC%EC%84%B1%EC%A0%84%EA%B8%B0&tqi=i74TZsprvTossZP6LTossssssvK-082600")
html = response.text
soup = BeautifulSoup(html, "html.parser")
articles = soup.select("div.info_group")

for article in articles:
    links = article.select("a.info")
    if(len(links) >= 2) :
        url = links[1].attrs['href']
        response = requests.get(url, headers={'User-agent':'Mozila/5.0'}) # 네이버 봇이 막는 것을 방지하기 위해서 headers 추가 # headers={'user-agent' : 'mozila/5.0'}로 기계같이 보이는 오류를 막음 #받아온 url들을 다시 불러옴 
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        
        if "entertain" in response.url: # 리다이렉션 문제 때문에 response.url로 해주어야 한다.
            article_title = soup.select_one(".end_tit").text
            article_content = soup.select_one("#articeBody").text
        #if "view" in url:
        else:
            article_title = soup.select_one("#title_area").text
            article_content = soup.select_one("#newsct_article").text
        
        print("==============================링크===============\n", url)
        print("==============================제목===============\n", article_title.strip()) #strip 메서드는 양쪽 빈 공백을 제거해준다.
        print("==============================내용===============\n", article_content.strip())
        time.sleep(0.3) # 프로그램의 안정성을 올리기 위해 출력이 완료된 후로 0.3초동안은 프로그램을 잠재운다.(멈춰준다.)