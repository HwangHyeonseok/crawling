# -*- coding: euc-kr -*-

from openpyxl import Workbook

# ���� �����ϱ�
wb = Workbook()

# ���� ��Ʈ ����
ws = wb.create_sheet("hyeonseok")

# �ش� ��Ʈ�� �� ������ �߰��ϱ�
ws['A1'] = "����"

# ���� �����ϱ�
wb.save(r"C:\pratice_crolling\��ȭ1_\test.xlsx")

