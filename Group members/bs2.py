from bs4 import BeautifulSoup
import requests as rq

res=rq.get('https://kuckjwi0928.github.io/pythoncodingprogram/')
soup=BeautifulSoup(res.content,'html.parser')

for i in range(6,0,-1):
    print(soup.find(id="this-is-h%s" % i).text)