from pandas import DataFrame
from Data import grade_dic

# 데이터프레임 생성
df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# Series Return
# DataFrame은 Series의 모음
column = df.loc['노진구']
print(type(column))
