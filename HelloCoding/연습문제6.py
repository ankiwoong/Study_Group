nums = (1, 2, 3)
print(nums)

my_tuple = (3.14, 2.71)
print(my_tuple)
print(my_tuple[1])

my_var = 1,
print(type(my_var))

my_var = (1,)
print(type(my_var))

my_var = (1)
print(type(my_var))

my_var = 1, 2
print(type(my_var))

nums = 1, 2, 3
for i in range(3):
    print(nums[i])

diamonds = 1, 5, 6, 7
ace, king, quen, jack = diamonds
print(quen)

alice = {}
alice["성별"] = "여"
alice["나이"] = 13
alice["혈액형"] = "AB"
print(alice)

alice["나이"] = 14
print(alice)

alice["전화번호"] = "010-1234-5678"
print(alice)

del alice["전화번호"]
print(alice)