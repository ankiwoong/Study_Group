import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.title)
# print(soup.title.get_text())

# print(soup.a)  # spup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs)  # a element 의 속성 정보를 출력
# print(soup.a["href"])  # a element 의 속성 '값' 정보를 출력

# print(
#     soup.find("a", attrs={"class": "Nbtn_upload"})
# )  # class='Nbtn_upload' 인 a element를 찾아줘
# print(
#     soup.find(attrs={"class": "Nbtn_upload"})
# )  # class='Nbtn_upload' 인 어떤 element를 찾아줘

# print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a)