# -*- coding: euc-kr -*-
# �ֽ� ���簡�� ũ�Ѹ��Ͽ� �����ͼ� '�����̸�.xlsx' ���� ���Ͽ� B2, B3, B4�� ���簡�� ä������.

import openpyxl
import requests
from bs4 import BeautifulSoup

#�����̸�.xlsx ��θ� ����ȭ
fpath = r"C:\pratice_crolling\�ǽ�3_���̽����� ���� �ٷ��\�����̸�.xlsx"

# �����̸�.xlsx ���� ���� �ҷ�����
excel = openpyxl.load_workbook(fpath)

# ������ ��ũ��Ʈ �����ϱ�
worksheet = excel['�ֽ���Ȳ']
 
# �����͸� ũ�Ѹ��ϱ�
stocks = ['005930', '000660', '035720']
row = 2
for stock in stocks:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={stock}")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("#_nowVal").text
    # 71,900 -> 71900 �� �ٲٱ� ���ؼ� ���ڿ� ���¸� �ٲ۴�. (',' -> '')
    price = price.replace(',', '')
    #(ũ�Ѹ��� �����ʹ� price�� ����ִ�.)
    print(price)
    
    # ũ�Ѹ��� �����͸� ���� ���� [B2]~[B4]���� �ֱ�
    worksheet[f'B{row}'] = int(price)
    row = row+1

#���� �� ���� ���� ����
excel.save(fpath)

