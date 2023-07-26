# -*- coding: euc-kr -*-
# -------------------------------------------------------문제 상황-----------------------------------------------------------
# 인공지능 학습을 위해 대량의 동물 이미지가 필요합니다.
# 강아지, 고양이 등 동물이름을 입력하면
# 이미지를 자동으로 다운받는 프로그램을 개발해 주세요.

# 단, 썸네일이 아니라 클릭했을 때 보여지는 큰 이미지를 다운로드 받아 주세요.
# 동물이름에 따라 폴더명도 자동으로 만들어서 그 안에서 저장해 주세요.

# -------------------------------------------------------Key Point-----------------------------------------------------------
# KeyPoint : HTTP Error 403 : Forbidden 에러를 해결 해보자.
# KeyPoint : click intercepted 에러를 해결 해보자. 



### 1) 정적 크롤링(requests) vs 동적 크롤링 (selenium)
# 구글 사이트에 들어가서 아무거나 검색한 후 이미지 탭을 들어가서 이미지를 보니 
# 페이지를 아래로 내려도 사이트 주소는 바뀌지 않는데, 이미지 개수는 바뀌므로,
# 이는 "동적 페이지"임을 알 수 있다.
# 이럴 경우 Selenium(셀레니움)을 이용하는 것이 간단하게 구현할 수 있다고 판단하였다.

### 2) 썸네일에서 이미지 다운 시 (.jpg) 확장자 VS 큰 이미지 다운 시 (.webp) 확장자

# -------------------------------------------------------코드 작성-----------------------------------------------------------

# SSL 설정 변경
import ssl
ssl._create_default_https_context = ssl._create_default_https_context # SSL 설정 변경 - urllib.error.URLError: <urlopen error [SSL: WRONG_SIGNATURE_TYPE] wrong signature type (_ssl.c:1002)> 오류 회피

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

# 검색어 입력 받기(사용자 입력)
search = pyautogui.prompt("구글에서 가져올 이미지의 검색어를 입력해주세요.")

# 폴더 생성
import os
#동일한 폴더가 이미 있으면 그냥 넘어간다.     #새로운 폴더라면 생성해준다.
path = f"심화5_구글 이미지 크롤링/{search}"
if not(os.path.exists(path)): 
    os.mkdir(path)

# 구글에서 검색 후 이미지 페이지 주소
main_url = f"https://www.google.com/search?hl=ko&q={search}&tbm=isch&sa=X&ved=2ahUKEwj_xp2LhJ2AAxWWZ_UHHZ5WBQYQ0pQJegQIDxAB&biw=1538&bih=587&dpr=1.25"

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

#브라우저 꺼짐 방지 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
browser = webdriver.Chrome(service=service, options=chrome_options)

#윈도우 창 크기 최대로
browser.maximize_window()

# 웹페이지 이동
browser.get(main_url)
browser.implicitly_wait(5) # 페이지가 열릴 때까지 최대 5초동안 대기

# 무한 스크롤 처리 알고리즘 적용(스크롤을 끝까지 내린다.)
before_height = browser.execute_script("return window.scrollY")

while True:
    # 스크롤을 맨 아래로 내린다.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
    after_height = browser.execute_script("return window.scrollY")

    if before_height == after_height:
        break
        #more_info = browser.find_element(By.CSS_SELECTOR, "input.LZ4I")
        #if more_info == None:
            #break
        #else:
            #more_info.click()

    before_height = after_height

# 썸네일 이미지 태그 추출 
imgs = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

for i, img in enumerate (imgs, 1):
    # 썸네일 이미지를 클릭한다.
        # 오류 참고 reference : https://deep-jin.tistory.com/entry/JAVA-Selenium-error 
    #img.click() #ElementClickInterceptedException 오류 발생 : 클릭하려는 요소가 다른 요소에 의해 가려져서 클릭할 수 없을 때 발생하는 오류
    browser.execute_script("arguments[0].click();", img) # img.click()은 오류가 발생하여, JavaScript를 사용하여 이미지 클릭

    time.sleep(0.5)
    # 큰 이미지의 url을 받아온다. (1번째 이미지는 해당하는 첫 번째 url를 가져오고 2번째이미지부터 해당하는 두 번째 url을 가져와야 한다.)
    if(i == 1):
        bigimg = browser.find_elements(By.CSS_SELECTOR, '.r48jcc.pT0Scc, .r48jcc.pT0Scc.iPVvYb')[0]
    
    else:
        bigimg = browser.find_elements(By.CSS_SELECTOR, '.r48jcc.pT0Scc, .r48jcc.pT0Scc.iPVvYb')[1] # img 태그의 class 속성 값이 "r48jcc pT0Scc"이거나 "r48jcc pT0Scc iPVvYb"인것만 가져온다.

    bigimg_src = bigimg.get_attribute("src")
    print(i, bigimg_src)

# 이미지 저장 과정
    import urllib.request

    # HTTP Error 403: Forbidden 에러 해결을 위한 코드 ("나 기계 아니고 사람이야!")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)

    #이미지 저장 (다운로드)
    try: # 오류 발생이 예상되는 코드 (urllib.error.URLError: <urlopen error [SSL: WRONG_SIGNATURE_TYPE] wrong signature type (_ssl.c:1002)> 오류)
        urllib.request.urlretrieve(bigimg_src, f'심화5_구글 이미지 크롤링/{search}/{search}_{i}.jpg')
    except: # 오류 발생 시는 해당 이미지를 다운로드 하지 않는다. -> SSL 오류는 보통 이미지가 해당 사이트에서 크롤링 하지 못하도록 막은 것이므로 크롤링해서 사용할 경우 문제가 될 수 있음.
        pass