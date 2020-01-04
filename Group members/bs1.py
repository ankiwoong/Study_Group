import requests
from bs4 import BeautifulSoup
html = requests.get('https://kuckjwi0928.github.io/pythoncodingprogram/').content.decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
h_tags = reversed(soup.select(','.join(['#this-is-h{}'.format(i + 1) for i in range(0, 6)])))
print('\n'.join([h_tag.text for h_tag in h_tags]))