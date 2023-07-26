# -*- coding: euc-kr -*-
# -------------------------------------------------------���� ��Ȳ-----------------------------------------------------------
# �ΰ����� �н��� ���� �뷮�� ���� �̹����� �ʿ��մϴ�.
# ������, ����� �� �����̸��� �Է��ϸ�
# �̹����� �ڵ����� �ٿ�޴� ���α׷��� ������ �ּ���.

# ��, ������� �ƴ϶� Ŭ������ �� �������� ū �̹����� �ٿ�ε� �޾� �ּ���.
# �����̸��� ���� ������ �ڵ����� ���� �� �ȿ��� ������ �ּ���.

# -------------------------------------------------------Key Point-----------------------------------------------------------
# KeyPoint : HTTP Error 403 : Forbidden ������ �ذ� �غ���.
# KeyPoint : click intercepted ������ �ذ� �غ���. 



### 1) ���� ũ�Ѹ�(requests) vs ���� ũ�Ѹ� (selenium)
# ���� ����Ʈ�� ���� �ƹ��ų� �˻��� �� �̹��� ���� ���� �̹����� ���� 
# �������� �Ʒ��� ������ ����Ʈ �ּҴ� �ٲ��� �ʴµ�, �̹��� ������ �ٲ�Ƿ�,
# �̴� "���� ������"���� �� �� �ִ�.
# �̷� ��� Selenium(�����Ͽ�)�� �̿��ϴ� ���� �����ϰ� ������ �� �ִٰ� �Ǵ��Ͽ���.

### 2) ����Ͽ��� �̹��� �ٿ� �� (.jpg) Ȯ���� VS ū �̹��� �ٿ� �� (.webp) Ȯ����

# -------------------------------------------------------�ڵ� �ۼ�-----------------------------------------------------------

# SSL ���� ����
import ssl
ssl._create_default_https_context = ssl._create_default_https_context # SSL ���� ���� - urllib.error.URLError: <urlopen error [SSL: WRONG_SIGNATURE_TYPE] wrong signature type (_ssl.c:1002)> ���� ȸ��

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui

# �˻��� �Է� �ޱ�(����� �Է�)
search = pyautogui.prompt("���ۿ��� ������ �̹����� �˻�� �Է����ּ���.")

# ���� ����
import os
#������ ������ �̹� ������ �׳� �Ѿ��.     #���ο� ������� �������ش�.
path = f"��ȭ5_���� �̹��� ũ�Ѹ�/{search}"
if not(os.path.exists(path)): 
    os.mkdir(path)

# ���ۿ��� �˻� �� �̹��� ������ �ּ�
main_url = f"https://www.google.com/search?hl=ko&q={search}&tbm=isch&sa=X&ved=2ahUKEwj_xp2LhJ2AAxWWZ_UHHZ5WBQYQ0pQJegQIDxAB&biw=1538&bih=587&dpr=1.25"

# ũ�� ����̹� �ڵ� ������Ʈ
from webdriver_manager.chrome import ChromeDriverManager

#������ ���� ���� 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ���ʿ��� ���� �޽��� ���ֱ�
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
browser = webdriver.Chrome(service=service, options=chrome_options)

#������ â ũ�� �ִ��
browser.maximize_window()

# �������� �̵�
browser.get(main_url)
browser.implicitly_wait(5) # �������� ���� ������ �ִ� 5�ʵ��� ���

# ���� ��ũ�� ó�� �˰��� ����(��ũ���� ������ ������.)
before_height = browser.execute_script("return window.scrollY")

while True:
    # ��ũ���� �� �Ʒ��� ������.
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
    after_height = browser.execute_script("return window.scrollY")

    if before_height == after_height:
        break
        #more_info = browser.find_element(By.CSS_SELECTOR, "input.LZ4I")
        #if more_info == None:
            #break
        #else:
            #more_info.click()

    before_height = after_height

# ����� �̹��� �±� ���� 
imgs = browser.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

for i, img in enumerate (imgs, 1):
    # ����� �̹����� Ŭ���Ѵ�.
        # ���� ���� reference : https://deep-jin.tistory.com/entry/JAVA-Selenium-error 
    #img.click() #ElementClickInterceptedException ���� �߻� : Ŭ���Ϸ��� ��Ұ� �ٸ� ��ҿ� ���� �������� Ŭ���� �� ���� �� �߻��ϴ� ����
    browser.execute_script("arguments[0].click();", img) # img.click()�� ������ �߻��Ͽ�, JavaScript�� ����Ͽ� �̹��� Ŭ��

    time.sleep(0.5)
    # ū �̹����� url�� �޾ƿ´�. (1��° �̹����� �ش��ϴ� ù ��° url�� �������� 2��°�̹������� �ش��ϴ� �� ��° url�� �����;� �Ѵ�.)
    if(i == 1):
        bigimg = browser.find_elements(By.CSS_SELECTOR, '.r48jcc.pT0Scc, .r48jcc.pT0Scc.iPVvYb')[0]
    
    else:
        bigimg = browser.find_elements(By.CSS_SELECTOR, '.r48jcc.pT0Scc, .r48jcc.pT0Scc.iPVvYb')[1] # img �±��� class �Ӽ� ���� "r48jcc pT0Scc"�̰ų� "r48jcc pT0Scc iPVvYb"�ΰ͸� �����´�.

    bigimg_src = bigimg.get_attribute("src")
    print(i, bigimg_src)

# �̹��� ���� ����
    import urllib.request

    # HTTP Error 403: Forbidden ���� �ذ��� ���� �ڵ� ("�� ��� �ƴϰ� ����̾�!")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)

    #�̹��� ���� (�ٿ�ε�)
    try: # ���� �߻��� ����Ǵ� �ڵ� (urllib.error.URLError: <urlopen error [SSL: WRONG_SIGNATURE_TYPE] wrong signature type (_ssl.c:1002)> ����)
        urllib.request.urlretrieve(bigimg_src, f'��ȭ5_���� �̹��� ũ�Ѹ�/{search}/{search}_{i}.jpg')
    except: # ���� �߻� �ô� �ش� �̹����� �ٿ�ε� ���� �ʴ´�. -> SSL ������ ���� �̹����� �ش� ����Ʈ���� ũ�Ѹ� ���� ���ϵ��� ���� ���̹Ƿ� ũ�Ѹ��ؼ� ����� ��� ������ �� �� ����.
        pass