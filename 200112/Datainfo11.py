from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 합계
print(df.sum())
print('-' * 30)
print(df['영어'].sum())
