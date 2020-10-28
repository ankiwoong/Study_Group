from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?query=날씨")
# pprint(html.text)

soup = bs(html.text, "html.parser")
# pprint(soup)

data1 = soup.find("div", {"class": "detail_box"})
# pprint(data1)

data2 = data1.findAll("dd")
# pprint(data2)

fine_dust = data2[0].find("span", {"class": "num"}).text
print(fine_dust)