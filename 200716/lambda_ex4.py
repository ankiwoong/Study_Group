def new_func(x):
    return lambda y: x + y


t = new_func(3)
u = new_func(2)

print(t(3))
print(u(3))
