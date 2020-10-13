"""
^ : 시작
ex> "^hello"
"""
import re

txt = "hello world"

# 문자열이 'hello'로 시작하는지 확인합니다.
x = re.findall("^hello", txt)
if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")
