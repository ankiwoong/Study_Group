from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 전체에 대한 마지막 2줄만 추출
# 파라미터가 없을 경우 5줄이 기본
tail_data = df.tail()
print(tail_data)
print('-' * 30)

tail_data2 = df.tail(2)
print(tail_data2)
