# -*- coding: euc-kr -*-

# ���� ���? ũ�Ѹ��� ���뿡�� �ֿ��ϰ� ����� Ű���尡 �������� �м��غ��� ������!

import pyautogui
import pyperclip

# ��ü ���� ���� ��Ƶδ� ����
total_content = "" 

pyperclip.copy(total_content) # ��ü ���� ������ Ŭ������ �ȿ��� �ٿ��־��ش�. (���� ���簡 �Ǿ����Ƿ� ���� Ctrl+V�� �ٿ��ֱ⸸ ���ָ� �ȴ�.)
pyautogui.alert("Ŭ�����忡 ���� ����Ǿ����ϴ�.")


# Ŭ�� ���尡 ���簡 �Ǿ�����, 
# 1) ���ۿ� "���ڸ��� ���ڼ� ����" �˻� �Ǵ� https://www.jobkorea.co.kr/service/user/tool/textcount ����Ʈ �湮 => Ctrl + V �� ���ڼ��� 100,000�ڰ� ���� �ʵ��� ����
# 2) ���ۿ� "WordItOut" �˻� �Ǵ� https://worditout.com/word-cloud/create ����Ʈ �湮 => Ctrl + V �� Ű���� �м�
