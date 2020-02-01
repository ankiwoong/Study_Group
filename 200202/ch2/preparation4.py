from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 행 삭제(결과 반영된 복사본 생성)
del_df = df.drop('노진구')

print_df(del_df)
