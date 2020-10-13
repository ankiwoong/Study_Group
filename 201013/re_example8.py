"""
{} : 정확히 지정된 발생 횟수
ex> "al{2}"		
"""
import re

txt = "The rain in Spain falls mainly in the plain!"

# 문자열에 "a"다음에 정확히 2 개의 "l"문자가 포함되어 있는지 확인합니다.
x = re.findall("al{2}", txt)

print(x)

if x:
    print("Yes, there is at least one match!")
else:
    print("No match")
