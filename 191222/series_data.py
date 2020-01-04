# pandas 모듈에서 series 클래스 가져오기
from pandas import Series

# 기본 시리즈 만들기
# 리스트를 통해 만들 수 있다.
# 즉, 리스트 자료형을 가공하여 생성된 데이터 구조
items = [10, 30, 50, 70, 90]
column = Series(items)

# 특정 조건에 맞는 항목들만 추출
# 이름[이름에 대한 조건식]
# 30 초과인 항목들만 추출
data_serach1 = column[column > 30]
print(type(data_serach1))
print(data_serach1)
print()

# 70 이하 and 10 초과인 항목들만 추출
data_serach2 = column[column <= 70][column > 10]
print(type(data_serach2))
print(data_serach2)
print()

# 10 이하 or 70 이상인 항목들만 추출
data_serach3 = column[(column <= 10) | (column >= 70)]
print(type(data_serach3))
print(data_serach3)
