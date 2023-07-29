# -*- coding: euc-kr -*-
# ---------------------- �䱸 ���� -------------------------------
# �һ���� ��� �м� ���񽺿� �ʿ��� ���α׷� ����

# ����ڿ��� �˻�� �Է� �ް�, ���̹� ������ ǥ�õǴ� ������� 
#����, ���Ը�, ����, �湮�ڸ������ ������ �����ϴ� ���α׷��� ������ּ���. (1��������)

# �˻��� ���� : [������ ����], [ȫ�� ����], [���¿� ī��] - [���� + ����]
# !����� �������ּ���.
# !������ ���� ���Դ� �������ּ���.
# !�湮�� ���䰡 ���ٸ� 0���� ǥ�����ּ���.

# ���� ��� "���� ȣ��" �˻� �� 1�������� �ִ� ���� �����鸸 �������� �˴ϴ�.
# ----------------------- Point ----------------------------
# 1. iframe �±� ������ �� ��ó ���
# 2. ���� ��ũ�� ó�� ����� ����غ���.

# �����Ͽ� ��� -> ��ũ�� �ÿ��� ����Ʈ �ּҰ� �ٲ��� ����. (���� ����Ʈ��� �Ǻ�)
# ---------------------- �ڵ� -------------------------------
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyautogui
import openpyxl

search = pyautogui.prompt("���̹� ���� ũ�Ѹ� ���α׷��Դϴ�. �˻�� �Է����ּ���. (���� + ����)")

# ���� ���� ����� + ��Ʈ �����
wb = openpyxl.Workbook()
ws = wb.create_sheet(f"{search} �˻� ���")
# ���� �� �ʺ� ����
ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 50
ws.column_dimensions['C'].width = 10
ws.column_dimensions['D'].width = 25
# ���� ���� �߰�
ws.append(["���� ����", "���Ը�", "����", "�湮�� ���� ��"]) 

url = f"https://map.naver.com/v5/search/{search}?c=15,0,0,0,dh"    

# ũ�� ����̹� �ڵ� ������Ʈ
from webdriver_manager.chrome import ChromeDriverManager

#������ ���� ���� 
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ���ʿ��� ���� �޽��� ���ֱ�
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service() # chrome-for-testing ������ ���� ����Ǵ� �ڵ�
driver = webdriver.Chrome(service=service, options=chrome_options)

# iframe ���� ��ũ���� ������ ���
# 1) iframe ���� �� �� Ŭ��
# 2) ���� li ���� Ȯ��
# 3) ��ũ���� ������
# 4) ���� li ���� ��ȭ Ȯ�� (��ȭ �� �� ������ �Ǵ°Ű� ��ȭ�� ������ ������ ���ȴٴ� �ǹ�)
def scroolDown():
    driver.find_element(By.CSS_SELECTOR, "#_pcmap_list_scroll_container").click() # 1) iframe ���� �� ���� Ŭ���Ѵ�.
    before_li = len(driver.find_elements(By.CSS_SELECTOR, "li.UEzoS.rTjJo")) # 2)
    while True:
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END) # 3)
        time.sleep(2)
        after_li = len(driver.find_elements(By.CSS_SELECTOR, "li.UEzoS.rTjJo")) # 4)

        if(before_li == after_li): # ������ ���� ���
            break
        
        before_li = after_li
    

# �������� �ش� �ּ� �̵�
driver.get(url)
driver.maximize_window() # ������ â �ִ�ȭ
driver.implicitly_wait(5) # webpage�� �ε� �� ������ �ִ� 5�ʱ��� ��ٷ��ش�. 

# iframe ������ ���� - �ش� iframe ���� �̵� <iframe> �±� ��ó 
driver.switch_to.frame("searchIframe")
time.sleep(1)

# iframe ���� ��ũ���� ��� ������.
scroolDown()

driver.implicitly_wait(0) # �����͸� ������ ����ϱ� ���ؼ� ���� �ڵ� - �����͸� ��ٷ��ִ� �ð��� 0���� ���ش�.( ��� �ð� : 0�� )

shops = driver.find_elements(By.CSS_SELECTOR, "li.UEzoS.rTjJo")

rank = 1 # ���� ����
for shop in shops:
    try: # ���� �ִ� ��� ������� �ʴ´�.
        ad = shop.find_element(By.CSS_SELECTOR, "a.gU6bV.mdfXq") # ���� �ִ� ���
        continue
    except:
        pass
    
    try:
        subject = shop.find_element(By.CSS_SELECTOR, "span.place_bluelink.TYaxT").text #���Ը�
    except: # ���Ը��� ���� ��� ���(����)���� �ʴ´�.
        continue
    try: 
        star_score = shop.find_element(By.CSS_SELECTOR, "span.h69bs.a2RFq").text # ����
        star_score = star_score.replace("����\n", "") # "����\n"�� ���� ���
    except: # ������ ���� ��� ���(����)���� �ʴ´�.
        continue
    try: 
        review = shop.find_element(By.CSS_SELECTOR, 'span.h69bs:not([class*=" "])').text # ���� ��
        review = review.replace("���� ", "") # "���� " �κ��� ���� ���
    except: # ������� ���� ��� 0���� ����Ѵ�.
        review = 0

    print(f"���� ���� : {rank} ���� : {subject}, ���� : {star_score}, ���� �� : {review}")
    ws.append([rank, subject, star_score, review])
    rank += 1

# ���� ����
wb.save(rf"C:\pratice_crolling\��ȭ8_���̹� ���� ũ�Ѹ�\{search}�˻� ���.xlsx")

    