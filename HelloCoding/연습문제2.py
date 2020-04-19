nums = [1, 2, 3]
print(nums)

fruits = []
print(fruits)
fruits.append("자몽")
print(fruits)
fruits.append("멜론")
print(fruits)
fruits.append("레몬")
print(fruits)

print(fruits[1])

del fruits[0]
print(fruits)

nums = [1, 3]
nums[1] = 2
nums.append(3)
nums.append(4)
print(nums)

nums.append(5)
print(nums[2])
print(nums[-3])

print(nums[0:3])
print(nums[2:5])

nums = [1, 1, 1, 2, 2, 3]
print(nums.count(1))

fruits = ["멜론", "거봉", "레몬"]
print(fruits)
fruits.sort()
print(fruits)