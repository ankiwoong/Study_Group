def func(n):
    def func1():
        return "edureka"

    def func2():
        return "python"

    if n == 1:
        return func1
    else:
        return func2


a = func(1)
b = func(2)
print(a())
print(b())
