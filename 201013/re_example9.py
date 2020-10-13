"""
| : 또는
ex> "falls|stays"		
"""
import re

txt = "The rain in Spain falls mainly in the plain!"

# 문자열에 "falls"또는 "stays"가 포함되어 있는지 확인합니다.
x = re.findall("falls|stays", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
