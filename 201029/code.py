from bs4 import BeautifulSoup
from pprint import pprint
import requests

# 웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, "html.parser")
html.close()

# 요일별 웹툰영역 추출하기
data1_list = soup.findAll("div", {"class": "col_inner"})
pprint(data1_list)