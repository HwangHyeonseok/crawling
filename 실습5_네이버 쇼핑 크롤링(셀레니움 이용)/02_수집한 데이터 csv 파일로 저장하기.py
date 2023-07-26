# -*- coding: euc-kr -*-

# Quiz : 네이버 쇼핑 페이지에 들어가서 상품명, 가격, 링크 정보를 크롤링하는 코드를 작성하시오.
# 이때 프로그램 사용자의 입력을 받아 상품을 검색합니다.
# 예시 : 프로그램 실행 후 '유산균'을 입력하면 자동으로 네이버 쇼핑 창을 열어서 유산균 상품의 상품명, 가격, 링크 정보를 크롤링하여 출력한다.

# 셀레니움 4 기본 설정 복붙 (3~22줄)
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


# 사용자의 입력 받기 - 어떤 것을 검색할까요?
find = pyautogui.prompt("어떤 것을 검색할까요?")

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.get("https://www.naver.com")
browser.implicitly_wait(5) # webpage가 로드 될 때까지 최대 5초까지 기다려준다. 

# css 선택자가 span 태그이고 + 클래스 이름이 "service_icon type_shopping"인 것을 클릭한다.
browser.find_element(By.CSS_SELECTOR, "span.service_icon.type_shopping").click()

# 클릭하면 target="_blank" 코드 때문에 새 창으로 열리게 된다.
# 따라서 쇼핑 페이지에서 작업하도록 작업 창을 선택해준다. 
# 이때 browser.window_handles[0]은 이전에 열었던 네이버 창
# browser.window_handles[1]은 이번에 열은 네이버 쇼핑 창이다.
browser.switch_to.window(browser.window_handles[1])

# 페이지를 넘길 때마다 페이지가 로딩 될 때까지 대기해준다.
browser.implicitly_wait(5) # 최대 5초까지 대기

# css 선택자가 input 태그이고 + 클래스 이름이 _searchInput_search_text_3CUDs 인 것을 클릭한다.
search =browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 사용자에게 입력받았던 검색어를 입력한다.
search.send_keys(find)
search.send_keys(Keys.ENTER)
browser.implicitly_wait(10) # 페이지 로딩될 때까지 대기 (최대 10초 대기)

#------------------ 상품명, 가격, 링크 정보를 크롤링 --------------------------------------


# 스크롤 전 높이 확인 
before_height = browser.execute_script("return window.scrollY")
# 1) 무한 스크롤 (밑으로 끝까지 내리기)
while True:
    # 맨 아래로 스크롤을 내린다. (END 키를 눌러 스크롤을 내린다.)
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # 스크롤 되는 동안 로딩 시간을 준다.
    time.sleep(1)
    # 스크롤 후 높이 체크
    after_height = browser.execute_script("return window.scrollY")
    
    if after_height == before_height: # 끝까지 내린 경우 내린 window.ScrollY 위치가 이전 위치와 같다.
        break # 이 경우에는 탈출한다.

    before_height = after_height

#파일 생성 
# (C:\pratice_crolling\실습5_네이버 쇼핑 크롤링(셀레니움 이용)에 02_data.csv 파일 생성)
# 'w' -> 쓰기 모드로 연다. # 인코딩 타입은 CP949이다. # 줄바꿈 문자를 없앤다.
f = open(r"C:\pratice_crolling\실습5_네이버 쇼핑 크롤링(셀레니움 이용)\02_data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)


# 2) 전체 상품 크롤링
# a 태그 + 클래스 이름이 product_link__TrAac linkAnchor 인 코드를 모두 가져온다.
products = browser.find_elements(By.CSS_SELECTOR, "div.product_inner__gr8QR")

for product in products:
    name = product.find_element(By.CSS_SELECTOR, "a.product_link__TrAac.linkAnchor").text # 상품 이름
    try: # 태그가 span이고 클래스가 price_num__S2p_v 인 것의 텍스트를 찾을 수 있는 경우
        price = product.find_element(By.CSS_SELECTOR, "span.price_num__S2p_v").text # 가격
    except: # 찾을 수 없는 경우에는 예외처리
        price = "판매중단"
    link = product.find_element(By.CSS_SELECTOR, "a.product_link__TrAac.linkAnchor").get_attribute('href') # 링크 정보 (href 속성값을 가져온다.)

    print(f"상품명 : {name}, 가격 : {price}, 구매 사이트 : {link}")
    
    # csv 파일에 한 행을 추가하여 데이터 쓰기
    csvWriter.writerow([name, price, link])

f.close() # 파일 닫기

