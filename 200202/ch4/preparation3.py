from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])
df['프로그래밍'] = [92, 49, 21, 20, None]

# print_df(df)

# numpy 사용열 추가
# sum : 합계 / mean : 평균 / max : 최대값 / min : 최소값
# astype('int') -> mean의 값을 정수로
df['평균'] = df.mean(axis=1).astype('int')

# 다중 조건부 데이터 추가
# 학점 조건
gpa = [
    (df['평균'] >= 90),     # A
    (df['평균'] >= 80),     # B
    (df['평균'] >= 70),     # C
    (df['평균'] >= 59),     # D
    (df['평균'] < 58),      # F
]

# 학점
gpa_label = ['A', 'B', 'C', 'D', 'F']

# 학점 추가
df['학점'] = numpy.select(gpa, gpa_label)

print_df(df)
