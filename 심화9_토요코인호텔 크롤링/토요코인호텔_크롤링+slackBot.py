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
import time

#slack Ȱ�� �׽�Ʈ - slack ������ �޽��� �������� �غ���
token = "xoxb-5662516985204-5645537229607-BedaC5Elif1fCTeAioWWHqFM" #Bot User OAuth Token �Է�
channel = "#ũ�Ѹ�����" # channel : Bot�� �ʴ��� "ä�θ�"

def send_passage(texts):
    requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel, "text": texts})

url = "https://www.toyoko-inn.com/korea/search" # POST ��û�� �� ������ Request URL (������ ���� F12 > Headers > Request URL Ȯ��)
form_data = { # POST ��û�� �� ������ Form ������ ���� (������ ���� F12 > Payload > Form Data Ȯ��)
"lcl_id": "ko",
"prcssng_dvsn": "dtl",
"sel_area_txt": "�ѱ�", #������ ����
"sel_htl_txt": "������� ���ﰭ��", # ������ ��
"chck_in": "2023/07/31", # üũ�� ��¥
"inn_date": "1",
"sel_area": "8",
"sel_htl": "00282",
"rsrv_num": "1",
"sel_ldgngPpl": "1"
}


attempt = 1 # �õ� Ƚ��

while True: 
    try:
        print(f'{attempt} ��° �õ��Դϴ�.')
        response = requests.post(url, data=form_data)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        beds = soup.select("ul.btnLink03 > li")

        for i, bed in enumerate (beds, 1):
            no_room = bed.select('a')
            if len(no_room) >= 1: #�ܽ��� �ִ� ���
            # �л� ���� �̺�Ʈ �̱۷�
                if i==1 or i==2:
                    send_passage(f"�л� ���� �̺�Ʈ �̱۷뿡 �ܽ��� �ֽ��ϴ�.")
                    print(f"�л� ���� �̺�Ʈ �̱۷뿡 �ܽ��� �ֽ��ϴ�.")
                # �̱۷�
                elif i==3 or i==4:
                    send_passage(f"�̱۷뿡 �ܽ��� �ֽ��ϴ�.")
                    print(f"�̱۷뿡 �ܽ��� �ֽ��ϴ�.")
                # �����
                elif i==5 or i==6:
                    send_passage(f"����뿡 �ܽ��� �ֽ��ϴ�.")
                    print(f"����뿡 �ܽ��� �ֽ��ϴ�.")
                # Ʈ����
                elif i==7 or i==8:
                    send_passage(f"Ʈ���뿡 �ܽ��� �ֽ��ϴ�.")
                    print(f"Ʈ���뿡 �ܽ��� �ֽ��ϴ�.")
                # Ʈ���÷�
                elif i==9 or i==10:
                    send_passage(f"Ʈ���÷뿡 �ܽ��� �ֽ��ϴ�.")
                    print(f"Ʈ���÷뿡 �ܽ��� �ֽ��ϴ�.")
                # ��ƮǮƮ����
                elif i==11 or i==12:
                    send_passage(f"��ƮǮƮ���뿡 �ܽ��� �ֽ��ϴ�.")
                    print(f"��ƮǮƮ���뿡 �ܽ��� �ֽ��ϴ�.")

    except:
        print("���� �߻�!")
    
    time.sleep(10)
    attempt += 1