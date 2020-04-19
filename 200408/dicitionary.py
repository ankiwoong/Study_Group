# Associative Array / Map / Hash Map
# {key : value}

# empty dictionary
a = {}
print(a)
print('-' * 30)

# dict
b = {'turquoise': 'IB', 'Chair': 'Ohio', 'Tasty Rubber Hat': 'purple'}
print(b)
print('-' * 30)

# empty dict item add
c = {}
c['Borders'] = 'multi-byte'
c['overriding'] = 'reboot'
c['AI'] = 'enhance'
print(c)
print('-' * 30)

# item update
b['turquoise'] = 'Sleek Rubber Chair'
print(b)
print(b['turquoise'])
print('-' * 30)

# item del
del b['turquoise']
print(b)
print('-' * 30)

# dict find
not_find = b.get('Chief')
print(not_find)
find = b.get('Chair')
print(find)
print('-' * 30)

# dict change
d = [['hack', 'Generic Steel Hat'], [
    '1080p', 'Money Market Account'], ['Small', 'wireless']]
print(dict(d))
print('-' * 30)

# Make sure the dictionary has a key
e = {'Rue': 'neutral', 'connecting': 'Hat', 'Michigan': 'override'}
print('Rue' in e)
print('killer' in e)
print('-' * 30)

# Get Key
print(e.keys())
print('-' * 30)

# Get Values
print(e.values())
print('-' * 30)

# Get Key - Values
print(e.items())
print('-' * 30)
