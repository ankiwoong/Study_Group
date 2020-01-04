from bs4 import BeautifulSoup

html = "<html>" \
       "<head>" \
            "<title>Let's Python!</title>" \
       "</head>" \
       "<body>" \
            "<div id='parent1'>" \
                "<div id='parent2'>" \
                   "<p>Python Coding Program</p>" \
                "</div>" \
            "</div>" \
       "</body>" \
       "</html>"
soup = BeautifulSoup(html, 'lxml')

print('### parent ###')
print(soup.p.parent)

print('### parents ###')
for parent in soup.p.parents:
    print(parent)
