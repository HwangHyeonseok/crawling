# -*- coding: euc-kr -*-

# 크롤링 참고 refernce : https://kimcoder.tistory.com/259
# 네이버에서 이미지를 컴퓨터에 다운로드 할 일이 많습니다.
# 검색어를 입력하면 한 번에 저장되는 프로그램을 개발해주세요.

# 예를 들어, 검색어로 폴더를 자동으로 만들어주고 파일이름은 1.png, 2.png, 3.png 이런 식으로 500개 정도를 크롤링 되는 프로그램을 원합니다.
# ex) 사용자가 '아이유' 입력 시 -> 아이유 폴더를 생성하고 안에 1.png~500.png 까지 사진을 자동으로 저장해준다.

# 이미지 크롤링 방법이나 폴더를 만드는 방법 등 구글링을 해보자.

# ---------------------------------------------- 개발 시작 ----------------------------------

# 1) 네이버 사이트 웹 스크래퍼 가능 여부 확인
#참고 : robots.txt는 크롤링계의 교통 표지판 역할
#사이트 : naver.com/robots.txt

#User-agent: * => 모든 검색엔진 크롤러에게 적용한다.
#Disallow: / => /(root) 디렉토리 이하 디렉토리의 크롤링을 금지한다.
#Allow : /$ => /$ 디렉토리는 크롤링을 허용한다.

# 2) url 주소 규칙성 확인
# 3) 정적사이트(requests 사용할건지)인지 동적사이트(selenium 사용할건지)인지 확인
# -> 해당 요구조건은 이미지 탭에서 끝까지 내려야 이미지를 모두 긁을 수 있고 사이트 주소는 변하지 않으므로 동적 사이트로 판단
# => selenium 으로 크롤링하는 것이 유리하겠다.
# 4) 무한 스크롤 처리
# 5) 이미지 주소 가져오기 및 이미지 파일에 저장하기

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pyautogui

import urllib

# 사용자 입력

search = pyautogui.prompt("어떤 검색어의 이미지를 추출하시겠어요?")

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)


# 웹페이지 해당 주소 이동 - 네이버의 이미지 검색
imagepage = driver.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query={search}&tqi=i7jsNlprvmsssjdtxrhssssstEo-152051")
driver.implicitly_wait(5) # webpage가 로드 될 때까지 최대 5초까지 기다려준다. 

# 페이지 끝까지 스크롤 내리기
before_height = driver.execute_script("return window.scrollY")
while True:
    # 맨 아래로 스크롤을 내린다. (END 키를 눌러 스크롤을 내린다.)
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # 스크롤 되는 동안 로딩 시간을 준다.
    time.sleep(1)
    # 스크롤 후 높이 체크
    after_height = driver.execute_script("return window.scrollY")
    
    if after_height == before_height: # 끝까지 내린 경우 내린 window.ScrollY 위치가 이전 위치와 같다.
        break # 이 경우에는 탈출한다.

    before_height = after_height

# 파일 저장 시, 파일명에 숫자를 부여하기 위해 변수지정
i = 1

# 폴더 생성
import os
if not os.path.exists(f"심화4_네이버 이미지 크롤링/{search}"):
    os.mkdir(f"심화4_네이버 이미지 크롤링/{search}")

# 이미지 태그 추출
images = driver.find_elements(By.CSS_SELECTOR, "._image._listImage")
for i, image in enumerate (images, 1):
    # 각 이미지 태그의 주소 추출
    image_src = image.get_attribute("src")
    print(i, image_src)
    urllib.request.urlretrieve(image_src, f"심화4_네이버 이미지 크롤링/{search}/{i}.png")