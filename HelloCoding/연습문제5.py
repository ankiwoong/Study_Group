count = 0
while count < 3:
    print(count)
    count = count + 1

count = 1
while count < 4:
    count = count + 1
    print(count)

count = 0
while count <= 5:
    if count % 2 != 0:
        print(count)
    count = count + 1

sum = 0
count = 1
while count <= 5:
    sum = sum + count
    count = count + 1
print("총합은", sum)

for i in range(3):
    print("안녕 거북이", i)

for j in range(0,3):
    print("안녕 거북이", j)

k = 0
while k <= 3:
    print("안녕 거북이", k)
    k = k + 1

l = 0
while True:
    print("안녕 거북이", l)
    l = l + 1
    if l == 3:
        break

count = 3
while count > 0:
    print(count)
    count = count - 1

clovers = ["클로버1", "클로버2", "클로버3"]
count = 0
while count < 3:
    print(clovers[count])
    count = count + 1

clovers = ["클로버1", "클로버2", "클로버3"]
count = 1
while count <3:
    print(clovers[count])
    count = count + 1

clovers = ["클로버1", "클로버2", "클로버3"]
for count in range(0, 2):
    print(clovers[count])

clovers = ["클로버1", "클로버2", "클로버3"]
for count in range(1, 3):
    print(clovers[count])

num = 1
while True:
    if num > 3:
        break
    print(num)
    num = num + 1

price = 0
while price != -1:
    price = int(input("가격을 입력하세요 (종료 : -1): "))
    if price > 10000:
        print("너무 비싸요")
    elif price > 5000:
        print("괜찮은 가격이네요")
    elif price > 0:
        print("정말 싸요")

while True:
    number = int(input("2 이상의 저수를 입력하세요. (종료 : -1): "))
    if number == -1:
        break
    count = 2
    is_prime = True
    while count < number:
        if number % count == 0:
            is_prime = False
            break
        count = count + 1
    if is_prime:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")