from matplotlib import pyplot as plt

# 정의관계 : x가 증가 할때 y도 증가
value1 = [10, 20, 30, 40, 50, 60, 70]
value2 = [20, 40, 60, 65, 70, 75, 80]

plt.scatter(value1, value2)

plt.show()

plt.close()
