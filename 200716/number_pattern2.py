def pascal(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print(function(i, j), " ", end="")
        print()


def function(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        res = res * (n - i)
        res = res // (i + 1)

    return res


pascal(7)
