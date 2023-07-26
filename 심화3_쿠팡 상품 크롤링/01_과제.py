# -*- coding: euc-kr -*-
#참고 reference : https://www.dinolabs.ai/163






#과제 : 쿠팡 상품 데이터 수집 전달 건으로 문의드립니다.
#과제 내용 : 안녕하세요. K뱅크 홍보 마케팅 과장 XXX 입니다.
# 본사 제품 판매를 위해 쿠팡 상품 데이터가 필요합니다.
# 아래 키워드 별로 순위, 브랜드명, 제품명, 가격, 상세페이지링크를 엑셀에 저장해 주세요. (1~100위)
# [게이밍 마우스, 기계식 키보드, 27인치 모니터]
# 단, 광고 상품은 제외한다. 브랜드명이 없으면 비워둔다.










import requests
from bs4 import BeautifulSoup
import pyautogui
import time
import openpyxl

rank = 1 # 순위
cur_page = 1 # 현재 페이지

# 엑셀 파일 생성
excel = openpyxl.Workbook()
row = 2 #엑셀의 줄


find_product_count = int(pyautogui.prompt("몇 개의 상품을 찾으시겠습니까?"))
    # 찾으려는 상품 개수만큼 크롤링 진행
for i in range(0,find_product_count,1):
    search = pyautogui.prompt("찾으시려는 상품의 이름을 작성해주세요.")
    ws = excel.create_sheet(f"{search}") # 엑셀 시트 생성
    #엑셀 제목열 추가
    #ws.append(['순위', '브랜드명', '제품명', '가격', '상세페이지'])
    ws['A1'] = "순위"
    ws['B1'] = "브랜드명"
    ws['C1'] = "제품명"
    ws['D1'] = "가격"
    ws['E1'] = "상세페이지"

    for cur_page in range(1,5,1):
    # 쿠팡 사이트가 업데이트 되면서 User-Agent 로만 크롤링하는 것이 불가능해짐. 그래서 header 선언
        main_url = f"https://www.coupang.com/np/search?q={search}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={cur_page}&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
        header = {
            'Host': 'www.coupang.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
        }
        response = requests.get(main_url, headers=header)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        products = soup.select("a.search-product-link") # 상품에 해당하는 코드들이 리스트로 저장됨

        for product in products:
            ad = product.select("span.ad-badge-text") # 광고가 있는 것들을 추출
            bestseller = product.select(".best-seller-search-product-wrap") # 베스트셀러 제품들도 추출
            if(len(ad) > 0 or len(bestseller) > 0): # 광고가 있거나 베스트셀러 제품의 url을 가져오지 않는다.
                continue

            product_url = "https://www.coupang.com" + product.attrs['href'] # 광고가 없는 상품만 상품 url 링크를 가져온다.
            # 상품 상세 사이트로 연결
            response = requests.get(product_url, headers=header) 
            html = response.text
            product_page_soup = BeautifulSoup(html, "html.parser")
            # 순위, 브랜드명, 제품명, 가격, 상세페이지링크 저장
            try:
                brand = product_page_soup.select_one(".prod-brand-name").text.strip()
            except:
                brand = "브랜드 없음"
            try:
                product_name = product_page_soup.select_one(".prod-buy-header__title").text.strip()
            except:
                product_name = "상품 이름 없음"
            try:
                price = product_page_soup.select_one(".total-price").text.strip()
            except:
                pirce = "가격 정보 없음"
            # 상세페이지링크는 product_url 링크

        
            # 100개를 출력했으면 이제 빠져나온다.
            if(rank > 100):
                break

            # 엑셀에 데이터를 쓴다.
            ws[f'A{row}'] = rank
            ws[f'B{row}'] = brand
            ws[f'C{row}'] = product_name
            ws[f'D{row}'] = price
            ws[f'E{row}'] = product_url
            row+=1

            print(rf"순위:{rank} | 브랜드:{brand} | 제품명:{product_name} | 가격:{price}")
            print(f"링크페이지 : {product_url}")
            rank+=1
            

        
    rank = 1 # 한 섹터가 끝나면 다시 순위를 초기화
    row = 2 # 한 섹터가 끝나면 다시 줄을 초기화

#엑셀 저장
excel.save(r"C:\pratice_crolling\심화3_쿠팡 상품 크롤링\S전자 크롤링 과제.xlsx")