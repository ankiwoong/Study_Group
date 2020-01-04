from bs4 import BeautifulSoup

html = "<html>" \
           "<head>" \
                "<title>Let's Python!</title>" \
                "<link ref='./style.css' />" \
           "</head>" \
           "<body>" \
               "<div>" \
                   "<p id='python'>Python Coding Program1</p>" \
                   "<p class='coding'>Python Coding Program2</p>" \
                   "<p class='coding'>Python Coding Program3</p>" \
               "</div>" \
               "<div>" \
                   "<p id='python2'>파이썬</p>" \
                   "<p class='coding'>쉽지만</p>" \
                   "<p class='coding'>은근 어렵습니다.</p>" \
               "</div>" \
               "<script type='text/javascript' src='./main.js' />" \
               "<script type='text/javascript' src='./common.js' />" \
       "</body>" \
       "</html>"
soup = BeautifulSoup(html, 'lxml')

# find_all()
# print(soup.find_all('p'))
# print(soup.find_all('p', class_='coding'))
# print(soup.find_all('p', limit=2))

# find()
# print(soup.find('p', id='python'))
# print(soup.find('p', id='python2'))
# print(soup.find('div').find_all('p', class_='coding'))

# select()
# css selector id = #, class = .
# print(soup.select('div'))
# print(soup.select('div p'))
# print(soup.select('div .coding'))
# print(soup.select('div #python'))

# extract()
# print(soup)
# soup.head.extract()
# for script_tag in soup.find_all('script'):
#     script_tag.extract()
# print(soup)
