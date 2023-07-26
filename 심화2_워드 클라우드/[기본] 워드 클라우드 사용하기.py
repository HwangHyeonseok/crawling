# -*- coding: euc-kr -*-

# 언제 사용? 크롤링한 내용에서 주요하게 언급한 키워드가 무엇인지 분석해보고 싶을때!

import pyautogui
import pyperclip

# 전체 본문 내용 담아두는 변수
total_content = "" 

pyperclip.copy(total_content) # 전체 본문 내용을 클립보드 안에다 붙여넣어준다. (이제 복사가 되었으므로 나는 Ctrl+V로 붙여넣기만 해주면 된다.)
pyautogui.alert("클립보드에 정상 복사되었습니다.")


# 클립 보드가 복사가 되었으면, 
# 1) 구글에 "잡코리아 글자수 세기" 검색 또는 https://www.jobkorea.co.kr/service/user/tool/textcount 사이트 방문 => Ctrl + V 후 글자수가 100,000자가 넘지 않도록 조절
# 2) 구글에 "WordItOut" 검색 또는 https://worditout.com/word-cloud/create 사이트 방문 => Ctrl + V 후 키워드 분석
