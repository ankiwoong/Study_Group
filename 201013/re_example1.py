"""
[] : 문자 집합
ex> "[a-m]"
"""
import re

txt = "The rain in Spain"

x = re.findall("[a-m]", txt)  # "a"와 "m"사이의 모든 소문자를 알파벳순으로 찾습니다.
print(x)
