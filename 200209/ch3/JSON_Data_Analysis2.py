import requests
import json
from pandas import DataFrame
from print_df import print_df

url = 'https://api.androidhive.info/contacts'

response = requests.get(url)

if response.status_code != 200:
    print("[%d Error] %s" % (response.status_code, response.reason))
    quit()

response.encoding = 'UTF-8'

result = json.loads(response.text)

# 데이터 프레임으로 변환 작업
df = DataFrame(result['contacts'])

print_df(df)

name = []

# name을 인덱스 대신 사용하기 위해 리스트 형식으로 추출
for i in result['contacts']:
    name.append(i['name'])

# name 딕셔너리 생성
name_dict = {}
for i, v in enumerate(name):
    name_dict[i] = v

# Data Frame의 인덱스 변경 및 name 컬럼 삭제
df.rename(index=name_dict, inplace=True)
df.drop('name', axis=1, inplace=True)

print_df(df)
