from Crawler import crawler
from pandas import DataFrame

url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

page_list = []

page_n = crawler.select(url, selector='.pager > li.current')

for h in page_n:
    page_list.append(h.text.strip().split())

# print(page_list)

title_list = []
price_list = []

for n in range(int(page_list[0][1]), int(page_list[0][-1]) + 1):
    url_s = 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-{}.html'.format(
        n)

    dom1 = crawler.select(url_s, selector='.product_pod > h3 > a')
    dom2 = crawler.select(url_s, selector='.product_price > p.price_color')

    for i in dom1:
        title_list.append(i.text)

    for j in dom2:
        price_list.append(j.text.lstrip('£'))

# print(title_list)
# print(price_list)

di = {
    'title': title_list,
    'price': price_list
}

df = DataFrame(di, columns=['title', 'price'])

df.to_csv('title_price.csv', encoding='utf-8', index=False)
