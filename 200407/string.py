# string -> '', ""
a = 'hello world'
b = "hello world"

print(a)
print(b)
print('-' * 30)

# string concatenation
first_name = 'Karli'
middle_name = 'Gennaro'
surname = 'Baumbach'

print(first_name + ' ' + middle_name + ' ' + surname)
print('-' * 30)

# string multiplication
c = 'hello' * 3
print(c)
print('-' * 30)

# escape character
# 1. Newline
d = 'hello\n' + 'world'
print(d)
# 2. Tab
e = '\thello world'
print(e)
# 3. carriage return
f = '\rhello world'
print(f)
# 4. null
g = '\0hello world'
print(g)
# 5. \
h = 'hello\\world'
print(h)
# 6. '
i = 'hi i\'am world'
print(i)
# 7. "
j = "\"hello world\""
print(j)
print('-' * 30)

# type convert
k = str(10.2)
print(k)
print(type(k))
print('-' * 30)

# indexing
l = 'hello world'
print(l[0])
print('-' * 30)

# slicing
print(l[0:5])
print(l[-5:])
print(l[1:-1])
print(l[:-5])
print('-' * 30)

# len
print(len(l))
print('-' * 30)
