# -*- coding: euc-kr -*-
import openpyxl

#���� ���������� ����� ���
fpath = r"C:\pratice_crolling\�ǽ�3_���̽����� ���� �ٷ��\�����̸�.xlsx"

# 1) ���� ���� �ҷ�����
wb = openpyxl.load_workbook(fpath)

# 2) ���� ��Ʈ����
ws = wb['��ũ��Ʈ�̸�']

# 3) ������ �����ϱ� (���������.py�� �Ȱ���)
ws['A3'] = 456
ws['B3'] = '������'

# 4) ���� �� ���� �����ϱ�
wb.save(fpath)
