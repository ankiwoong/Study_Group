from matplotlib import pyplot as plt

# Sample Data
newborn = [470171, 471265, 484550, 436455,
           434435, 438420, 406243, 357771, 326822]
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'         # 한글 폰트
plt.rcParams["font.size"] = 12                      # 폰트 사이즈
plt.rcParams["figure.figsize"] = (12, 8)           # 그래프 사이즈

# 그래프 설정
plt.figure()

# 세로 막대 그래프
# barh() 함수의 기준측은 y방향

# 막대 그래프 표현
plt.barh(year, newborn, label='신생아 수')

# 범주 표현
plt.legend()

# 기준 축(y 축)
plt.ylabel('년도')

# 데이터 축(x 축)
plt.xlabel('신생아 수')

# 데이터 범위
plt.xlim(300000, 490000)

# 그래프 제목
plt.title('년도별 신생아 수')

# 그리드 표시
plt.grid()

# 막대 그래프 수치 값 표시
# 그래프 데이터 수 만큼 반복하여 텍스트 표시
for i, v in enumerate(year):
    # 텍스트
    str_value = '%d명' % newborn[i]

    # x 축 좌표, y 축 좌표, 표시문구, 글자크기, 색상, 가로 / 세로 정렬
    # 가로 설정 :
    # 세로 설정 :
    plt.text(newborn[i], v, str_value, fontsize=10, color='#ff6600',
             horizontalalignment='left', verticalalignment='center')

# 그래프 보이기
plt.show()

# 그래프 종료
plt.close()
