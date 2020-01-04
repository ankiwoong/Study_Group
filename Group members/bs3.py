homework = []
for i in range(1,7):
    a='h%d'%i
    d = soup.select(a)
    if len(d) >= 2:
        hid = d[1]
        print(hid.contents)
        homework.append(hid.contents)
    else:
        hid = d[0]
        print(hid.contents)
        homework.append(hid.contents)
print(homework)
a2 = homework
print(a2)

a2.reverse()
print(a2)
for i in range(0,6):
    print(a2[i][0])