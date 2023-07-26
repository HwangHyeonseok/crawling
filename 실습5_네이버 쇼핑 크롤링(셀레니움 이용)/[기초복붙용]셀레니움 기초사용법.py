# -*- coding: euc-kr -*-

# 셀레니움 4 기본 설정 복붙 (3~22줄)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

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

# 쇼핑 메뉴 클릭 - 클래스가 "service_icon type_shopping"인 것을 가져온다. 
#띄어쓰기 연결도 .으로 한다.
browser.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping").click()
# 새로운 탭으로 이동 - 참고 refernce : https://m.blog.naver.com/kiddwannabe/221449593300
browser.switch_to.window(browser.window_handles[1])
time.sleep(3) # 프로그램 자체를 3초 대기

# 검색창 입력 - input 태그를 가지고 + 클래스 이름이 "input._searchInput_search_text_3CUDs"인 것을 가져온다.
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys('아이폰 13')
search.send_keys(Keys.ENTER)
time.sleep(10) # 10초 대기 

# 현재 사용중인 탭 종료
browser.close()

# 메인 탭으로 이동
browser.switch_to.window(browser.window_handles[0])