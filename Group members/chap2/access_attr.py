from bs4 import BeautifulSoup

html = "<html><head><title>Let's Python!</title></head><body>" \
       "<p id='python' name='coding' class='program'>Python Coding Program</p></body></html>"
soup = BeautifulSoup(html, 'lxml')
p_tag = soup.p

# attribute
print('{} {} {}'.format(p_tag.get('id'), p_tag.get('name'), p_tag.get('class')).title())

# 클래스는 배열로 출력