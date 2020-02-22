import numpy as np
from matplotlib import pyplot as plt

# Sample Data
car_vs_people = [9110, 8849, 9370, 10604, 10986, 10783,
                 10869, 10892, 10683, 11118, 11318, 10683, 10249]
car_vs_car = [28649, 28555, 29136, 30261, 31922, 29579,
              28294, 28537, 27358, 28201, 28854, 28030, 27103]
car_only = [769, 830, 853, 1141, 1350, 1300,
            1288, 1399, 1398, 1473, 1493, 1326, 1273]
label = ['2005년', '2006년', '2007년', '2008년', '2009년', '2010년',
         '2011년', '2012년', '2013년', '2014년', '2015년', '2016년', '2017년']

# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (12, 8)

# 데이터 계산
value1 = np.array(car_vs_people)
value2 = np.array(car_vs_car)
value3 = np.array(car_only)

# 데이터 범위
ratio = [value1.sum(), value2.sum(), value3.sum()]

# 라벨
labels = ['차 대 사람', '차 대 차', '차량단독']
# 색상
colors = ['#ff6600', '#ff00ff', '#00ffff']
# 확대 비율
explode = [0.0, 0.0, 0.0]

# 파이그래프 표현
plt.pie(ratio, labels=labels, colors=colors, explode=explode,
        autopct='%0.2f%%', shadow=False, startangle=90)

# 그래프 제목
plt.title('2005년 ~ 2017년 유형별 교통 사고 현황')
# 범주 표시
plt.legend()
# 그래프 보이기
plt.show()
# 그래프 종료
plt.close()
