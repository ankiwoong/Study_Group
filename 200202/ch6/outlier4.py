from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
from matplotlib import pyplot
from sklearn.impute import SimpleImputer
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 국어점수 이상치 필터링
filtering_outlier = df.query('국어 > 100')

# 필터링 된 이상치 인덱스 추출
filtering_outlier_index = list(filtering_outlier.index)

# 결측치로 변경
for i in filtering_outlier_index:
    df.loc[i, '국어'] = numpy.nan

print_df(df)
