# -*- coding: euc-kr -*-
# ---------------------- 요구 사항 -------------------------------
# 토요코인 호텔 예약 사이트에서 호텔이 만석이 되어 계속 F5을 눌러 잔석을 모니터링해야 합니다.
# 일일이 모니터링을 하기 귀찮아서 잔석이 생길 때 자동으로 slack을 통해 알림을 보내주는 프로그램을 제작하려고 합니다.

# ----------------------- Point ----------------------------
# 1. post 요청
# 2. Status Code 303 -> redirection이란? 
#=> 요청을 주고 응답을 받아서 다른 url로 페이지를 보내는 것
# 3. slack 알림 보내기
# 4. 입력한 폼 데이터는 개발자도구의 Payload 탭에서 확인이 가능하다.

# ---------------------- 코딩 -------------------------------
import requests
from bs4 import BeautifulSoup

url = "https://www.toyoko-inn.com/korea/search"
form_data = {
"lcl_id": "ko",
"prcssng_dvsn": "dtl",
"sel_area_txt": "한국",
"sel_htl_txt": "토요코인 서울강남",
"chck_in": "2023/08/15",
"inn_date": "1",
"sel_area": "8",
"sel_htl": "00282",
"rsrv_num": "1",
"sel_ldgngPpl": "1"
}

response = requests.post(url, data=form_data)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
beds = soup.select("ul.btnLink03 > li")

for i, bed in enumerate (beds, 1):
    no_room = bed.select('a')
    reserve_ok_room = "자리 O"
    if len(no_room) == 0: #잔실이 없는 경우
        reserve_ok_room = "자리 X"

    # 학생 할인 이벤트 싱글룸
    if i==1 or i==2:
        print(f"학생 할인 이벤트 싱글룸 : {reserve_ok_room}")
    # 싱글룸
    elif i==3 or i==4:
        print(f"싱글룸 : {reserve_ok_room}")
    # 더블룸
    elif i==5 or i==6:
        print(f"더블룸 : {reserve_ok_room}")
    # 트윈룸
    elif i==7 or i==8:
        print(f"트윈룸 : {reserve_ok_room}")
    # 트리플룸
    elif i==9 or i==10:
        print(f"트리플룸 : {reserve_ok_room}")
    # 하트풀트윈룸
    elif i==11 or i==12:
        print(f"하트풀트윈룸 : {reserve_ok_room}")
        