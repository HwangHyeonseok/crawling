# -*- coding: euc-kr -*-
#slack Ȱ�� �׽�Ʈ - slack ������ �޽��� �������� �غ���
import requests

token = "xoxb-5662516985204-5645537229607-BedaC5Elif1fCTeAioWWHqFM" #Bot User OAuth Token �Է�
channel = "#ũ�Ѹ�����" # channel : Bot�� �ʴ��� "ä�θ�"
texts = "�ȳ� ���� ���̾�! Hello World!" # text : ���� ����

requests.post("https://slack.com/api/chat.postMessage",
              headers={"Authorization": "Bearer "+token},
              data={"channel": channel, "text": texts})