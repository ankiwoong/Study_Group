from matplotlib import pyplot as plt

# f(x) = x
# 데이터는 리스트 or 배열 등 연속성 데이터 형식
data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 그래프 설정
plt.figure()

# 그래프 데이터 표시
# y축 => 리스트의 각 원소
# x축 => 리스트의 index
plt.plot(data)

# 그래프 표시
plt.show()

# 그래프 종료
plt.close()
