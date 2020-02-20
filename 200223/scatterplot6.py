from matplotlib import pyplot as plt

# Sample Data
age = [10, 20, 30, 40, 50, 60, 70]
retv = [14.2, 19.6, 8.5, 3.5, 1.4, 0.4, 0.2]

# 전역 설정
plt.rcParams["font.family"] = 'NanumGothic'
plt.rcParams["font.size"] = 12
plt.rcParams["figure.figsize"] = (10, 10)

# 그래프 시작
plt.figure()

plt.scatter(age, retv, color='#ff6600', marker='o', label='나이에 따른 티비 다시보기')

plt.legend()

plt.grid()

plt.title('title')

plt.ylabel('y')

plt.xlabel('x')

plt.show()

plt.close()
