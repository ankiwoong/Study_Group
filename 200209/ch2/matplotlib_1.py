from matplotlib import pyplot as plt

# sample data
# Median Developer Salaries by Age
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# 선형 그래프(x 축 data, y 축 data)
plt.plot(ages_x, dev_y, label='All Devs')

# sample datas
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

# 선형 그래프(x 축 data, y 축 data)
plt.plot(ages_x, py_dev_y, label='Python')

# x축 label
plt.xlabel('Ages')

# y축 label
plt.ylabel('Median Salaries(USD)')

# pyplot 제목
plt.title('Median Salary (USD) by Age')

# pyplot 참조
#plt.legend(['All Devs', 'Python'])
plt.legend()


# pyplot 보이기
plt.show()
