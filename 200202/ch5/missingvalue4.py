from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

null_data_del = df.dropna()

# 결측치 갯수 확인
print_df(null_data_del.isnull().sum())
