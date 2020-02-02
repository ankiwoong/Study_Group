from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

null_data = df.isnull()

# 결측치 수 파악
null_data_sum = null_data.sum()

print_df(null_data_sum)
