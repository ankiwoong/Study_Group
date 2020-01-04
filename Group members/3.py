from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import numpy as np

r = requests.get("https://kuckjwi0928.github.io/pythoncodingprogram/").text
soup = bs(r, 'html.parser')
texts = soup.find_all('td')

DF = pd.DataFrame(columns=['Name', 'Phone', 'Value'])
for P in range(0, 4):
    if (P % 2 == 0):
        DF.loc[(P//2), ['Name']] = re.split('/', texts[P].text)[0]
        DF.loc[(P//2), ['Phone']] = re.split('/', texts[P].text)[1]
    else:
        pattern = re.compile('[A-Z가-힣]')
        DF.loc[(P//2), ['Value']] = ', '.join(pattern.findall(texts[P].text))

print(DF)
