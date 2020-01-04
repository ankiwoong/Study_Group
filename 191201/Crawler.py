import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

"""
pip install BeautifulSoup4
pip install requests
pip install fake-useragent
"""


class Crawler:
    # 멤버변수(1) - 브라우저 버전 정보 문자열
    # User_agent
    user_agent = UserAgent()

    # 멤버변수(2) - 접속에 사용될 세션객체 (생성자에서 사용된다.)
    session = None

    """
    객체가 생성됨과 동시에 크롤러가 웹 페이지에서 접속할 때 사용할 세션을 생성
    세션이 생성되면서 referer 값과 UserAgent 정보를 설정
    """
    # 세션 생성

    def __init__(self, referer=''):
        # 접속에 필요한 정보 구성
        # Authorization : kakao app Key(REST API 키)
        ses_info = {'referer': referer, 'User-agent': self.user_agent.random,
                    'Authorization': 'KakaoAK e1a1063bede7c7a0d87559d66974c2c2'}

        # 세션객체 생성
        self.session = requests.Session()

        # 세션에 접속 정보 설정
        self.session.headers.update(ses_info)

    """
    URL에 접근한 뒤 모든 결과를 텍스트로 리턴하는 함수
    일반 웹페이지 -> JSON
    JSON 웹페이지 -> JSON
    """

    # HTML 소스 파싱
    def get(self, url, encoding='utf-8'):
        # 생성자에서 만든 세션 객체를 사용하여 URL에 접근
        r = self.session.get(url)

        # 에러가 발생했다면 None을 리턴하고 처리 중단
        if r.status_code != 200:
            return None

        # 인코딩 설정
        r.encoding = encoding

        # 결과 문자열의 앞,뒤 공백을 제거한 상태로 리턴
        return r.text.strip()

    """
    웹 페이지의 URL로 접속한 후 특정 CSS 셀렉터에 해당하는 부분만 리턴하는 함수
    """
    # 특정 셀렉터에 대하여 파싱한 결과를 List로 반환

    def select(self, url, selector='html', encoding='utf-8'):
        # 웹 페이지 접속 함수를 호출하여 소스코드 리턴받기
        source = self.get(url, encoding)

        # 리턴값이 없다면 처리 중단
        if not source:
            return None

        # 웹 페이지의 소스코드 HTML 분석 객체로 생성
        soup = BeautifulSoup(source, 'html.parser')

        # CSS 선택자를 활용하여 가져오기를 원하는 부분 지정
        # -> list로 리턴
        return soup.select(selector)

    """
    특정 태그 부분만 제거하는 함수
    """
    # 크롤링한 결과르 원본(item)에서 tag와 selector가 일치하는 항목을 삭제

    def remove(self, item, tag, selector=None):
        for target in item.find_all(tag, selector):
            target.extract()

    """
    파일 다운로드 함수
    """
    # 특정 URL의 파일을 다운로드

    def download(self, url, filename=""):
        # 접속 객체를 사용하여 파라미터로 전달된 URL 다운로드 받기
        r = self.session.get(url, stream=True)

        # 에러여부 검사 - 에러가 발생했다면 None을 리턴하며 처리 종료
        if r.status_code != 200:
            return None

        # 이미지의 byte 데이터를 추출
        img = r.raw.read()

        # 추출한 데이터를 저장
        with open(filename, 'wb') as f:
            f.write(img)

        # 저장된 파일 이름만 리턴
        return filename

    def list2dict(keywords):
        keys = {}
        for keyword in keywords:
            keys[keyword] = 0
        return keys


# 크롤링 클래스에 대한 객체를 생성
# -> 이 파일을 모듈로서 참조하는 다른 파일이 사용할 수 있다.
crawler = Crawler()
