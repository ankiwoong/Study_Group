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
        print(m.group())
    else:
        print("매칭되지 않음")


m = p.match("case")  #  mattch : 주어진 문자열의 일치하는지 확인
print_match(m)
# m = p.match("casd")
# print(m.group())  # 매치되지 않으면 에러가 발생
