# 모듈 가져오기
from Crawler import crawler
from print_df import print_df
from pandas import DataFrame
from pandas import concat

s = str(input('검색할 내용을 입력하세요 : '))

# 크롤링 할 사이트 주소 -> 네이버 쇼핑에서 "노트북"으로 검색한 결과
site_url = "https://search.shopping.rla.com/search/all.nhn?origQuery={0}&pagingIndex=1&pagingSize=80&viewType=list&sort=rel&frm=NVSHATC&query={0}".format(
    s)

# 결과를 저장할 빈 데이터 프레임
df = DataFrame()

# 상품 목록 영역 크롤링
html = crawler.select(site_url, selector=".info", encoding="utf-8")

# 검색된 상품목록 영역 수 만큼 반복
for item in html:
    # 하나의 상품 정보를 담기 위한 빈 딕셔너리
    info = {}

    # 상품명 추출
    # -> class 이름으로 상품명 영역 추출
    title_list = item.select('.tit')
    # -> 상품명은 하나만 존재하므로 0번째에 직접 접근하여 텍스트 추출
    title = title_list[0].text.strip()
    # -> 추출된 결과를 빈 딕셔너리에 추가
    info['제품명'] = title

    # 가격 추출
    # -> class 이름으로 가격 영역 추출
    price_list = item.select('.num')
    # -> 가격은 하나만 존재하므로 0번째에 직접 접근하여 텍스트 추출
    price = price_list[0].text.strip()
    # -> 상품 가격에 포함된 콤마를 빈 문자열로 변경
    price = price.replace(",", "")
    # -> 정수형으로 변환
    price = int(price)
    # -> 추출된 결과를 빈 딕셔너리에 추가
    info['가격'] = price

    # 노트북 스팩 영역 추출
    # -> class 이름으로 접근하여 그 하위의 링크 추출
    spec_list = item.select('.detail a')

    # -> 제품별로 스팩 항목이 여러개 이므로 추출된 결과만큼 반복
    for v in spec_list:
        v = v.text.strip()  # -> 텍스트 추출
        tmp = v.split(":")  # -> 콜론으로 분리 (ex: 디스플레이 : 1920x1080 )

        if len(tmp) == 2:  # -> 길이가 2라면 key와 value로 분리하여 딕셔너리에 추가
            key = tmp[0].strip()
            value = tmp[1].strip()
            info[key] = value

    # 개별 상품 정보를 담고 있는 빈 딕셔너리를 데이터 프레임으로 변환
    item_df = DataFrame([info], columns=info.keys())

    # 맨 처음 준비한 빈 딕셔너리에 개별 상품에 대한 데이터 프레임을 병합
    df = concat([df, item_df], sort=False)


# 전체 데이터 프레임 확인
print(df)

# 데이터 프레임을 엑셀로 저장
df.to_excel("{0}.xlsx".format(s), index=False)
