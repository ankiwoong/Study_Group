from pandas import DataFrame, Series
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# Series를 사용하여 열 추가
df['프로그래밍'] = Series([70, 40, 20, 38], index=['노진구', '이슬이', '비실이', '퉁퉁이'])

print_df(df)
