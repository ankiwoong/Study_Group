from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 딕셔너리 행 추가
df.loc['짱구'] = {'국어': 70, '영어': 60, '수학': 73, '과학': 24}

print_df(df)
