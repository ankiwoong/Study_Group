from pandas import DataFrame
from matplotlib import pyplot
from Data import grade_dic

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# 한글폰트, 그래픽 크기 설정
pyplot.rcParams['font.family'] = 'NanumGothic'
pyplot.rcParams['font.size'] = 14
pyplot.rcParams['figure.figsize'] = (12, 8)

# 국어 점수에 대한 박스 보기
pyplot.figure()
df.boxplot('국어')

# 시각화
pyplot.show()

# 저장
pyplot.savefig('boxplot.png', dpi=300)

# 종료
pyplot.close()
