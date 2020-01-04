from bs4 import BeautifulSoup


def correct_syntax():
    html = "<p>Python Coding Program</p>"
    soup = BeautifulSoup(html, 'html5lib')
    print(soup)


def incorrect_syntax():
    html = "<p>Python Coding Program<p"
    soup = BeautifulSoup(html, 'html5lib')
    print(soup)


correct_syntax()
# incorrect_syntax()
