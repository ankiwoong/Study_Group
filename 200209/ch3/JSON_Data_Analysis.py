import requests
import json

url = 'https://api.androidhive.info/contacts'

response = requests.get(url)

if response.status_code != 200:
    print("[%d Error] %s" % (response.status_code, response.reason))
    quit()

response.encoding = 'UTF-8'

# print(response.text)

result = json.loads(response.text)
# print(result)

id = []
gender = []
mobile = []

for i in result['contacts']:
    id.append(i['id'])
    gender.append(i['gender'])
    mobile.append(i['phone']['mobile'])

# print(id)
# print(gender)
# print(mobile)

# for j in range(len(id)):
#     print('id : {0}'.format(id[j]))
#     print('Gender : {0}'.format(gender[j]))
#     print('phone mobile : {0}'.format(mobile[j]))
#     print('-' * 20)

for j in range(len(id)):
    if gender[j] == 'male':
        print('id : {0}'.format(id[j]))
        print('Gender : {0}'.format(gender[j]))
        print('phone mobile : {0}'.format(mobile[j]))
        print('-' * 20)
    else:
        pass
