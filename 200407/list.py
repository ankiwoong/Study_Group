# Sequence Structure Container(시퀀스 구조 컨테이너)
# empty list
a = []
print(a)
print('-' * 30)

# numbers
b = [10, 20, 30, 40, 50]
print(b)
print('-' * 30)

# string
c = ['Elmore Kautzer', 'Ms. Kara Gleason', 'Caleigh Hoeger']
print(c)
print('-' * 30)

# mixed items
d = [10, 'Koby Kuphal', 2.5]
print(d)
print('-' * 30)

# type
print(type(a))
print('-' * 30)

# indexing
e = ['purple', 'ubiquitous', 'Tanzanian Shilling', 'primary']
print(e[0])
print('-' * 30)

# slicing
print(e[0:1])
print(e[2:])
print(e[:2])
print(e[-1:])
print(e[:-1])
print('-' * 30)

# change item
print(e)
e[1] = 'Toys'
print(e)
print('-' * 30)

# word delete
e.remove('Toys')
print(e)
print('-' * 30)

# index delete
del e[1]
print(e)
print('-' * 30)

# append item
e.append('Tajikistan')
print(e)
print('-' * 30)

# insert item
e.insert(1, 'Table')
print(e)
print('-' * 30)

# type change
f = 'View'
print(list(f))
print('-' * 30)

# specific word split
g = '1986.01.09'
print(g.split('.'))
print('-' * 30)

# blank word split
h = '1986 01 09'
print(h.split())
print('-' * 30)

# find offset by value
i = ['Arizona', 'Hat', 'Bridge', 'bus', 'array']
print(i.index('Hat'))
print('-' * 30)

# check items by value
print('bus' in i)
print('cat' in i)
print('-' * 30)

# count
print(i.count('bus'))
print(i.count('dog'))
print('-' * 30)
