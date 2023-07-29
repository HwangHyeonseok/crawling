# -*- coding: euc-kr -*-
# ---------------------- 요구 사항 -------------------------------
# 소상공인 상권 분석 서비스에 필요한 프로그램 제작

# 사용자에게 검색어를 입력 받고, 네이버 지도에 표시되는 순서대로 
#순위, 가게명, 별점, 방문자리뷰수를 엑셀에 저장하는 프로그램을 만들어주세요. (1페이지만)

# 검색어 예시 : [강남역 맛집], [홍대 술집], [이태원 카페] - [지역 + 섹터]
# !광고는 제외해주세요.
# !별점이 없는 가게는 제외해주세요.
# !방문자 리뷰가 없다면 0으로 표시해주세요.

# 예를 들어 "서울 호텔" 검색 시 1페이지에 있는 가게 정보들만 가져오면 됩니다.
# ----------------------- Point ----------------------------
# 1. iframe 태그 만났을 때 대처 방법
# 2. 무한 스크롤 처리 방법을 고안해본다.

# 셀레니움 사용 -> 스크롤 시에도 사이트 주소가 바뀌지 않음. (동적 사이트라고 판별)
# ---------------------- 코딩 -------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui
import openpyxl

search = pyautogui.prompt("네이버 지도 크롤링 프로그램입니다. 검색어를 입력해주세요. (지역 + 섹터)")

# 엑셀 파일 만들기 + 시트 만들기
wb = openpyxl.Workbook()
ws = wb.create_sheet(f"{search} 검색 결과")
# 엑셀 열 너비 조절
ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 50
ws.column_dimensions['C'].width = 10
ws.column_dimensions['D'].width = 25
# 엑셀 제목 추가
ws.append(["노출 순위", "가게명", "별점", "방문자 리뷰 수"]) 

url = f"https://map.naver.com/v5/search/{search}?c=15,0,0,0,dh"    

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service() # chrome-for-testing 버전에 맞춰 적용되는 코드
driver = webdriver.Chrome(service=service, options=chrome_options)

# iframe 내의 스크롤을 내리는 방법
# 1) iframe 쪽을 한 번 클릭
# 2) 이전 li 개수 확인
# 3) 스크롤을 내리고
# 4) 이후 li 개수 변화 확인 (변화 시 더 내려도 되는거고 변화가 없으면 끝까지 내렸다는 의미)
def scroolDown():
    driver.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click() # 1) iframe 쪽의 빈 곳을 클릭한다.
    before_li = len(driver.find_elements(By.CSS_SELECTOR, "li.UEzoS.rTjJo")) # 2)
    while True:
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END) # 3)
        time.sleep(2)
        after_li = len(driver.find_elements(By.CSS_SELECTOR, "li.UEzoS.rTjJo")) # 4)

        if(before_li == after_li): # 끝까지 내린 경우
            break
        
        before_li = after_li
    

# 웹페이지 해당 주소 이동
driver.get(url)
driver.maximize_window() # 브라우저 창 최대화
driver.implicitly_wait(5) # webpage가 로드 될 때까지 최대 5초까지 기다려준다. 

# iframe 안으로 들어가기 - 해당 iframe 으로 이동 <iframe> 태그 대처 
driver.switch_to.frame("searchIframe")
time.sleep(1)

# iframe 내의 스크롤을 모두 내린다.
scroolDown()

driver.implicitly_wait(0) # 데이터를 빠르게 출력하기 위해서 넣은 코드 - 데이터를 기다려주는 시간을 0으로 해준다.( 대기 시간 : 0초 )

shops = driver.find_elements(By.CSS_SELECTOR, "li.UEzoS.rTjJo")

rank = 1 # 노출 순위
for shop in shops:
    try: # 광고가 있는 경우 출력하지 않는다.
        ad = shop.find_element(By.CSS_SELECTOR, "a.gU6bV.mdfXq") # 광고가 있는 경우
        continue
    except:
        pass
    
    try:
        subject = shop.find_element(By.CSS_SELECTOR, "span.place_bluelink.TYaxT").text #가게명
    except: # 가게명이 없는 경우 출력(저장)하지 않는다.
        continue
    try: 
        star_score = shop.find_element(By.CSS_SELECTOR, "span.h69bs.a2RFq").text # 별점
        star_score = star_score.replace("별점\n", "") # "별점\n"은 빼고 출력
    except: # 별점이 없는 경우 출력(저장)하지 않는다.
        continue
    try: 
        review = shop.find_element(By.CSS_SELECTOR, 'span.h69bs:not([class*=" "])').text # 리뷰 수
        review = review.replace("리뷰 ", "") # "리뷰 " 부분은 빼고 출력
    except: # 리뷰수가 없는 경우 0으로 출력한다.
        review = 0

    print(f"노출 순위 : {rank} 제목 : {subject}, 별점 : {star_score}, 리뷰 수 : {review}")
    ws.append([rank, subject, star_score, review])
    rank += 1

# 엑셀 저장
wb.save(rf"C:\pratice_crolling\심화8_네이버 지도 크롤링\{search}검색 결과.xlsx")

    