import requests as req
import json

KAKAO_BOOK_URL = 'https://dapi.kakao.com/v3/search/book'
APP_KEY = '78f47a71bcce805400332bf76adb2ef5'

# oauth 2.0
headers = {
    'Authorization': 'KakaoAK {}'.format(APP_KEY),
}

params = {
    'query': '카카오',
    'sort': 'accuracy',
    'page': 1,
    'size': 10,
}

content = req.get(KAKAO_BOOK_URL, params,
                  headers=headers).content.decode('utf-8')
json_content = json.loads(content)

for jc in json_content.get('documents'):
    print(jc)
