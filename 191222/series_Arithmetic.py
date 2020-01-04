# pandas 모듈에서 series 클래스 가져오기
from pandas import Series

# 인덱스를 직접 지정하면서 시리즈 만들기
# 지난주 주말 매출
last_week = Series([240000, 140000], index=['sat', 'sun'])
# 이번주 주말 매출
this_week = Series([124000, 400200], index=['sun', 'sat'])

# 객체의 사칙 연산
# index가 동일한 항목끼리 연산이 수행된다.
merge = last_week + this_week
print(type(merge))
print(merge)
