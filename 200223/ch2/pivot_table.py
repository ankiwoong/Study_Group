from print_df import print_df
from pandas import DataFrame
from matplotlib import pyplot as plt
import numpy as np
from sample_data import kosis_data

# 데이터 프레임 생성
df = DataFrame(kosis_data)
# print_df(df)

# 각 도시별 연도에 따른 인구수
# 행이나 열에 값들 중 중복이 존재 할 경우 에러 발생
pivot_table_1 = df.pivot('도시', '연도', '인구')
# print_df(pivot_table_1)

# 그룹 분석
# 행정구역별 인구수
administrative_area = df.groupby(df['행정구역']).sum()
# print_df(administrative_area)

# 연도별 인구수
year = df.groupby(df['연도']).sum()
# print_df(year)

# 도시별 인구수
city = df.groupby(df['도시']).sum()
# print_df(city)

# 행정구역 / 연도 평균 인구수
a_a_y = df.groupby([df['행정구역'], df['연도']]).mean()
# print_df(a_a_y)
