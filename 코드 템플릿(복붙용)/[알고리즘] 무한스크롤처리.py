# ���ѽ�ũ��ó�� (�������� ������) �˰��� (���̹� ����)
import time

# ��ũ�� �� ���� : before_height

def scroolDown():
    before_height = driver.execute_script("return window.scrollY")

    while True:
        # �� �Ʒ��� ��ũ���� ������. (END Ű�� ���� ��ũ���� ������.)
        driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
        # ��ũ�� �Ǵ� ���� �ε� �ð��� �ش�.
        time.sleep(1)
        # ��ũ�� �� ���� üũ
        after_height = driver.execute_script("return window.scrollY")
        
        if after_height == before_height: # ������ ���� ��� ���� window.ScrollY ��ġ�� ���� ��ġ�� ����.
            break # �� ��쿡�� Ż���Ѵ�.

        before_height = after_height