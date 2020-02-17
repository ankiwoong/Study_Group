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
plt.rcParams["font.family"] = 'NanumGothic'         # 한글 폰트
plt.rcParams["font.size"] = 12                      # 폰트 사이즈
plt.rcParams["figure.figsize"] = (12, 8)           # 그래프 사이즈

# 그래프 설정
plt.figure()

# 좌표 배열 생성(0 ~ 8)
x = np.arange(len(label))
# print(x)

# x축 좌표와 굵기를 설정
plt.bar(x-0.2, car_vs_people, label='차 대 사람', width=0.4, color='#ff6600')
plt.bar(x+0.2, car_vs_car, label='차 대 차', width=0.4, color='#0066ff')

# x축 라벨 별도 지정
plt.xticks(x, label)

# 범주 표시
plt.legend()

# x축 라벨
plt.xlabel('년도')

# y축 라벨
plt.ylabel('교통사고 수')

# y축 범위
plt.ylim(0, 34000)

# 그래프 제목
plt.title('2005년 ~ 2017년 유형별 교통 사고 현황')

# 그래프 보이기
plt.show()

# 그래포 종료
plt.close()
