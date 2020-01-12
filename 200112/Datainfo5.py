from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 특정 열에 대한 마지막 2줄
print(df['영어'].tail(2))
