from pandas import DataFrame
from Data import grade_dic
from print_df import print_df
from matplotlib import pyplot
from sklearn.impute import SimpleImputer
import numpy

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 상자 수염 그림 생성
pyplot.rcParams['font.family'] = 'NanumGothic'
pyplot.rcParams['font.size'] = 14
pyplot.rcParams['figure.figsize'] = (12, 8)

pyplot.figure()

df.boxplot()

pyplot.savefig('outlier.png', dpi=300)
pyplot.show()
pyplot.close()
