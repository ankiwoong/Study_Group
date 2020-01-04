import requests as req
import json

url = 'https://openapi.naver.com/v1/search/doc.json'

"""
요청 변수명	타입	필수 여부	기본값	설명
query	string	Y	-	검색을 원하는 문자열로서 UTF-8로 인코딩한다.
display	integer	N	10(기본값), 100(최대)	검색 결과 출력 건수 지정
start	integer	N	1(기본값), 1000(최대)	검색 시작 위치로 최대 1000까지 가능
sort	string	N	sim(기본값), date, asc, dsc	정렬 옵션: sim (유사도순), date (날짜순), asc(가격오름차순) ,dsc(가격내림차순)
"""

headers = {
    'X-Naver-Client-Id': '6vQEeenWzIJitTqQVSA1',
    'X-Naver-Client-Secret': 'yATlft1qqI',
}

params = {
    'query': '파이썬',
    'display': 10,
    'start': 1,
}

content = req.get(url, params, headers=headers).content.decode('utf-8')

json_content = json.loads(content)

for jc in json_content.get('items'):
    print(jc.get('title'))
