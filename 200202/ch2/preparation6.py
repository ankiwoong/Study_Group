from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 인덱싱을 이용 삭제
del_df = df.drop(df.index[0])

print_df(del_df)
