from Crawler import crawler
from print_df import print_df
from pandas import DataFrame

"""
데이터 수집 - 네이버 메인에서 실시간 검색어 순위 가져오기
"""
# 실시간 검색어 순위에 해당하는 CSS 셀렉터 설정
dom = crawler.select('https://www.naver.com',
                     selector='.ah_roll_area > .ah_l > .ah_item > .ah_a > .ah_k')

# 요소 확인(20개의 원소가 포함된 리스트가 반환)
# print(dom)

"""
데이터 전처리 - 수집 결과가 저장된 리스트의 원소에 대해 반복하면서
랭킹과 키워드를 분리하고 그 결과를 데이터 프레임으로 만들기
"""
# 데이터프레임의 인덱스로 사dyd하기 위해 순위를 저장할 리스트
rank_list = []

# 검색어를 저장할 리스트
keyword_list = []

# 크롤링 결과수 만큼 반복하면서 순위와 검색어를 리스트에 분류
for i, item in enumerate(dom):
    rank_list.append('%02d위' % (i + 1))
    keyword_list.append(item.text.strip())

# 데이터 프레임 생성
df = DataFrame(keyword_list, index=rank_list, columns=['검색어'])

# 데이터 프레임 출력
print_df(df)
