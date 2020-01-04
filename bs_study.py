from bs4 import BeautifulSoup
import requests

req = requests.get('https://kuckjwi0928.github.io/pythoncodingprogram/')

html = req.text
# print(html)

soup = BeautifulSoup(html, 'html.parser')
# print(soup)

soup_select = soup.select('div.highlight > pre.highlight > code')

for i in soup_select:
    print(i.text)