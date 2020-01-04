import requests
from bs4 import BeautifulSoup as bs

LOGIN_INFO = {
    'username': 'seunghwan',
    'password': '1234'
}

with requests.Session() as s:
    first_page = s.get('http://quotes.toscrape.com/login')
    html = first_page.text
    soup = bs(html, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf_token'})

    LOGIN_INFO = {**LOGIN_INFO, **{'csrf_token': csrf['value']}}

    login_req = s.post('http://quotes.toscrape.com/login', data=LOGIN_INFO)

    post = s.get('http://quotes.toscrape.com/')
    html = post.text
    soup = bs(html, 'html.parser')
    text = soup.select('body > div > div.row.header-box > div.col-md-4 > p > a')

    print(text[0].text)