# -*- coding: euc-kr -*-

#1. 폴더 생성
import os

#동일한 폴더가 이미 있으면 그냥 넘어간다.     #새로운 폴더라면 생성해준다.
if not(os.path.exists("심화4_네이버 이미지 크롤링/폴더명")): 
    os.mkdir("심화4_네이버 이미지 크롤링/폴더명")