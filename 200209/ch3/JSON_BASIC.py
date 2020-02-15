import requests
import pprint
res = requests.get('http://api.github.com/users/ankiwoong')

# print(type(res))

text = res.text
# print(text)

# pprint.pprint(res.text)

# pprint.pprint(res.json())
