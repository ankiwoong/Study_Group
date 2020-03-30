from random import randint
from time import sleep
from fake_useragent import UserAgent
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import requests
'''
인터넷 영화 데이터베이스(https://www.imdb.com/)
- https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv
? : 리소스 경로 시작의 끝과 매개 변수의 시작
groups=top_1000 : 페이지의 내용
ref_= : 다음 페이지(adv_nxt) 또는 이전 페이지(adv_prv)의 매개 변수 지정
'''


# usaragnt 생성 및 header 정보 생성
ua = UserAgent(verify_ssl=False)
headers = {'User-Agent': ua.random}

# 데이터 추출 리스트 생성
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# 페이지 생성
# 시작 끝 간격
pages = np.arange(1, 1001, 50)

for page in pages:
    # 페이지 파라미터 조합
    page = requests.get("https://www.imdb.com/search/title/?groups=top_1000&start=" +
                        str(page) + "&ref_=adv_nxt", headers=headers)
    # HTML 구문 확인
    soup = BeautifulSoup(page.text, 'html.parser')
    movie_div = soup.find_all('div', class_='lister-item mode-advanced')
    # 크롤링 속도 제어
    # 2 ~ 10초 대기 시간 지정
    sleep(randint(2, 10))

    for container in movie_div:
        # 영화 제목 추출
        name = container.h3.a.text
        titles.append(name)
        # 개봉 년도 추출
        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)
        # 상영 시간 추출
        runtime = container.p.find('span', class_='runtime') if container.p.find(
            'span', class_='runtime') else ''
        time.append(runtime)
        # 평점 추출
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
        # 메타스코어 추출
        m_score = container.find('span', class_='metascore').text if container.find(
            'span', class_='metascore') else ''
        metascores.append(m_score)
        # 투표 / 총 매출 추출을 위한 데이터
        nv = container.find_all('span', attrs={'name': 'nv'})
        # 투표 점수 추출
        vote = nv[0].text
        votes.append(vote)
        # 총 매출 추출
        grosses = nv[1].text if len(nv) > 1 else ''
        us_gross.append(grosses)

# DataFrame 생성
movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
    'timeMin': time
})

# 데이터 전처리 과정 - , 삭제 > 정수
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)
# 데이터 전처리 과정 - ( ) 삭제 > 정수
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
# 데이터 전처리 과정 - 문자 > 특수문자 제거 > 정수
movies['timeMin'] = movies['timeMin'].astype(str)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)
# 데이터 전처리 과정 - 특수문자 제거
movies['metascore'] = movies['metascore'].str.extract('(\d+)')
movies['metascore'] = pd.to_numeric(movies['metascore'], errors='coerce')
# 데이터 전처리 과정 - $ M 제거
movies['us_grossMillions'] = movies['us_grossMillions'].map(
    lambda x: x.lstrip('$').rstrip('M'))
movies['us_grossMillions'] = pd.to_numeric(
    movies['us_grossMillions'], errors='coerce')


# 전처리 과정 후 DataFrame 확인
# print(movies.head())
# print(movies.tail())

# DataFrame 타입 확인
# print(movies.dtypes)

# 결측치 확인
# print(movies.isnull().sum())

# 결측치 데이터 추가
movies.metascore = movies.metascore.fillna("None Given")
movies.us_grossMillions = movies.us_grossMillions.fillna("")

# print(movies['metascore'])
# print(movies['us_grossMillions'])

# CSV 파일 생성
movies.to_csv('movies.csv')
