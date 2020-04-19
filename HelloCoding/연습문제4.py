num1 = 55
num2 = 13
print(num1 <= num2)
print(num1 != num2)

MVP = "하트잭"
print(MVP == "공작부인")

switch = "켜짐"
if switch == "켜짐":
    print("조명이 켜졌어요.")
else:
    print("조명이 꺼졌어요.")

price = 10000
if price > 10000:
    print("너무 비싸요.")
elif price > 5000:
    print("괜찮은 가격이네요.")
else:
    print("정말 싸요.")

print(2 > 5)
print(2 != 5)
print(False)
print(2 == 5)

input_number = -9
if input_number < 0:
    absolute_value = input_number * -1
else:
    absolute_value = input_number
print(absolute_value)

total_price = 0
choices = ["버섯스프", "당근주스", "벌꿀파이"]
for choice in choices:
    if choice == "버섯스프":
        total_price = total_price + 8000
    elif choice == "당근주스":
        total_price = total_price + 4500
    elif choice == "벌꿀파이":
        total_price = total_price + 6000
print("총 주문금액은", total_price, "입니다.")

odd_nums = []
for num in range(10):
    if num % 2 != 0:
        odd_nums.append(num)
print(odd_nums)

clovers = ["클로버1", "클로버2", "클로버3"]
print(clovers)
for clover in clovers:
    if clover == "클로버1":
        print(clover, "안녕!")
    elif clover == "클로버2":
        print(clover, "안녕!")
    elif clover == "클로버3":
        print(clover, "안녕!")
    else:
        print("넌 누구니?")

year = int(input("입력"))
if year % 400 == 0:
    print(year, "년은 윤년입니다.")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 안닙니다.")