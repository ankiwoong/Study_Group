from pandas import DataFrame
from Data import grade_list
from Data import grade_dic

# 각각의 데이터 열의 값과 타입 조회
# 각 열의 자료형 -> Series(DataFrame = Series의 모음)
df = DataFrame(grade_list)
print(df[0])
print(type(df[0]))
print('-' * 30)
print(df[1])
print(type(df[1]))