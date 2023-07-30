# -*- coding: euc-kr -*-
#slack 활용 테스트 - slack 봇에게 메시지 보내도록 해보기
import requests

token = "xoxb-5662516985204-5645537229607-BedaC5Elif1fCTeAioWWHqFM" #Bot User OAuth Token 입력
channel = "#크롤링연습" # channel : Bot을 초대한 "채널명"
texts = "안녕 나는 봇이야! Hello World!" # text : 보낼 내용

requests.post("https://slack.com/api/chat.postMessage",
              headers={"Authorization": "Bearer "+token},
              data={"channel": channel, "text": texts})