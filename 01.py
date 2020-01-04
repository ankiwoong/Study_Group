y, m, d = map(int,input().split())

n = y + m + d

list = []

for i in str(n):
    list.append(i)

if len(list) == 4:
    if int(list[1]) % 2 == 0:
        print('대박')
    else:
        print('그럭저럭')
elif len(list) == 3:
    if int(list[0]) % 2 == 0:
        print('대박')
    else:
        print('그럭저럭')
elif len(list) == 2:
    if int(list[0]) % 2 == 0:
        print('대박')
    else:
        print('그럭저럭')