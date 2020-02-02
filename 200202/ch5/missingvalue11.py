from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
from sklearn.impute import SimpleImputer
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 결측치 규칙 정의
null_regulation = SimpleImputer(
    missing_values=numpy.nan, strategy='most_frequent')

# 결측치 규칙 적용
df_null_regulation = null_regulation.fit_transform(df.values)

# 결측치 규칙 적용 데이터 프레임 생성
df2 = DataFrame(df_null_regulation, index=df.index, columns=df.columns)

print_df(df2)