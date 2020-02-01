from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 열 순서 변경
df_columns = df.reindex(columns=['국어', '수학', '영어', '과학'])

# 열 순서 변경 후 출력
print_df(df_columns)
