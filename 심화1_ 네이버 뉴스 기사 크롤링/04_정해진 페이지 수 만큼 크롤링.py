# -*- coding: euc-kr -*-
# 정해진 페이지 수 만큼 크롤링 하기

import requests
from bs4 import BeautifulSoup
import pyautogui
import time

search = pyautogui.prompt("어떤 것을 검색하시겠어요?")
lastpage = int(pyautogui.prompt("몇 페이지까지 크롤링할까요?"))
page_num = 1

for now_page in range(1, lastpage * 10, 10): # 5페이지 까지면, 1페이지 1 2페이지 11 .. 5페이지 51
    print(f"{page_num} 페이지 크롤링 중입니다.")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=54&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={now_page}")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    articles = soup.select(".info_group")

    for article in articles:
        # '네이버뉴스' 가 있는 기사만 추출한다. (<a> 하이퍼링크가 2개 이상인 경우에 해당)
        links = article.select("a.info")
        if len(links) >=2 :
            url = links[1].attrs['href']
            response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            
            # 스포츠 기사인 경우
            if "sports" in response.url: # response.url을 사용하는 경우 : html 코드 안에 있는 url 링크와 들어갔을 때 들어간 페이지의 링크가 다른 경우
                article_title = soup.select_one("h4.title")
                article_body = soup.select_one("#newsEndContents")
                # 본문 내에 불필요한 내용 제거 p태그와 div태그의 내용은 출력할 필요가 없다. 없애주자.
                p_tags = article_body.select("p") # 본문에서 p 태그인 것들을 추출
                for p_tag in p_tags:
                    p_tag.decompose()

                div_tags = article_body.select("div") # 본문에서 div 태그인 것들을 추출
                for div_tag in div_tags:
                    div_tag.decompose()
            
            # 연예 기사인 경우
            elif "entertain" in response.url:
                article_title = soup.select_one("h2.end_tit")
                article_body = soup.select_one("#articeBody")
                print(article_title)
                print(article_body)
            
            # 일반 뉴스 기사인 경우
            else:
                article_title = soup.select_one("#title_area")
                article_body = soup.select_one("#dic_area")

            # 출력문
            print("==================================================== 주소 ===========================================================")
            print(url.strip())
            print("==================================================== 제목 ===========================================================")
            print(article_title.text.strip())
            print("==================================================== 본문 ===========================================================")
            print(article_body.text.strip()) #strip 함수는 앞 뒤의 공백을 제거한다.
            time.sleep(0.3)
    page_num = page_num+1