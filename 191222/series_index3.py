# pandas 모듈에서 series 클래스 가져오기
from pandas import Series

# 인덱스를 직접 지정하면서 시리즈 만들기
# 지난주 주말 매출
last_week = Series([240000, 140000], index=['sat', 'sun'])
# 이번주 주말 매출
this_week = Series([124000, 400200], index=['sun', 'sat'])

print(type(last_week))
print(last_week)
print()
print(type(this_week))
print(this_week)
