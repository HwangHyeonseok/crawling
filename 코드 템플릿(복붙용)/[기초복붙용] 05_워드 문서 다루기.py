# -*- coding: euc-kr -*-
from docx import Document

# 1. ���� �����ϱ�
document = Document()

# 2. ���� ������ �߰��ϱ� # add_heading�� ����, add_paragraph�� ���� ����
document.add_heading('��� ����', level=0)
document.add_paragraph('��� ��ũ')
document.add_paragraph('��� ����')

# 3. ���� �����ϱ�
document.save(r"C:\pratice_crolling\��ȭ1_\test.docx")