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

children = soup.div.children
contents = soup.div.contents

print('children type is {}'.format(type(children)))
print('contents type is {}'.format(type(contents)))

print('### children ###')
for c in children:
    print(c)

print('### contents ###')
for i in range(0, len(contents)):
    print(contents[i])
