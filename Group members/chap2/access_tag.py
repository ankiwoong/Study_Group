from bs4 import BeautifulSoup

html = "<html><head><title>Let's Python!</title></head><body><p>Python Coding Program</p><p>Study</p></body></html>"
soup = BeautifulSoup(html, 'lxml')

# title
print(soup.title)
