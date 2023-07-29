# -*- coding: euc-kr -*-

# �����Ͽ� 4 �⺻ ���� ���� (3~22��)
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

service = Service() # chrome-for-testing ������ ���� ����Ǵ� �ڵ�
#service = Service(executable_path=ChromeDriverManager(version="114.0.5735.90").install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# �������� �ش� �ּ� �̵�
driver.get("https://naver.com/")
driver.implicitly_wait(5) # webpage�� �ε� �� ������ �ִ� 5�ʱ��� ��ٷ��ش�. 

# ���� �޴� Ŭ�� - Ŭ������ "service_icon type_shopping"�� ���� �����´�. 
#���� ���ᵵ .���� �Ѵ�.
driver.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping").click()
# ���ο� ������ �̵� - ���� refernce : https://m.blog.naver.com/kiddwannabe/221449593300
driver.switch_to.window(driver.window_handles[1])
time.sleep(3) # ���α׷� ��ü�� 3�� ���

# �˻�â �Է� - input �±׸� ������ + Ŭ���� �̸��� "input._searchInput_search_text_3CUDs"�� ���� �����´�.
search = driver.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# �˻��� �Է�
search.send_keys('������ 13')
search.send_keys(Keys.ENTER)
time.sleep(10) # 10�� ��� 

# ���� ������� �� ����
driver.close()

# ���� ������ �̵�
driver.switch_to.window(driver.window_handles[0])