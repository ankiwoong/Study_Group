from bs4 import BeautifulSoup
import requests
import re


def get_html():
    return requests.get('https://kuckjwi0928.github.io/pythoncodingprogram/').content.decode('utf-8')


def find_etc_by_name(_tr_tags, name):
    for tr_tag in _tr_tags:
        td_tags = tr_tag.find_all('td')
        if td_tags[0].text.find(name) != -1:
            return td_tags[1].text
    return ''


def get_info(_tr_tags):
    return list(map(lambda tr_tag: tr_tag.td.text, _tr_tags))


soup = BeautifulSoup(get_html(), 'html.parser')
tr_tags = soup.tbody.find_all('tr')

# 문제 1-1
print(''.join(re.findall(r'[A-Z]', find_etc_by_name(tr_tags, 'jeny'))))
# 문제 1-2
print(''.join(re.findall(r'[가-힣]|[\s]|[?]',
                         find_etc_by_name(tr_tags, 'master'))).strip())
# 문제 2
user_dic = {}
for info in get_info(tr_tags):
    name = re.search(r'[a-z]+', info).group()
    phone_number = re.search(r'\d{3}-\d{4}-\d{4}', info).group()
    user_dic[name] = phone_number
print(user_dic)
