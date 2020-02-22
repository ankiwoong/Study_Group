'''
Quiz 1> 년도별 출생률에 대한 빈도와 시계율 변화를 한눈에 확인 하는 그래프 작성
막대그래프 + 선 그래프
'''
from matplotlib import pyplot as plt

# Sample Data
newborn = [470171, 471265, 484550, 436455,
           434435, 438420, 406243, 357771, 326822]
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

# 전역 설정
plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (12, 8)

# 그래프 시작
plt.figure()
# 선 그래프
plt.plot(year, newborn, linestyle='--', marker='.', color='#ff6600')
# 막대 그래프
plt.bar(year, newborn, label='신생아 수', color='#f6e640')
# 범주 표시
plt.legend()
# x 라벨
plt.xlabel('년도')
# y 라벨
plt.ylabel('신생아 수')
# 데이터 범위
plt.ylim(300000, 490000)
# 그래프 제목
plt.title('년도별 신생아 수')
# 그래프 격자
plt.grid()

# 막대 그래프 수치 값 표시
# 그래프 데이터 수 만큼 반복하여 텍스트 표시
for i, v in enumerate(year):
    str_val = "%d명" % newborn[i]

    plt.text(v, newborn[i], str_val, fontsize=9, color='#000000',
             horizontalalignment='center', verticalalignment='bottom')

# 그래프 보이기
plt.show()
# 그래프 종료
plt.close()
