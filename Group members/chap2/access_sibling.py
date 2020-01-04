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

p_tag_2 = soup.p.next_sibling

print('### previous ###')
print(p_tag_2.previous_sibling)
print('### next ###')
print(p_tag_2.next_sibling)
