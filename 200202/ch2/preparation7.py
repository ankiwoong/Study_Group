from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 슬라이싱 사용 삭제
del_df = df.drop(df.index[2:5])

print_df(del_df)
