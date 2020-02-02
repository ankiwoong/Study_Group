from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 결측치 모든 열 삭제
null_data_del = df.dropna(axis=1)

# 결측치 갯수 확인
print_df(null_data_del.isnull().sum())
