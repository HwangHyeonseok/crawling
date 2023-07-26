# -*- coding: euc-kr -*-
# ���̹� �ֽ����簡 ũ�Ѹ� �ϱ�
# ���ϴ� �ֽ����� �ڵ带 �Է��ϸ� �ֽ����� �ڵ忡 �´� �ֽ����簡�� ��µǵ��� �Ѵ�.
# ��, ��� ���´� 77,400(string��) �� �ƴ� 77400(int��) ���� ��µǵ��� �Ѵ�.

import requests
from bs4 import BeautifulSoup
import pyautogui

search = pyautogui.prompt("���簡�� Ȯ���� �ֽ� ������ �ڵ带 �ۼ����ּ���. ")

url = f"https://finance.naver.com/item/sise.naver?code={search}"

# 1. �ش� url�� ���ؼ� ��û�� �Ѵ�. ������ response ��ü�� ��´�.
response = requests.get(url)

# 2. response ��ü�� text�� ������ ���� �� �������� html �ڵ尡 �ȴ�.
html = response.text

# 3. html �ڵ� ���ڿ������� �Ľ��� �ϱⰡ �����Ƿ� ���������� beautifulsoup�� ����Ͽ� �Ľ��Ѵ�.
# �Ľ��� ���� soup ��ü�� ��´�.
soup = BeautifulSoup(html, "html.parser")

# 4. id ���� _nowVal �� �ڵ带 ��� ������ ������ text�� ���� �����Ͽ� �����Ѵ�.
price = soup.select_one("#_nowVal").text

# 5. ���� price�� 71,900 ó�� ���ڿ��� �Ǿ� �ִ�. ',' �� ���ֱ� ���ؼ� ������ ���� �۾��� �Ѵ�.
# ��ü�� ���� => , ��ü �� ���� => �� ĭ
# ��, replace�� "���ڿ� ��ü �Լ�"�̰� ','�� �ִ� �κ��� '' ���� �ٲ۴�.
# ex. 47,900 -> 47900
price= price.replace(',', '')

print(price)
