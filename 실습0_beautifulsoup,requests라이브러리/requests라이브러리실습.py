# ���ϴ� ����Ʈ�� html �ڵ� ��������
import requests

response = requests.get("https://www.naver.com")
html = response.text
print(html)