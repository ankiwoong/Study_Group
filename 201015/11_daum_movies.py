import requests
from bs4 import BeautifulSoup

res = requests.get(
    "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=2019%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup)

images = soup.find_all("img", attrs={"class": "thumb_img"})

for image in images:
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url
    print(image_url)