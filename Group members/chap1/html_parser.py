from bs4 import BeautifulSoup


def correct_syntax():
    html = "<p>Python Coding Program</p>"
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)


def incorrect_syntax():
    html = "<p>Python Coding Program<p"
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)


correct_syntax()
# incorrect_syntax()
