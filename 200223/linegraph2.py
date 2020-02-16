from matplotlib import pyplot as plt

# Sample Data
newborn = [470171, 471265, 484550, 436455,
           434435, 438420, 406243, 357771, 326822]
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

# 그래프 설정
plt.figure()

# y축 -> newborn
# x축 -> year
# linestyle -> '-' 직선 / '--' 끊긴 선 / '-.' 선과 점의 교차 표시 / ':' 점선 / 'steps' 직각 / 'none' 표시안함
# marker -> '+' 덧셈표시 / '.' 원 표시
# color -> HEX Color
plt.plot(newborn, label='baby count',
         linestyle='-.', marker='.', color='#a2ff00')

# 범주 표시
plt.legend()

# 그리드 표시
plt.grid()

# 그래프 제목
plt.title('Korea Newborn Baby of Year')

# X축 라벨
plt.xlabel('Year')

# Y축 라벨
plt.ylabel('Newborn')

# 좌표값 대신 라벨 표시
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8], year)

# 그래프 표시
plt.show()

# 그래프 종료
plt.close()
