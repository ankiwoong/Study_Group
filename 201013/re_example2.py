"""
\ : 특수 시퀀스 신호(특수 문자를 이스케이프하는 데도 사용할 수 있음)
ex> "\d"
"""
import re

txt = "That will be 59 dollars"

x = re.findall("\d", txt)  # 모든 숫자 문자 찾기 :

print(x)
