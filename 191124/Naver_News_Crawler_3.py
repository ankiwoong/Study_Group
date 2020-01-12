import requests
from bs4 import BeautifulSoup as BS

def list2dict(keywords):
    keys = {}
    for keyword in keywords:
        keys[keyword]=0
    return keys

date = input("언제[YYYYmmdd] 기사를 검색할까요? : ")
pages = int(input("총 몇 페이지를[20/page]를 검색할까요? : "))
keywords = input("관심있는 단어를 띄어쓰기로 입력하세요 : ").split()
keys = list2dict(keywords)

number = 1

news= []

for page in range(1, pages + 1):
    url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&date={}&page={}".format(date, page)
    response = requests.get(url)
    text = response.text
    html = BS(text, "html.parser")
    li_list = html.find("td", {"class":"content"}).find_all("li")

    for li in li_list:
        title = li.find("dt","").find("a").text.strip("\n\t\r ") # 뉴스 제목 추출하기
        try:
            img_url = li.find("img")["src"].split("?")[0]
        except:
            img_url = "없음"
        body = li.find("span", {"class":"lede"}).text # 뉴스 내용 요약 추출하기
        writer =  li.find("span", {"class":"writing"}).text # 뉴스 제공자

        for key in keys.keys():
            if key in title:
                keys[key] += 1
                print("기사 제목 : {:03}_{}".format(number, title))
                print("기사 내용 : {}".format(body))
                print("기사 사진 : {}".format(img_url))
                print("기사 제공 : {}".format(writer))
                print("")
                print("-------------------------------------------------------------------")
        number += 1