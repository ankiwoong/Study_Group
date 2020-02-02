from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
from sklearn.impute import SimpleImputer
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 결측치 대표값으로 대체
re_null_data = df.fillna(value=0)

print_df(re_null_data)
