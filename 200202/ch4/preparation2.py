from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])
df['프로그래밍'] = [92, 49, 21, 20, None]

# print_df(df)

# numpy 사용열 추가
# sum : 합계 / mean : 평균 / max : 최대값 / min : 최소값
df['평균'] = df.mean(axis=1)

# 단일 조건부 데이터 추가
df['평가'] = numpy.where(df['평균'] >= 65, 'Pass', 'Fail')

print_df(df)
