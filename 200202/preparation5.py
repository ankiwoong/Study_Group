from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 원본 수정
# inplace=True -> 원본 값 수정
df.rename(
    columns={
        '국어': 'kor', '영어': 'eng', '수학': 'math', '과학': 'sin'
    }, inplace=True
)

# 원본 수정 후 출력
print_df(df)
