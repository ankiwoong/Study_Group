my_list = [2, 3, 4, 5, 6, 7, 8]
new_list = list(map(lambda a: (a / 3 != 2), my_list))
print(new_list)
