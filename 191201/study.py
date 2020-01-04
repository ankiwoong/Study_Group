from Crawler import crawler
from pandas import DataFrame

total_url = 'http://books.toscrape.com/'
categories = crawler.select(
    total_url, selector='#default > div > div > div > aside > div.side_categories > ul > li > ul > li > a')

categorie_list = []

for categorie in categories:
    categorie_list.append(categorie.text.strip().replace(' ', '-').lower())

# print('Total Categorie {}'.format(len(categorie_list)))

# for categorie_print in categorie_list:
#     print('categorie : {}'.format(categorie_print))

n = 1

main_url_list = []
full_url_list = []

for url_catgorie in categorie_list:
    main_url = 'http://books.toscrape.com/catalogue/category/books/{}_{}'.format(
        url_catgorie, (n + 1))

    full_url = main_url + '/index.html'

    n += 1

    main_url_list.append(main_url)
    full_url_list.append(full_url)

    # print('Serach_url : {}'.format(full_url))

# for main_url_print in main_url_list:
#     print('Main_url : {}'.format(main_url_print))

page_number_list = []
i_list = []

for url_page_n in main_url_list:
    url_t = url_page_n + '/index.html'
    page_ns = crawler.select(url_t, selector='.pager > li.current')

    for page_n in page_ns:
        page_number_list.append(page_n.text.strip().split())
        i_list.append(url_page_n)

title_list = []
price_list = []

for i in page_number_list:
    for j in i_list:
        for u in range(int(i[1]), int(i[-1]) + 1):
            end_url = '/page-{}.html'.format(u)
            url_s = j + end_url

            dom1 = crawler.select(url_s, selector='.product_pod > h3 > a')

            for y in dom1:
                try:
                    title_list.append(y.text)
                except TypeError:
                    pass

print(title_list)
