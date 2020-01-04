from Crawler import crawler, Conversation
import requests
from bs4 import BeautifulSoup
import re
import time

url = 'https://basicenglishspeaking.com/daily-english-conversation-topics/'

keyword_list = []
keyword_list2 = []

keyword = crawler.select(
    url, selector='#tve_editor > div.thrv_wrapper.thrv-columns > div > div > div > div > p > a')

for i in keyword:
    keyword_list.append(i.text.replace(' ', '-'))

for j in keyword_list:
    text = re.sub('[/]', '', j)
    keyword_list2.append(text)

print('총 {} 개의 주제를 찾았습니다.'.format(len(keyword_list2)))

i = 1

for b in keyword_list2:
    print('({} / {})주제: {}'.format(i, len(keyword_list2), b))
    i += 1

conversations = []

for u in keyword_list2:
    req = requests.get('https://basicenglishspeaking.com/' + u)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    qnas = soup.findAll('div', {'class': 'sc_player_container1'})

    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling

        else:
            a = qna.next_sibling
            c = Conversation(q, a)
            conversations.append(c)

    time.sleep(3)

for c in conversations:
    print(str(c))
