# -*- coding: euc-kr -*-
animals = ['고양이', '강아지', '알파카']

#기존 방법
#i=1
#for animal in animals:
#   print(i , f" : {animal}")
#   i = i+1


# enumerate 방법
for i, animal in enumerate (animals, 1):
    print(i, animal)