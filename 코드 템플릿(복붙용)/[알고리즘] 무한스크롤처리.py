# 무한스크롤처리 (페이지의 끝까지) 알고리즘 (네이버 전용)
import time

# 스크롤 전 높이 : before_height

before_height = browser.execute_script("return window.scrollY")

while True:
    # 맨 아래로 스크롤을 내린다. (END 키를 눌러 스크롤을 내린다.)
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # 스크롤 되는 동안 로딩 시간을 준다.
    time.sleep(1)
    # 스크롤 후 높이 체크
    after_height = browser.execute_script("return window.scrollY")
    
    if after_height == before_height: # 끝까지 내린 경우 내린 window.ScrollY 위치가 이전 위치와 같다.
        break # 이 경우에는 탈출한다.

    before_height = after_height