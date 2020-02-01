from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 두 개 이상의 열로 정렬
# 국어 점수가 동일할 경우 과학점수 순으로 정렬
df.sort_values(['국어', '과학'], inplace=True)

# 정렬 후 출력
print_df(df)
