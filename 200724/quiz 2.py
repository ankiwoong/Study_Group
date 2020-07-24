stars = ["안기웅", "김유림", "안지아", "원빈", "송혜교", "김진"]
print(stars)
print('-' * 30)

stars.append("한예슬")
print(stars)
print('-' * 30)

stars.pop(4)
print(stars)
print('-' * 30)

del stars[3]
print(stars)
print('-' * 30)

stars.sort()
print(stars)
print('-' * 30)

stars.sort(reverse=True)
print(stars)
print('-' * 30)

print(stars[2])
print(stars[4])
print('-' * 30)

stars[2] = stars[4]
print(stars)
stars[4] = stars[2]
print(stars)
print('-' * 30)

stars = set(stars)
new_starts = list(stars)
print(new_starts)
