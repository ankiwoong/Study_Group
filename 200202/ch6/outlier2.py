from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
from matplotlib import pyplot
from sklearn.impute import SimpleImputer
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 국어점수 이상치 필터링
filtering_outlier = df.query('국어 > 100')

print_df(filtering_outlier)
