# -*- coding: utf-8 -*-
# --------------------------------------- 요구 사항 ------------------------------------------------
# 네이버 로그인을 자동화하고 싶습니다.
# 네이버를 켜서 아이디 패스워드를 자동으로 입력하고 로그인 버튼을 클릭해주는 프로그램을 작성해주세요.

# 외우는거 아님. 그냥 필요할 때 복붙
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service() # Chrome-for-testing 버전이 기존 114->115로 수정됨에 따라 코드 수정
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹 페이지가 로딩될 때까지 5초는 기다린다.
driver.maximize_window() # 화면을 최대화 시킨다.

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창을 찾는다.
id = driver.find_element(By.CSS_SELECTOR, "#id") #chrome 드라이버를 가지고 #id(id값이 id인) CSS지정자에 맞는 태그를 자동으로 찾아준다.

# 그 아이디 입력창에 클릭 명령을 준다.
id.click() # 클릭
pyperclip.copy("naver_id") # 키보드 입력 (자신의 네이버 id 입력)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 비밀번호 입력창을 찾는다.
pw = driver.find_element(By.CSS_SELECTOR, "#pw") 
pw.click()
pyperclip.copy("naver_pw") # 키보드 입력 (자신의 네이버 pw 입력)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)


# 로그인 버튼을 눌러준다.
login = driver.find_element(By.CSS_SELECTOR, "#log\.login") 
login.click()