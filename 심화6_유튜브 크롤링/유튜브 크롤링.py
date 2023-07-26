# -*- coding: euc-kr -*-
# -------------------------------------------------------문제 상황----------------------------------------------------------
# 유튜브를 키우고 싶은 사람입니다. 유튜브를 성장시키기 위해 잘 팔리는 제목을 뽑아내려고 합니다.
# 제목 분석을 위해서 "유튜브 사이트에서 검색을 하여 상위 1번부터 200개 영상의 제목/조회수/날짜"을
# "하나의 엑셀"로 저장해주는 크롤링 하는 프로그램을 만들어주세요.

# 상세 요구 조건입니다.
# 제목은 제목 그대로 출력하면 됩니다.
# 조회수는 15만회라면, 숫자로 150000 이 엑셀에 저장되도록 하면 됩니다.
# 날짜는 3개월 전 과 같이 현재 시점에서 영상을 업로드한 기간을 엑셀에 저장되도록 하면 됩니다.
# 유튜브 라이브 방송은 출력에서 제외해주세요.

# -------------------------------------------------------문제 분석----------------------------------------------------------
# * 1) 정적 사이트(requests) vs 동적 사이트(selenium) 판별
# 유튜브 페이지에서 검색어를 검색하고 밑으로 스크롤을 내리면 영상들이 추가적으로 더 뜨는데, url 주소는 바뀌지 않는다.
# 즉, 동적 사이트로 판별할 수 있고 selenium 으로 크롤링 하는 것이 더 편할 것이라고 판단하였다.
# -------------------------------------------------------소스 코드----------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#사용자의 입력 받기 (검색어 입력)
import pyautogui
search = pyautogui.prompt("유튜브 크롤링 프로그램입니다. 200개의 영상의 제목/조회수/날짜를 크롤링합니다. 검색어를 입력해주세요.")

import openpyxl

# 1) 엑셀 만들기
wb = openpyxl.Workbook()

# 2) 엑셀 워크시트 만들기
ws = wb.create_sheet(search)

# 3) 엑셀 너비 열 조절
ws.column_dimensions['A'].width = 10
ws.column_dimensions['B'].width = 120
ws.column_dimensions['C'].width = 13
ws.column_dimensions['D'].width = 10

# 3) 엑셀 제목 넣기
ws['A1'] = "영상 번호"
ws['B1'] = "영상 제목"
ws['C1'] = "조회수"
ws['D1'] = "날짜"

# "조회수 8.3억회 -> 830000000 으로 파싱하기 위한 함수"
def parse_views(views_str):
    if '천회' in views_str:
        views_str = views_str.replace('조회수 ', '').replace('천회', '').strip()
        views = float(views_str) * 1000
    elif '만회' in views_str:
        views_str = views_str.replace('조회수 ', '').replace('만회', '').strip()
        views = float(views_str) * 10000
    elif '억회' in views_str:
        views_str = views_str.replace('조회수 ', '').replace('억회', '').strip()
        views = float(views_str) * 100000000
    elif '회' in views_str:
        views_str = views_str.replace('조회수 ', '').replace('회', '').strip()
        views = views_str
    else: #조회수가 없는 경우
        views = 0

    return int(views)

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service() # chrome-for-testing 버전에 맞춰 적용되는 코드
browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.get(f"https://www.youtube.com/results?search_query={search}")
browser.implicitly_wait(5) # webpage가 로드 될 때까지 최대 5초까지 기다려준다. 

# 스크롤 내리기 (단, 영상 200개만 추출하므로 200개까지만 내린다.)
before_height = browser.execute_script("return window.scrollY")

while True:
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(2) # 2초 대기
    
    after_height = browser.execute_script("return window.scrollY")
    print("전 :" + str(before_height))
    print("후 :" + str(after_height))

    video_count = len(browser.find_elements(By.CSS_SELECTOR, "div#dismissible.style-scope.ytd-video-renderer"))
    if(video_count >= 200 ): # 영상 200개를 채운 경우 - div 태그의 id 속성값이 dismissible 이면서 동시에 class 속성값이 style-scope ytd-video-renderer 인 것이 200개가 넘는지 검사한다.
        print("영상 200개를 찾았습니다.")
        break
    
    elif before_height == after_height: # 스크롤을 끝까지 다 내린 경우
        print(f"검색할 수 있는 영상이 {video_count}개 입니다. 스크롤을 다 내렸습니다.")
        break



    before_height = after_height

infos = browser.find_elements(By.CSS_SELECTOR, "div.text-wrapper.style-scope.ytd-video-renderer")

#nth-child : 모든 자식의 순서에서 찾음
#nth-of-type: 해당하는 자식 태그 요소에서의 순서를 찾음

video_index = 1 #영상 순서 세기 위한 변수 (n번째 영상)
# info 코드 안에서 순회하면서 제목/조회수/날짜 등의 정보를 얻어온다.
for info in infos:
    # 제목
    subject = info.find_element(By.CSS_SELECTOR, "a#video-title") # 제목들을 리스트로 담는다.
    view = info.find_element(By.CSS_SELECTOR, "div#metadata-line>span:nth-of-type(1)") # 조회수 - div 태그의 id 속성값이 metadata-line인 바로 자식의 span 태그의 첫 번째 것을 가져온다.
    view_num = parse_views(view.text) # 조회수 파싱 ex. 조회수 16만회 -> 160,000
    try:
        date = info.find_element(By.CSS_SELECTOR, "div#metadata-line>span:nth-of-type(2)") # 날짜
    except:
        print("생방송 라이브입니다.")
        continue
    
    print(f"{video_index}번째 영상 - 제목 : {subject.text} 조회수 : {view_num} 날짜 : {date.text}")
    # 엑셀에 데이터 저장
    ws[f'A{video_index+1}'] = video_index
    ws[f'B{video_index+1}'] = subject.text
    ws[f'C{video_index+1}'] = view_num
    ws[f'D{video_index+1}'] = date.text
    
    video_index += 1

# 엑셀 저장하기
wb.save(rf'C:\pratice_crolling\심화6_유튜브 크롤링\{search}.xlsx')
print("크롤링 엑셀 파일 생성 및 저장 완료")