from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 결측치 확인
null_data = df.isnull()
null_data2 = df.isna()

print_df(null_data)
print_df(null_data2)
