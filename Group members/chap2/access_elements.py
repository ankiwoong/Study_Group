from bs4 import BeautifulSoup

html = "<html>" \
           "<head>" \
                "<title>Let's Python!</title>" \
           "</head>" \
           "<body>" \
               "<div>" \
                    "<p>Python Coding Program1</p>" \
                    "<p>Python Coding Program2</p>" \
                    "<p>Python Coding Program3</p>" \
               "</div>" \
           "</body>" \
       "</html>"
soup = BeautifulSoup(html, 'lxml')

print('### next element ###')
print(soup.p.next_element)

print('### next elements ###')
for el in soup.p.next_elements:
    print(el)
