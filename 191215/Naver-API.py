from requests import Request
from requests import Session

f = open('yesterday.txt', 'r')
text = f.read()
f.close()

s = Session()

headers = {
    'X-Naver-Client-Id': '6vQEeenWzIJitTqQVSA1',
    'X-Naver-Client-Secret': 'yATlft1qqI',
}

payload = {
    'source': 'en',
    'target': 'ko',
    'text': text,
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

# print(res.json())

result = res.json()['message']['result']['translatedText']

print(result)
