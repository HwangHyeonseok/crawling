# 원하는 사이트의 html 코드 가져오기
import requests

response = requests.get("https://www.naver.com")
html = response.text
print(html)