import requests
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = BeautifulSoup(html, "html.parser")
#print( bs_obj )
# ul 중에 class 이름이 an_l 인 애들만 찾겟다.
ul = bs_obj.find("ul", {"id": "PM_ID_serviceNavi"})

#  하위 리스트 를 넣는다.
lists = ul.findAll("li")


for li in lists:

    # a 태그를 찾는다.
    a_tag = li.find("a")

    # a 태그에서 class 가 an_txt인 span 태그를 찾는다.
    span = a_tag.find("span", {"class": "an_txt"})
    print(span.text, end=" ")
    print(a_tag.get('href'))
