from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 새로운 열 같은값으로 추가
df['프로그래밍'] = 100

print_df(df)
