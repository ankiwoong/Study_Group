from matplotlib import pyplot as plt

# 기준 축 데이터
basic = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 데이터 축
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 세로 막대 그래프 생성
plt.bar(basic, data)

# 그래프 보이기
plt.show()

# 그래프 종료
plt.close()
