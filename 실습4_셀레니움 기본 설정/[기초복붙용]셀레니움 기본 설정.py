# -*- coding: utf-8 -*-

# �ܿ�°� �ƴ�. �׳� �ʿ��� �� ����
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# ũ�� ����̹� �ڵ� ������Ʈ
from webdriver_manager.chrome import ChromeDriverManager

#������ ���� ���� 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ���ʿ��� ���� �޽��� ���ֱ�
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install()) # Chrome-for-Testing ������ 114->115�� �����ʿ� ���� ������ �ڵ� (20230725)
browser = webdriver.Chrome(service=service, options=chrome_options)

# �������� �ش� �ּ� �̵�
browser.get("https://www.naver.com")