for num in [3, 1, 2]:
    print(num)

for num in range(2):
    print(num)

clovers = ["클로버1", "클로버2", "클로버3"]
for clover in clovers:
    print(clover)

for i in range(3):
    print(clovers[i])

for num in range(1, 4):
    print("*" * num)

stars = [2, 1, 3]
for num in stars:
    print("*" * num)

total = 0
for num in [0, 1, 2, 3]:
    total = total + num
print(total)

total = 0
for num in range(4):
    total = total + num
print(total)

total = 0
for num in range(0, 5):
    total = total + num
print(total)

total = 0
for num in range(1, 4):
    total = total + num
print(total)

total = 0
card_nums = [1, 3, 6, 7]
for num in card_nums:
    total = total + num
print(total / len(card_nums))

clovers = ["클로버1", "클로버2", "클로버3"]
for i in [2, 1, 0]:
    print(clovers[i])

nums = [0, 1, 2, 3, 4, 5]
for num in nums[1:3]:
    print(num)