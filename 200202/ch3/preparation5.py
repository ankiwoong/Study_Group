from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])
df['프로그래밍'] = [92, 49, 21, 20, None]

# print_df(df)

# 인덱싱 사용 열 삭제
column_del = df.drop(df.columns[4], axis=1)

print_df(column_del)
