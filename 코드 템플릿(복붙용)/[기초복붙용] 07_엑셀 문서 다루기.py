# -*- coding: euc-kr -*-

from openpyxl import Workbook

# ���� �����ϱ�
excel = Workbook()

# ���� ��Ʈ ����
ws = excel.create_sheet("hyeonseok")

# �ش� ��Ʈ�� �� ������ �߰��ϱ�
ws['A1'] = "����"

# ���� �����ϱ�
excel.save(r"C:\pratice_crolling\��ȭ1_\test.xlsx")

