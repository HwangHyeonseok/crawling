# -*- coding: euc-kr -*-
# 끝 페이지를 만나면 크롤링 중지하기
# ----------------------------------------- 요구 사항 ----------------------------------------------------------
# 원하는 검색어를 입력받고, 네이버 기사를 크롤링하여 엑셀로 저장하는 프로그램을 만들어주세요.

import requests
from bs4 import BeautifulSoup
import pyautogui
import time
from openpyxl import Workbook
from openpyxl.styles import Alignment

search = pyautogui.prompt("어떤 것을 검색하시겠어요?")
lastpage = int(pyautogui.prompt("몇 페이지까지 크롤링할까요?"))
page_num = 1 # 콘솔에 페이지 수를 출력하기 위한 변수
shell_width = 65 # 엑셀의 첫 행은 'A' 부터 시작
shell_row = 2 # 엑셀의 첫 행은 1 부터 시작인데, 이미 제목으로 1을 채웠으므로 2부터 시작


# 엑셀 파일 생성
excel = Workbook()

# 엑셀 워크시트 생성
ws = excel.create_sheet(f"{search} 기사 모음")

# 엑셀 열 너비 조절
ws.column_dimensions['A'].width = 60
ws.column_dimensions['B'].width = 60
ws.column_dimensions['C'].width = 120

# 엑셀 제목부분에 내용 추가
ws['A1'] = "기사 링크"
ws['B1'] = "기사 제목"
ws['C1'] = "기사 본문"


for now_page in range(1, lastpage * 10, 10): # 5페이지 까지면, 1페이지 1 2페이지 11 .. 5페이지 51
    print(f"{page_num} 페이지 크롤링 중입니다.")
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={search}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=54&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={now_page}")
    html = response.text
    soup_naver_search_page = BeautifulSoup(html, "html.parser") # 1번째 soup : 뉴스 검색 페이지에서의 수프
    articles = soup_naver_search_page.select(".info_group")

    for article in articles:
        # '네이버뉴스' 가 있는 기사만 추출한다. (<a> 하이퍼링크가 2개 이상인 경우에 해당)
        links = article.select("a.info")
        if len(links) >=2 :
            url = links[1].attrs['href']
            response = requests.get(url, headers={'User-agent':'Mozila/5.0'})
            html = response.text
            soup_naver_article_page = BeautifulSoup(html, "html.parser") # 2번째 soup : 네이버기사를 눌러 직접 들어간 페이지의 수프
            
            # 스포츠 기사인 경우
            if "sports" in response.url: # response.url을 사용하는 경우 : html 코드 안에 있는 url 링크와 들어갔을 때 들어간 페이지의 링크가 다른 경우
                article_title = soup_naver_article_page.select_one("h4.title")
                article_body = soup_naver_article_page.select_one("#newsEndContents")
                # 본문 내에 불필요한 내용 제거 p태그와 div태그의 내용은 출력할 필요가 없다. 없애주자.
                p_tags = article_body.select("p") # 본문에서 p 태그인 것들을 추출
                for p_tag in p_tags:
                    p_tag.decompose()

                div_tags = article_body.select("div") # 본문에서 div 태그인 것들을 추출
                for div_tag in div_tags:
                    div_tag.decompose()
            
            # 연예 기사인 경우
            elif "entertain" in response.url:
                article_title = soup_naver_article_page.select_one("h2.end_tit")
                article_body = soup_naver_article_page.select_one("#articeBody")
                print(article_title)
                print(article_body)
            
            # 일반 뉴스 기사인 경우
            else:
                article_title = soup_naver_article_page.select_one("#title_area")
                article_body = soup_naver_article_page.select_one("#dic_area")

            # 출력문
            print("==================================================== 주소 ===========================================================")
            print(url.strip())
            ws[f"A{shell_row}"] = url.strip() # 엑셀 시트에 데이터 추가
            print("==================================================== 제목 ===========================================================")
            print(article_title.text.strip())
            ws[f"B{shell_row}"] = article_title.text.strip() # 엑셀 시트에 데이터 추가
            print("==================================================== 본문 ===========================================================")
            print(article_body.text.strip()) #strip 함수는 앞 뒤의 공백을 제거한다.
            ws[f"C{shell_row}"] = article_body.text.strip() # 엑셀 시트에 데이터 추가
            
            # 엑셀의 자동 줄바꿈 기능 구현
            ws[f'C{shell_row}'].alignment = Alignment(wrap_text=True)

            shell_row = shell_row +1 # 다 썼으면 엑셀은 그 다음 줄로 이동해서 또 써야한다. ex A2 B2 C2 모두 다 썼으므로 그다음 줄 A3 B3 C3을 쓴다.
            time.sleep(0.3)
    
    #마지막 페이지 여부 확인하기
    if(soup_naver_search_page.select_one("a.btn_next").attrs["aria-disabled"] == "true"):
        print("마지막 페이지입니다.")
        break
    page_num = page_num+1

excel.save(fr"C:\pratice_crolling\심화1_ 네이버 뉴스 기사 크롤링\{search} 기사 크롤링 결과.xlsx")