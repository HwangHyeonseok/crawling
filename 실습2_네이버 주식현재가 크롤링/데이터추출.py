# -*- coding: euc-kr -*-
# 네이버 주식현재가 크롤링 하기
# 원하는 주식종목 코드를 입력하면 주식종목 코드에 맞는 주식현재가가 출력되도록 한다.
# 단, 출력 형태는 77,400(string형) 이 아닌 77400(int형) 으로 출력되도록 한다.

import requests
from bs4 import BeautifulSoup
import pyautogui

search = pyautogui.prompt("현재가를 확인할 주식 종목의 코드를 작성해주세요. ")

url = f"https://finance.naver.com/item/sise.naver?code={search}"

# 1. 해당 url에 대해서 요청을 한다. 응답을 response 객체로 담는다.
response = requests.get(url)

# 2. response 객체의 text만 가져온 것이 웹 페이지의 html 코드가 된다.
html = response.text

# 3. html 코드 문자열만으로 파싱을 하기가 어려우므로 보조도구인 beautifulsoup을 사용하여 파싱한다.
# 파싱한 것을 soup 객체에 담는다.
soup = BeautifulSoup(html, "html.parser")

# 4. id 값이 _nowVal 인 코드를 모두 가져온 다음에 text인 값만 추출하여 저장한다.
price = soup.select_one("#_nowVal").text

# 5. 현재 price는 71,900 처럼 문자열로 되어 있다. ',' 을 없애기 위해서 다음과 같은 작업을 한다.
# 교체할 문자 => , 교체 될 문자 => 빈 칸
# 즉, replace는 "문자열 교체 함수"이고 ','이 있는 부분을 '' 으로 바꾼다.
# ex. 47,900 -> 47900
price= price.replace(',', '')

print(price)
