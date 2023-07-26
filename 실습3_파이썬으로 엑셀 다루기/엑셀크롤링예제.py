# -*- coding: euc-kr -*-
# 주식 현재가를 크롤링하여 가져와서 '파일이름.xlsx' 엑셀 파일에 B2, B3, B4의 현재가에 채워넣자.

import openpyxl
import requests
from bs4 import BeautifulSoup

#파일이름.xlsx 경로명 변수화
fpath = r"C:\pratice_crolling\실습3_파이썬으로 엑셀 다루기\파일이름.xlsx"

# 파일이름.xlsx 엑셀 파일 불러오기
excel = openpyxl.load_workbook(fpath)

# 편집할 워크시트 선택하기
worksheet = excel['주식현황']
 
# 데이터를 크롤링하기
stocks = ['005930', '000660', '035720']
row = 2
for stock in stocks:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={stock}")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal").text
    # 71,900 -> 71900 로 바꾸기 위해서 문자열 형태를 바꾼다. (',' -> '')
    price = price.replace(',', '')
    #(크롤링한 데이터는 price에 담겨있다.)
    print(price)
    
    # 크롤링한 데이터를 엑셀 파일 [B2]~[B4]셀에 넣기
    worksheet[f'B{row}'] = int(price)
    row = row+1

#수정 후 엑셀 파일 저장
excel.save(fpath)

