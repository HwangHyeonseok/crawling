# -*- coding: euc-kr -*-
animals = ['�����', '������', '����ī']

#���� ���
#i=1
#for animal in animals:
#   print(i , f" : {animal}")
#   i = i+1


# enumerate ���
for i, animal in enumerate (animals, 1):
    print(i, animal)