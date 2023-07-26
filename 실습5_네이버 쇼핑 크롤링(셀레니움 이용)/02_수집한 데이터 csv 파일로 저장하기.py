# -*- coding: euc-kr -*-

# Quiz : ���̹� ���� �������� ���� ��ǰ��, ����, ��ũ ������ ũ�Ѹ��ϴ� �ڵ带 �ۼ��Ͻÿ�.
# �̶� ���α׷� ������� �Է��� �޾� ��ǰ�� �˻��մϴ�.
# ���� : ���α׷� ���� �� '�����'�� �Է��ϸ� �ڵ����� ���̹� ���� â�� ��� ����� ��ǰ�� ��ǰ��, ����, ��ũ ������ ũ�Ѹ��Ͽ� ����Ѵ�.

# �����Ͽ� 4 �⺻ ���� ���� (3~22��)
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv

# ũ�� ����̹� �ڵ� ������Ʈ
from webdriver_manager.chrome import ChromeDriverManager


# ������� �Է� �ޱ� - � ���� �˻��ұ��?
find = pyautogui.prompt("� ���� �˻��ұ��?")

#������ ���� ���� 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ���ʿ��� ���� �޽��� ���ֱ�
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service()
browser = webdriver.Chrome(service=service, options=chrome_options)

# �������� �ش� �ּ� �̵�
browser.get("https://www.naver.com")
browser.implicitly_wait(5) # webpage�� �ε� �� ������ �ִ� 5�ʱ��� ��ٷ��ش�. 

# css �����ڰ� span �±��̰� + Ŭ���� �̸��� "service_icon type_shopping"�� ���� Ŭ���Ѵ�.
browser.find_element(By.CSS_SELECTOR, "span.service_icon.type_shopping").click()

# Ŭ���ϸ� target="_blank" �ڵ� ������ �� â���� ������ �ȴ�.
# ���� ���� ���������� �۾��ϵ��� �۾� â�� �������ش�. 
# �̶� browser.window_handles[0]�� ������ ������ ���̹� â
# browser.window_handles[1]�� �̹��� ���� ���̹� ���� â�̴�.
browser.switch_to.window(browser.window_handles[1])

# �������� �ѱ� ������ �������� �ε� �� ������ ������ش�.
browser.implicitly_wait(5) # �ִ� 5�ʱ��� ���

# css �����ڰ� input �±��̰� + Ŭ���� �̸��� _searchInput_search_text_3CUDs �� ���� Ŭ���Ѵ�.
search =browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# ����ڿ��� �Է¹޾Ҵ� �˻�� �Է��Ѵ�.
search.send_keys(find)
search.send_keys(Keys.ENTER)
browser.implicitly_wait(10) # ������ �ε��� ������ ��� (�ִ� 10�� ���)

#------------------ ��ǰ��, ����, ��ũ ������ ũ�Ѹ� --------------------------------------


# ��ũ�� �� ���� Ȯ�� 
before_height = browser.execute_script("return window.scrollY")
# 1) ���� ��ũ�� (������ ������ ������)
while True:
    # �� �Ʒ��� ��ũ���� ������. (END Ű�� ���� ��ũ���� ������.)
    browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    # ��ũ�� �Ǵ� ���� �ε� �ð��� �ش�.
    time.sleep(1)
    # ��ũ�� �� ���� üũ
    after_height = browser.execute_script("return window.scrollY")
    
    if after_height == before_height: # ������ ���� ��� ���� window.ScrollY ��ġ�� ���� ��ġ�� ����.
        break # �� ��쿡�� Ż���Ѵ�.

    before_height = after_height

#���� ���� 
# (C:\pratice_crolling\�ǽ�5_���̹� ���� ũ�Ѹ�(�����Ͽ� �̿�)�� 02_data.csv ���� ����)
# 'w' -> ���� ���� ����. # ���ڵ� Ÿ���� CP949�̴�. # �ٹٲ� ���ڸ� ���ش�.
f = open(r"C:\pratice_crolling\�ǽ�5_���̹� ���� ũ�Ѹ�(�����Ͽ� �̿�)\02_data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)


# 2) ��ü ��ǰ ũ�Ѹ�
# a �±� + Ŭ���� �̸��� product_link__TrAac linkAnchor �� �ڵ带 ��� �����´�.
products = browser.find_elements(By.CSS_SELECTOR, "div.product_inner__gr8QR")

for product in products:
    name = product.find_element(By.CSS_SELECTOR, "a.product_link__TrAac.linkAnchor").text # ��ǰ �̸�
    try: # �±װ� span�̰� Ŭ������ price_num__S2p_v �� ���� �ؽ�Ʈ�� ã�� �� �ִ� ���
        price = product.find_element(By.CSS_SELECTOR, "span.price_num__S2p_v").text # ����
    except: # ã�� �� ���� ��쿡�� ����ó��
        price = "�Ǹ��ߴ�"
    link = product.find_element(By.CSS_SELECTOR, "a.product_link__TrAac.linkAnchor").get_attribute('href') # ��ũ ���� (href �Ӽ����� �����´�.)

    print(f"��ǰ�� : {name}, ���� : {price}, ���� ����Ʈ : {link}")
    
    # csv ���Ͽ� �� ���� �߰��Ͽ� ������ ����
    csvWriter.writerow([name, price, link])

f.close() # ���� �ݱ�

