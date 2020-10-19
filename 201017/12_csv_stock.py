import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok="

for page in range(1, 2):
    res = requests.get(url + str(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    data_rows = (
        soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    )
    # print(data_rows)

    for row in data_rows:
        columns = row.find_all("td")

        if len(columns) <= 1:  # 의미 없는 데이터는 skip
            continue

        data = [column.get_text().strip() for column in columns]
        print(data)
