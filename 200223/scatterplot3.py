from matplotlib import pyplot as plt

# 역의 관계 : x가 증가할 때 y는 감소
value1 = [10, 20, 30, 40, 50, 60, 70]
value2 = [80, 70, 65, 45, 40, 30, 20]

plt.scatter(value1, value2)

plt.show()

plt.close()
