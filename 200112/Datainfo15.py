from pandas import DataFrame
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 사분위 수 이외 (90% 위치 = 상위 10%)
print(df.quantile(q=0.9))
print('-' * 30)
print(df['수학'].quantile(q=0.9))
