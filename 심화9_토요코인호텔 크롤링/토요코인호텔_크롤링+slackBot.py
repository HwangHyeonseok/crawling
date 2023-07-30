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
import time

#slack 활용 테스트 - slack 봇에게 메시지 보내도록 해보기
token = "xoxb-5662516985204-5645537229607-BedaC5Elif1fCTeAioWWHqFM" #Bot User OAuth Token 입력
channel = "#크롤링연습" # channel : Bot을 초대한 "채널명"

def send_passage(texts):
    requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": texts})

url = "https://www.toyoko-inn.com/korea/search" # POST 요청을 한 문서의 Request URL (개발자 도구 F12 > Headers > Request URL 확인)
form_data = { # POST 요청을 한 문서의 Form 데이터 정보 (개발자 도구 F12 > Payload > Form Data 확인)
"lcl_id": "ko",
"prcssng_dvsn": "dtl",
"sel_area_txt": "한국", #목적지 국가
"sel_htl_txt": "토요코인 서울강남", # 목적지 상세
"chck_in": "2023/07/31", # 체크인 날짜
"inn_date": "1",
"sel_area": "8",
"sel_htl": "00282",
"rsrv_num": "1",
"sel_ldgngPpl": "1"
}


attempt = 1 # 시도 횟수

while True: 
    try:
        print(f'{attempt} 번째 시도입니다.')
        response = requests.post(url, data=form_data)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        beds = soup.select("ul.btnLink03 > li")

        for i, bed in enumerate (beds, 1):
            no_room = bed.select('a')
            if len(no_room) >= 1: #잔실이 있는 경우
            # 학생 할인 이벤트 싱글룸
                if i==1 or i==2:
                    send_passage(f"학생 할인 이벤트 싱글룸에 잔실이 있습니다.")
                    print(f"학생 할인 이벤트 싱글룸에 잔실이 있습니다.")
                # 싱글룸
                elif i==3 or i==4:
                    send_passage(f"싱글룸에 잔실이 있습니다.")
                    print(f"싱글룸에 잔실이 있습니다.")
                # 더블룸
                elif i==5 or i==6:
                    send_passage(f"더블룸에 잔실이 있습니다.")
                    print(f"더블룸에 잔실이 있습니다.")
                # 트윈룸
                elif i==7 or i==8:
                    send_passage(f"트윈룸에 잔실이 있습니다.")
                    print(f"트윈룸에 잔실이 있습니다.")
                # 트리플룸
                elif i==9 or i==10:
                    send_passage(f"트리플룸에 잔실이 있습니다.")
                    print(f"트리플룸에 잔실이 있습니다.")
                # 하트풀트윈룸
                elif i==11 or i==12:
                    send_passage(f"하트풀트윈룸에 잔실이 있습니다.")
                    print(f"하트풀트윈룸에 잔실이 있습니다.")

    except:
        print("오류 발생!")
    
    time.sleep(10)
    attempt += 1