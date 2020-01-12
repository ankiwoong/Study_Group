from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 사분위 수 (중앙값 : 50% 위치의 값)
print(df.quantile(q=0.5))
print('-' * 30)
print(df['영어'].quantile(q=0.5))
