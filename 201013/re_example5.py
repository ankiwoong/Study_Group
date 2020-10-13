"""
$ : 끝
ex> "world$"
"""
import re

txt = "hello world"

# 문자열이 'world'로 끝나는 지 확인 :
x = re.findall("world$", txt)
if x:
    print("Yes, the string ends with 'world'")
else:
    print("No match")
