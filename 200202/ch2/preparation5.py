from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 행 여러개 삭제
del_df = df.drop(['이슬이', '퉁퉁이', '도라에몽'])

print_df(del_df)
