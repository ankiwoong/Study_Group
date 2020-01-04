import requests

URL = 'http://quotes.toscrape.com/login'
OUTPUT_PATH = 'foo.txt'

res = requests.post(URL, {
    'username': 'kuckjwi',
    'password': 'kuckjwi',
})

with open(OUTPUT_PATH, 'w+') as f:
    f.write(res.content.decode('utf-8'))