from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 삭제 결과 원본 반영
# drop() -> 원본 수정 x / 복사본 반영
# inplace -> True : 원본 자체 삭제
df.drop(['노진구', '퉁퉁이'], inplace=True)

print_df(df)
