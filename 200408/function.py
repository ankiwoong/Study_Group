# define
def sum(x, y):
    sum = x + y
    print(sum)
    return sum


# call
sum(5, 10)
print('-' * 30)


# main() 사용
def average(numbers):
    s = 0
    for n in numbers:
        s += n

    avg = s / len(numbers)
    return avg


def main():
    v = [10, 20, 30, 40]
    r = average(v)
    print(r)


main()


# basic parameter designation
def sum2(x=10, y=20):
    sum2 = x + y
    print(sum2)
    return sum2


sum2()
