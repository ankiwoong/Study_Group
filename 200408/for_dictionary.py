a = {'Rue': 'neutral', 'connecting': 'Hat', 'Michigan': 'override'}
# for key
for i in a.keys():
    print(i)
print('-' * 30)

# for values
for i in a.values():
    print(i)
print('-' * 30)

# for item
for i in a.items():
    print(i)
print('-' * 30)

# for enumeerate index number
for i, v in enumerate(a.values()):
    print(i, v)
