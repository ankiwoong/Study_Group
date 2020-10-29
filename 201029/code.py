from bs4 import BeautifulSoup
from pprint import pprint
import requests

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

# 모든 웹툰 제목 영역 추출
data1 = soup.findAll("a", {"class": "title"})
week_title_list = [t.text for t in data1]
pprint(week_title_list)