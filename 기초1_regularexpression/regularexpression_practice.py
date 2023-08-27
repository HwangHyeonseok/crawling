import re

# 1. 정규식 선언
p = re.compile("ca.e") # 정규식 : ca.e

# 기본적으로 주어진 문자의 처음부터 순서대로 읽으면서 매치가 되는지 체크한다. (careless 예시 참조)

# < 정규식 >
# . (ca.e) : 하나의 문자를 의미 > care, cafe, careless | good care, caffe (X) 
# ^ (^de) : 문자열의 시작 > desk, destin, deok | doeg (X)
# $ (se$) : 문자열의 끝 > base, case, okse | cases (X)


# 2. 매칭이 되는지 체크 (case(문자열)와 정규식과 매칭이 되는가? => 매칭이 되면 객체를 반환, 매칭이 되지 않으면 에러 발생)
# m = p.match("비교할 문자열") #주어진 문자열에서 처음부터 일치하는지 확인
# m = p.search("비교할 문자열") #주어진 "문자열 중에 일치하는게 있는지" 확인
# lst = p.findall("비교할 문자열") # 일치하는 모든 것을 리스트 형태로 반환해준다.

# 3. 원하는 출력 형태로 출력
def check_match(m):
    if m:
        print(m.group()) # 일치하는 문자열을 반환
        print(m.string) # 입력받은 문자열을 그대로 반환
        print(m.start()) # 일치하는 문자열의 시작 인덱스를 반환
        print(m.end()) # 일치하는 문자열의 끝 인덱스를 반환
        print(m.span()) # 일치하는 문자열의 시작 / 끝 인덱스를 함께 반환

    else :
        print("매칭 되지 않았습니다.")


m = p.match("good care") #주어진 문자열에서 처음부터 일치하는지 확인
check_match(m)

m = p.search("good care") #주어진 "문자열 중에 일치하는게 있는지" 확인
check_match(m)

lst = p.findall("good care cafe") # 일치하는 모든 것을 리스트 형태로 반환
print(lst) #['care', 'cafe']
