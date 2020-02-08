from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 다중 조건 행 조회
# or 조건
all_index = df.query('국어 < 50 or 영어 < 40')

# 출력
print_df(all_index)
