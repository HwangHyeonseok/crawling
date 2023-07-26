# -*- coding: utf-8 -*-
# --------------------------------------- �䱸 ���� ------------------------------------------------
# ���̹� �α����� �ڵ�ȭ�ϰ� �ͽ��ϴ�.
# ���̹��� �Ѽ� ���̵� �н����带 �ڵ����� �Է��ϰ� �α��� ��ư�� Ŭ�����ִ� ���α׷��� �ۼ����ּ���.

# �ܿ�°� �ƴ�. �׳� �ʿ��� �� ����
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# ũ�� ����̹� �ڵ� ������Ʈ
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

#������ ���� ���� 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ���ʿ��� ���� �޽��� ���ֱ�
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service() # Chrome-for-testing ������ ���� 114->115�� �����ʿ� ���� �ڵ� ����
driver = webdriver.Chrome(service=service, options=chrome_options)

# �������� �ش� �ּ� �̵�
driver.implicitly_wait(5) # �� �������� �ε��� ������ 5�ʴ� ��ٸ���.
driver.maximize_window() # ȭ���� �ִ�ȭ ��Ų��.

driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# ���̵� �Է�â�� ã�´�.
id = driver.find_element(By.CSS_SELECTOR, "#id") #chrome ����̹��� ������ #id(id���� id��) CSS�����ڿ� �´� �±׸� �ڵ����� ã���ش�.

# �� ���̵� �Է�â�� Ŭ�� ����� �ش�.
id.click() # Ŭ��
pyperclip.copy("naver_id") # Ű���� �Է� (�ڽ��� ���̹� id �Է�)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# ��й�ȣ �Է�â�� ã�´�.
pw = driver.find_element(By.CSS_SELECTOR, "#pw") 
pw.click()
pyperclip.copy("naver_pw") # Ű���� �Է� (�ڽ��� ���̹� pw �Է�)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)


# �α��� ��ư�� �����ش�.
login = driver.find_element(By.CSS_SELECTOR, "#log\.login") 
login.click()