from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

# 데이터 프레임
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 열, 행 이름 변경
df_c_i = df.rename(
    columns={
        '국어': 'kor', '영어': 'eng', '수학': 'math', '과학': 'sin'
    },
    index={
        '노진구': 'no', '이슬이': 'is', '비실이': 'bs', '퉁퉁이': 'tt', '도라에몽': 'dr'
    }
)

# 열, 행 이름 변경 후 출력
print_df(df_c_i)
