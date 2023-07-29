# -*- coding: euc-kr -*-
# ---------------------- 요구 사항 -------------------------------
# 저평가된 주식을 찾기 위한 크롤링 프로그램을 만들려고 합니다.
# 네이버 금융 페이지에서 시가총액을 클릭하면 나오는 페이지의 옵션에서,
# PER(배), ROE(%), PBR(배), 유보율(%) 값을 가져와 하나의 엑셀 파일로 저장하는 프로그램을 제작해주세요.
# PER, ROE, PBR, 유보율의 데이터가 N/A인 경우 해당 데이터를 모두 빼고 엑셀에 저장해주세요.

# 단, 셀레니움은 느리니까, 반드시 requests와 BS4을 이용하여 개발해주세요.

# ----------------------- Point ----------------------------
# 1. 태그에 id와 class가 없는 경우 데이터 가져오기
# 2. 표 데이터는 어떻게 가져올까?
# 3. requests의 get 요청 네트워크 분석 (HTTP 302 방식)
# ---------------------- 코딩 -------------------------------
import requests
from bs4 import BeautifulSoup
import pyautogui
import openpyxl

# 사용자 입력 - 몇 개의 종목을 볼지 사용자로부터 입력받는다.
view_stocks = int(pyautogui.prompt("시가총액 순위/PER/ROE/PBR/유보율을 조회합니다. 몇 개의 종목을 조회하시겠습니까?"))
viewed_stocks = 0
lastpage = (view_stocks // 50) + 1 # 50개마다 한 페이지
print(lastpage)
marketcap_rank = 1

# 엑셀 파일 만들기
wb = openpyxl.Workbook()
# 엑셀 워크시트 만들기
ws = wb.create_sheet('코스피 시가총액 상위 종목 분석')
# 엑셀 1행 (제목 추가)
ws.append(["시가총액 순위", "종목명", "PER", "ROE", "PBR", "유보율"])


for page in range(1, lastpage+1, 1):
    # request URL을 받아올 경우 반드시 그 주소 그대로 쓰는 것이 아니라,
    # 구글에서 url decode 을 검색해서 decode 된 주소를 사용해야 한다.
    url = f"https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?page={page}&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

    # get 요청으로 url을 받아온다.
    response = requests.get(url, headers={'User-Agent' : 'Mozila/5.0'})
    html = response.text

    # parser : 번역 선생님 을 불러온다.
    soup = BeautifulSoup(html, 'html.parser')

    stocks = soup.select('tr[onmouseover="mouseOver(this)"]') # tr 태그의 onmouseover 속성이 mouseOver(this) 인 것을 가져온다.


    for stock in stocks: # marketcap_rank는 시가총액 순위
        if view_stocks < viewed_stocks: # 입력받은 개수만큼 모두 조회한 경우 
            break
        subject = stock.select_one('tr[onmouseover="mouseOver(this)"] > td:nth-child(2)').text
        per = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(7)').text
        roe = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(8)').text
        pbr = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(9)').text
        reserve_ratio = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(10)').text
        if subject != 'N/A' and per != 'N/A' and roe != 'N/A' and pbr != 'N/A' and reserve_ratio != 'N/A':
            print(f"{marketcap_rank} : 종목명 : {subject} PER : {per} ROE : {roe} PBR : {pbr} 유보율 : {reserve_ratio}")
            ws.append([marketcap_rank,subject, per, roe, pbr, reserve_ratio]) # 엑셀에 데이터 추가
            viewed_stocks +=1

        marketcap_rank +=1

#엑셀 저장        
wb.save(rf'C:\pratice_crolling/심화7_네이버 주식 크롤링/시가총액 {view_stocks}개 종목 분석 결과.xlsx')