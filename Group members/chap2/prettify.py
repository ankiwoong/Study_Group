from bs4 import BeautifulSoup
html = "<html><body><p>Python Coding Program</p></body></html>"
soup = BeautifulSoup(html, 'lxml')

# prettify
print(soup.prettify())
