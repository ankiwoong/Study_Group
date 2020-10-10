a = 10  # 전역 변수, 모든 함수에서 사용 가능


def f1(parma1):  # 파라메터도 지역 변수
    b = 20  # 지역 변수, 함수 f1 밖에서 사용할 수 없다.
    print(a)  # 전역 변수 a를 출력
    print(b)  # 지역 변수 b를 출력
    print(parma1)  # 파라메터 param1을 출력


def f2():
    print(a)  # 전역 변수는 어느 함수에서나 사용 가능
    # print(b)          # 에러 발생, 현재 함수에서 b를 정의하지 않음