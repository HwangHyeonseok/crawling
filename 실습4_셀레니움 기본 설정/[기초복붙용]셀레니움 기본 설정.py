# -*- coding: utf-8 -*-

# 외우는거 아님. 그냥 필요할 때 복붙
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

service = service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install()) # Chrome-for-Testing 버전이 114->115로 수정됨에 따라 수정한 코드 (20230725)
browser = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동
browser.get("https://www.naver.com")