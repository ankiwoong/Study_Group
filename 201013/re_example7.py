"""
+ :하나 이상의 발생 항목
ex> "aix+"	
"""
import re

txt = "The rain in Spain falls mainly in the plain!"

# 문자열에 "ai"와 1 개 이상의 "x"문자가 포함되어 있는지 확인합니다.
x = re.findall("aix+", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
