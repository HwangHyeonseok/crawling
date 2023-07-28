# -*- coding: euc-kr -*-
# ---------------------- �䱸 ���� -------------------------------
# ���򰡵� �ֽ��� ã�� ���� ũ�Ѹ� ���α׷��� ������� �մϴ�.
# ���̹� ���� ���������� �ð��Ѿ��� Ŭ���ϸ� ������ �������� �ɼǿ���,
# PER(��), ROE(%), PBR(��), ������(%) ���� ������ �ϳ��� ���� ���Ϸ� �����ϴ� ���α׷��� �������ּ���.
# PER, ROE, PBR, �������� �����Ͱ� N/A�� ��� �ش� �����͸� ��� ���� ������ �������ּ���.

# ��, �����Ͽ��� �����ϱ�, �ݵ�� requests�� BS4�� �̿��Ͽ� �������ּ���.




















# ----------------------- Point ----------------------------
# 1. �±׿� id�� class�� ���� ��� ������ ��������
# 2. ǥ �����ʹ� ��� �����ñ�?
# 3. requests�� get ��û ��Ʈ��ũ �м�
# ---------------------- �ڵ� -------------------------------
import requests
from bs4 import BeautifulSoup
import pyautogui
import openpyxl

# ����� �Է� - �� ���� ������ ���� ����ڷκ��� �Է¹޴´�.
view_stocks = int(pyautogui.prompt("�ð��Ѿ� ����/PER/ROE/PBR/�������� ��ȸ�մϴ�. �� ���� ������ ��ȸ�Ͻðڽ��ϱ�?"))
viewed_stocks = 0
lastpage = (view_stocks // 50) + 1 # 50������ �� ������
print(lastpage)
marketcap_rank = 1

# ���� ���� �����
wb = openpyxl.Workbook()
# ���� ��ũ��Ʈ �����
ws = wb.create_sheet('�ڽ��� �ð��Ѿ� ���� ���� �м�')
# ���� 1�� (���� �߰�)
ws.append(["�ð��Ѿ� ����", "�����", "PER", "ROE", "PBR", "������"])


for page in range(1, lastpage+1, 1):
    # request URL�� �޾ƿ� ��� �ݵ�� �� �ּ� �״�� ���� ���� �ƴ϶�,
    # ���ۿ��� url decode �� �˻��ؼ� decode �� �ּҸ� ����ؾ� �Ѵ�.
    url = f"https://finance.naver.com/sise/field_submit.naver?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.naver?page={page}&fieldIds=per&fieldIds=roe&fieldIds=pbr&fieldIds=reserve_ratio"

    # get ��û���� url�� �޾ƿ´�.
    response = requests.get(url, headers={'User-Agent' : 'Mozila/5.0'})
    html = response.text

    # parser : ���� ������ �� �ҷ��´�.
    soup = BeautifulSoup(html, 'html.parser')

    stocks = soup.select('tr[onmouseover="mouseOver(this)"]') # tr �±��� onmouseover �Ӽ��� mouseOver(this) �� ���� �����´�.


    for stock in stocks: # marketcap_rank�� �ð��Ѿ� ����
        if view_stocks < viewed_stocks: # �Է¹��� ������ŭ ��� ��ȸ�� ��� 
            break
        subject = stock.select_one('tr[onmouseover="mouseOver(this)"] > td:nth-child(2)').text
        per = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(7)').text
        roe = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(8)').text
        pbr = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(9)').text
        reserve_ratio = stock.select_one('tr[onmouseover="mouseOver(this)"] > :nth-child(10)').text
        if subject != 'N/A' and per != 'N/A' and roe != 'N/A' and pbr != 'N/A' and reserve_ratio != 'N/A':
            print(f"{marketcap_rank} : ����� : {subject} PER : {per} ROE : {roe} PBR : {pbr} ������ : {reserve_ratio}")
            ws.append([marketcap_rank, subject, per, roe, pbr, reserve_ratio]) # ������ ������ �߰�
            viewed_stocks +=1

        marketcap_rank +=1

#���� ����        
wb.save(rf'C:\pratice_crolling/��ȭ7_���̹� �ֽ� ũ�Ѹ�/�ð��Ѿ� {view_stocks}�� ���� �м� ���.xlsx')