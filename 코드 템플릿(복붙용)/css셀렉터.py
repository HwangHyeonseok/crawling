# CSS 셀렉터 모음

# 1) id와 class 속성으로 가져오기
# | # - id  | . - class 

# 2) class나 id 태그가 아닐 경우 기타 속성들로 가져오기
# Ex. tr[onmouseover="mouseOver(this)"] # tr 태그의 onmouseover 속성이 mouseOver(this) 인 것을 가져온다.

# 3) 바로 자식의 요소를 지칭하기 : > 사용
# nth-child : 모든 자식의 순서에서 찾음 | nth-of-type: 해당하는 자식 태그 요소에서의 순서를 찾음
# Ex. div#metadata-line>span:nth-of-type(2) 은, div 태그의 id 속성값이 metadata-line인 것의 바로 하위 자식의 span 태그 요소의 순서가 두 번째인 것을 가져온다.
# Ex. tr[onmouseover="mouseOver(this)"] > :nth-child(2) 은, tr 태그의 onmouseover 속성값이 mouseOver(this)인 것의 바로 하위 자식의 태그 요소 상관 없이 순서가 두 번째인 것을 가져온다.