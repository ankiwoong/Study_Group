from Crawler import crawler

naver_news_url = "https://news.naver.com/main/read.nhn?mode=LS2D&mid=shm&sid1=105&sid2=283&oid=008&aid=0004151505"

"""
웹 페이지 크롤링
- 모듈 장점 : 반복적인 코드를 함수로 묶어두고 재사용하기 때문에 전체적인 코드 구현 과정 단축
"""
element = crawler.select(naver_news_url,
                         encoding="euc-kr", selector='#articleBodyContents')

# 크롤링 결과의 원소 수 만큼 반복하면서 불필요한 태그를 제거한다.
for item in element:
    crawler.remove(item, 'script')
    crawler.remove(item, 'a')
    crawler.remove(item, 'br')
    crawler.remove(item, 'span', {'class': 'end_photo_org'})

    # 크롤링 처리된 최종 결과
    print(item.text.strip())
