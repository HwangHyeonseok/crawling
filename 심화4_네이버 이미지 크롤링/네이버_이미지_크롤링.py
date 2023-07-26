# -*- coding: euc-kr -*-

# ũ�Ѹ� ���� refernce : https://kimcoder.tistory.com/259
# ���̹����� �̹����� ��ǻ�Ϳ� �ٿ�ε� �� ���� �����ϴ�.
# �˻�� �Է��ϸ� �� ���� ����Ǵ� ���α׷��� �������ּ���.

# ���� ���, �˻���� ������ �ڵ����� ������ְ� �����̸��� 1.png, 2.png, 3.png �̷� ������ 500�� ������ ũ�Ѹ� �Ǵ� ���α׷��� ���մϴ�.
# ex) ����ڰ� '������' �Է� �� -> ������ ������ �����ϰ� �ȿ� 1.png~500.png ���� ������ �ڵ����� �������ش�.

# �̹��� ũ�Ѹ� ����̳� ������ ����� ��� �� ���۸��� �غ���.

# ---------------------------------------------- ���� ���� ----------------------------------

# 1) ���̹� ����Ʈ �� ��ũ���� ���� ���� Ȯ��
#���� : robots.txt�� ũ�Ѹ����� ���� ǥ���� ����
#����Ʈ : naver.com/robots.txt

#User-agent: * => ��� �˻����� ũ�ѷ����� �����Ѵ�.
#Disallow: / => /(root) ���丮 ���� ���丮�� ũ�Ѹ��� �����Ѵ�.
#Allow : /$ => /$ ���丮�� ũ�Ѹ��� ����Ѵ�.

# 2) url �ּ� ��Ģ�� Ȯ��
# 3) ��������Ʈ(requests ����Ұ���)���� ��������Ʈ(selenium ����Ұ���)���� Ȯ��
# -> �ش� �䱸������ �̹��� �ǿ��� ������ ������ �̹����� ��� ���� �� �ְ� ����Ʈ �ּҴ� ������ �����Ƿ� ���� ����Ʈ�� �Ǵ�
# => selenium ���� ũ�Ѹ��ϴ� ���� �����ϰڴ�.
# 4) ���� ��ũ�� ó��
# 5) �̹��� �ּ� �������� �� �̹��� ���Ͽ� �����ϱ�

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pyautogui

import urllib

# ����� �Է�

search = pyautogui.prompt("� �˻����� �̹����� �����Ͻðھ��?")

# ũ�� ����̹� �ڵ� ������Ʈ
from webdriver_manager.chrome import ChromeDriverManager

#������ ���� ���� 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ���ʿ��� ���� �޽��� ���ֱ�
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)


# �������� �ش� �ּ� �̵� - ���̹��� �̹��� �˻�
imagepage = driver.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query={search}&tqi=i7jsNlprvmsssjdtxrhssssstEo-152051")
driver.implicitly_wait(5) # webpage�� �ε� �� ������ �ִ� 5�ʱ��� ��ٷ��ش�. 

# ������ ������ ��ũ�� ������
before_height = driver.execute_script("return window.scrollY")
while True:
    # �� �Ʒ��� ��ũ���� ������. (END Ű�� ���� ��ũ���� ������.)
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # ��ũ�� �Ǵ� ���� �ε� �ð��� �ش�.
    time.sleep(1)
    # ��ũ�� �� ���� üũ
    after_height = driver.execute_script("return window.scrollY")
    
    if after_height == before_height: # ������ ���� ��� ���� window.ScrollY ��ġ�� ���� ��ġ�� ����.
        break # �� ��쿡�� Ż���Ѵ�.

    before_height = after_height

# ���� ���� ��, ���ϸ� ���ڸ� �ο��ϱ� ���� ��������
i = 1

# ���� ����
import os
if not os.path.exists(f"��ȭ4_���̹� �̹��� ũ�Ѹ�/{search}"):
    os.mkdir(f"��ȭ4_���̹� �̹��� ũ�Ѹ�/{search}")

# �̹��� �±� ����
images = driver.find_elements(By.CSS_SELECTOR, "._image._listImage")
for i, image in enumerate (images, 1):
    # �� �̹��� �±��� �ּ� ����
    image_src = image.get_attribute("src")
    print(i, image_src)
    urllib.request.urlretrieve(image_src, f"��ȭ4_���̹� �̹��� ũ�Ѹ�/{search}/{i}.png")