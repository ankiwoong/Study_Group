from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])
df['프로그래밍'] = [92, 49, 21, 20, None]

# print_df(df)

# 특정 열만 필터링하여 새로운 데이터 프레임 생성
df2 = df.filter(items=['영어', '프로그래밍'])

print_df(df2)
