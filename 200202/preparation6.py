from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 특정 열 오름차순
df.sort_values('국어', inplace=True)

# 오름차순 후 출력
print_df(df)
