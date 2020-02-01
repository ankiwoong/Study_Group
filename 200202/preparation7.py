from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 특정 열로 내림차순 정렬
df.sort_values('영어', inplace=True, ascending=False)

# 특정 열로 내림차순 후 출력
print_df(df)
