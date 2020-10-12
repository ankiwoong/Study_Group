"""
주민등록번호
901201-1111111

이메일 주소
ankiwoong@gmail.com

차량 번호
11가 1234
123가 1234

IP 주소
192.168.0.1
"""
import re

# abcd, bpok, desk
# ca?e, cafe, case, cave
# caae, cabe, cace, cabe, ...

p = re.compile("ca.e")
# . : 하나의 문자를 의미 ex>ca.e -> care, cafe, case(o) | caffe(x)
# ^ : 문자열의 시작 ex> ^de -> desk, destination(o) | fade(x)
# $ : 문자열의 끝 ex> se$ -> case, base(o) | face(x)


def print_match(m):
    if m:
        print("m.group() : ", m.group())  # 일치하는 문자열 반환
        print("m.string : ", m.string)  # 입력받은 문자열
        print("m.start() : ", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())  # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())  # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")


# m = p.match("case")  #  mattch : 주어진 문자열의 일치하는지 확인
# print_match(m)
# m = p.match("casd")
# print(m.group())  # 매치되지 않으면 에러가 발생

# m = p.search("careless")  # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("careless")  # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)


"""
1. re.compile('원하는 형태')
2. m = p.match('비교할 문자열') : 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search('비교할 문자열') : 주어진 문자열 중에 일치하는게 있는지 확인
4. lst = p.findall('비교할 문자열') : 일치하는 모든 것을 '리스트' 형태로 반환
"""