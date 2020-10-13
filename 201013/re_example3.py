"""
. : 임의의 문자(새 줄 문자 제외)
ex> "he..o"
"""
import re

txt = "hello world"

x = re.findall("he..o", txt)  # "he"로 시작하고 그 뒤에 두 개의 (임의) 문자와 "o"가 오는 시퀀스를 검색합니다.
print(x)
