# basic while
n = 0

while n < 5:
    print(n)
    # n += 1 = n = n + 1
    n = n + 1
print('-' * 30)

# odd number
n1 = 0

while n1 <= 10:
    if n1 % 2 == 1:
        print(n1)
    n1 += 1
print('-' * 30)

# even
n2 = 0

while n2 <= 10:
    if n2 % 2 == 0:
        print(n2)
    n2 += 1
print('-' * 30)


# break
n3 = 0

while n3 <= 10:
    print(n3)
    if n3 == 8:
        break
    n3 += 1
print('-' * 30)

# continue
n4 = 0

while n4 <= 10:
    n4 += 1
    if n4 == 8:
        continue
    print(n4)
