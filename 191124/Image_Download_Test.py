from Crawler import crawler

image_url = 'http://blogfiles.naver.net/20111129_220/ktr38_1322533255591QJtWz_JPEG/s_1210_2011112414293493.jpg'

"""
웹 페이지 크롤링
- 모듈 장점 : 반복적인 코드를 함수로 묶어두고 재사용하기 때문에 전체적인 코드 구현 과정 단축
"""
savename = crawler.download(image_url, filename='download.jpg')

print(savename + '(이)가 저장되었습니다.')
