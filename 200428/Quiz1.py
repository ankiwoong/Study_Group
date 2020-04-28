'''
문제1 : 암호해독!

세계 최고의 알고리즘 7개를 보유한 알고리즘 제왕 **파이**와 **썬**은 죽기 전, 이 알고리즘에 '암호'를 걸어 세계 어딘가에 묻어놨다고 공표하였다. 그가 남긴 문자는 아래와 같다.

섬으로 향하라!

'   + -- + - + -   '
'   + --- + - +   '
'   + -- + - + -   '
'   + - + - + - +   '

해(**1**)와 달(**0**),
Code의 세상 안으로!(**En-Coding**)

출력조건 : 문자열
'''

text = ['   + -- + - + -   '
        '   + --- + - +   '
        '   + -- + - + -   '
        '   + - + - + - +   ']

print(i.strip().replace(' ', '') for i in text)

print(i.strip().replace(' ', '').replace(
    '+', '1').replace(('-', '0') for i in text))

print(i.strip().replace(' ', '').replace(
    '+', '1').replace(('-', '0'), 2) for i in text)

print(chr(65))
print(ord('A'))
