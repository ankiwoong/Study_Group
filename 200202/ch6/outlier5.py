from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
from matplotlib import pyplot
from sklearn.impute import SimpleImputer
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 점수 이상치 필터링
filtering_outlier = df.query('국어 > 100')
filtering_outlier2 = df.query('과학 > 100')


# 필터링 된 이상치 인덱스 추출
filtering_outlier_index = list(filtering_outlier.index)
filtering_outlier_index2 = list(filtering_outlier2.index)


# 결측치로 변경
for i in filtering_outlier_index:
    df.loc[i, '국어'] = numpy.nan

for j in filtering_outlier_index2:
    df.loc[j, '과학'] = numpy.nan

print_df(df)
