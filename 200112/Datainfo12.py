from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 평균
print(df.mean())
print('-' * 30)
print(df['수학'].mean())
