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
plt.rcParams["figure.figsize"] = (13, 13)

# 그래프 설정
plt.figure()

# 그래드 설정
plt.grid()

# 그래프 제목
plt.title('2005년 ~ 2017년 유형별 교통 사고 현황')

# X축 라벨
plt.xlabel('년도')

# Y축 라벨
plt.ylabel('교통사고율')

# 라벨 설정
plt.plot(car_vs_people, label='차대사람', linestyle='--', marker='.')
plt.plot(car_vs_car, label='차대차', linestyle='--', marker='.')
plt.plot(car_only, label='차량단독', linestyle='--', marker='.')

# x축 범위 설정
plt.xlim(0, 12)

# y축 범위 설정
plt.ylim(0, 33000)

# 범주 표시 설정
plt.legend(title='유형별', loc='center left', shadow=True)

# x축 라벨 설정(0부터 1씩 증가하는 label 리스트 만큼 크기 리스트)
# x의 n번째 좌표에 label의 n번째 값을 설정
x_label = list(range(0, len(label)))

# x label 리스트의 각 좌표에 지정될 라벨 설정
plt.xticks(x_label, label)

# 그래프 표시
plt.show()

# 그래프 종료
plt.close()
