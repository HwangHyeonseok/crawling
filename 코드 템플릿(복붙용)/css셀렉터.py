# CSS ������ ����

# 1) id�� class �Ӽ����� ��������
# | # - id  | . - class 

# 2) class�� id �±װ� �ƴ� ��� ��Ÿ �Ӽ���� ��������
# Ex. tr[onmouseover="mouseOver(this)"] # tr �±��� onmouseover �Ӽ��� mouseOver(this) �� ���� �����´�.

# 3) �ٷ� �ڽ��� ��Ҹ� ��Ī�ϱ� : > ���
# nth-child : ��� �ڽ��� �������� ã�� | nth-of-type: �ش��ϴ� �ڽ� �±� ��ҿ����� ������ ã��
# Ex. div#metadata-line>span:nth-of-type(2) ��, div �±��� id �Ӽ����� metadata-line�� ���� �ٷ� ���� �ڽ��� span �±� ����� ������ �� ��°�� ���� �����´�.
# Ex. tr[onmouseover="mouseOver(this)"] > :nth-child(2) ��, tr �±��� onmouseover �Ӽ����� mouseOver(this)�� ���� �ٷ� ���� �ڽ��� �±� ��� ��� ���� ������ �� ��°�� ���� �����´�.

# 4) Ŭ���� ���� "��Ȯ��" ��ġ�ϴ� ��쿡�� ��������
# Ex. span.h69bs:not([class*=" "]) ��, span �±��� Ŭ���� ���� "h69bs"�� �͸� �����´�.