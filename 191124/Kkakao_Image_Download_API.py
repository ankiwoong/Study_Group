from Crawler import crawler
import urllib
import json
import datetime as dt

# 페이지를 띄어쓰기 구분으로 가져온다(1page = 50개 / 1 2 -> 100개)
page = map(int, input('검색할 최소페이지 최대페이지의 범위를 입력하세요 : ').split())

# 리스트화
page_list = list(page)

# 시작 페이지
page_min = page_list[0]

# 끝 페이지
page_max = page_list[1]

for num in range(page_min, page_max):
    # 쿼리값으로 던질 키워드(내가 검색해서 저장하고 싶은 단어)
    params_query = input('이미지를 저장할 키워드를 입력하세요 : ')
    """
    kakao developers
    키	    설명	                        필수	        타입
    query	검색을 원하는 질의어	        O	            String
    sort	결과 문서 정렬 방식	            X (accuracy)	accuracy (정확도순) or recency (최신순)
    page	결과 페이지 번호	            X(기본 1)	    1-50 사이 Integer
    size	한 페이지에 보여질 문서의 개수	X(기본 80)	    1-80 사이 Integer
    """
    params = {'page': num, 'size': '80', 'query': params_query}
    # Query String 수정 작업
    query = urllib.parse.urlencode(params)

    # URL + Qureay
    site_url = "https://dapi.kakao.com/v2/search/image?" + query

    # craweler.get를 사용하여 HTML 소스 파싱
    result = crawler.get(site_url)

    # json 형식의 string을 dictionary 형식으로 변경
    data = json.loads(result)
    documents = data['documents']

    for idx, item in enumerate(documents):
        # 저장받는 파일명 지정
        fname = params_query + '_' + dt.datetime.now().strftime('%y%m%d_') + \
            '%02d.png' % idx
        # crawler.download를 사용하여 파일 다운로드 함수 호출
        ok = crawler.download(item['image_url'], filename=fname)
        # 파일 다운로드시 출력
        print('{0} (이)가 저장되었습니다.'.format(ok))
