# -*- coding: euc-kr -*-
# ---------------------- �䱸 ���� -------------------------------
# ������� ȣ�� ���� ����Ʈ���� ȣ���� ������ �Ǿ� ��� F5�� ���� �ܼ��� ����͸��ؾ� �մϴ�.
# ������ ����͸��� �ϱ� �����Ƽ� �ܼ��� ���� �� �ڵ����� slack�� ���� �˸��� �����ִ� ���α׷��� �����Ϸ��� �մϴ�.

# ----------------------- Point ----------------------------
# 1. post ��û
# 2. Status Code 303 -> redirection�̶�? 
#=> ��û�� �ְ� ������ �޾Ƽ� �ٸ� url�� �������� ������ ��
# 3. slack �˸� ������
# 4. �Է��� �� �����ʹ� �����ڵ����� Payload �ǿ��� Ȯ���� �����ϴ�.

# ---------------------- �ڵ� -------------------------------
import requests
from bs4 import BeautifulSoup

url = "https://www.toyoko-inn.com/korea/search"
form_data = {
"lcl_id": "ko",
"prcssng_dvsn": "dtl",
"sel_area_txt": "�ѱ�",
"sel_htl_txt": "������� ���ﰭ��",
"chck_in": "2023/08/15",
"inn_date": "1",
"sel_area": "8",
"sel_htl": "00282",
"rsrv_num": "1",
"sel_ldgngPpl": "1"
}

response = requests.post(url, data=form_data)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
beds = soup.select("ul.btnLink03 > li")

for i, bed in enumerate (beds, 1):
    no_room = bed.select('a')
    reserve_ok_room = "�ڸ� O"
    if len(no_room) == 0: #�ܽ��� ���� ���
        reserve_ok_room = "�ڸ� X"

    # �л� ���� �̺�Ʈ �̱۷�
    if i==1 or i==2:
        print(f"�л� ���� �̺�Ʈ �̱۷� : {reserve_ok_room}")
    # �̱۷�
    elif i==3 or i==4:
        print(f"�̱۷� : {reserve_ok_room}")
    # �����
    elif i==5 or i==6:
        print(f"����� : {reserve_ok_room}")
    # Ʈ����
    elif i==7 or i==8:
        print(f"Ʈ���� : {reserve_ok_room}")
    # Ʈ���÷�
    elif i==9 or i==10:
        print(f"Ʈ���÷� : {reserve_ok_room}")
    # ��ƮǮƮ����
    elif i==11 or i==12:
        print(f"��ƮǮƮ���� : {reserve_ok_room}")
        